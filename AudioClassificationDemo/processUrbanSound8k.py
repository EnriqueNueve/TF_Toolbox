#!/usr/bin/python
# -*- coding: utf-8 -*-

# Path to install UrbanSounds8k dataset
# wget https://zenodo.org/record/1203745/files/UrbanSound8K.tar.gz -O urban8k.tgz
# tar -xzf urban8k.tgz
# mv UrbanSound8K UrbanSound8k

##############################

"""

TO-DO

1. Data process not all same size, need to fix!

"""

"""
processUrbanSound8k.py

Description: process UrbanSound8k data
Takes one arguments --download_UrbanSound8k (True,False)
Ex: python processUrbanSound8k.py --NCPU 8 --download_UrbanSound8k False
"""

from data_utils import *

import os
import argparse
from glob import glob

import multiprocessing as mp

import tensorflow as tf
from sklearn import preprocessing

import numpy as np
import pandas as pd


##############################
# Declare parser
##############################

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


parser = argparse.ArgumentParser()
parser.add_argument('--download_UrbanSound8k', type=str2bool)
parser.add_argument('--NCPU', type=int)

##############################
# Declare paths for data
##############################

data_path = 'UrbanSound8K'
audio_path = data_path + "/" + 'audio'
meta_path = data_path + "/" +'metadata/' +'UrbanSound8K.csv'

##############################
# Main logic
##############################

if __name__ == '__main__':
    args = parser.parse_args()
    NCPU = args.NCPU

    if args.download_UrbanSound8k == True:

        # #############################

        print('Downloading UrbanSound8k dataset')

        # #############################

        downloadUrbanSound8k()

    # #############################

    print('Load wav file paths into a dict')

    # #############################

    audio_folders = glob(audio_path+"/f*")
    audio_files = {}
    for folder in sorted(audio_folders):
        audio_files[folder.split("/")[-1]] = glob(folder+"/*.wav")
    n_samples = sum([len(audio_files[k]) for k in audio_files.keys()])


    # #############################

    print('Load meta data')

    # #############################

    meta_data = pd.read_csv(meta_path)
    meta_data['duration'] = meta_data['end'] - meta_data['start']

    # #############################

    print('Make tfRecords')

    # #############################

    if not os.path.isdir(data_path + '/tfRecords'):
        os.mkdir(data_path + '/tfRecords')

    all_data = []
    for k in audio_files.keys():
        labels, classIds = [], []
        for sample_path in audio_files[k]:
            sample_name = sample_path.split("/")[-1].split(".")[0]+".wav"
            row = meta_data[meta_data['slice_file_name'] == sample_name]
            sample_label =  row['class'].values[0]
            class_id = row['classID'].values[0]
            labels.append(sample_label)
            classIds.append(class_id)
        new_df = pd.DataFrame(list(zip(audio_files[k],labels,classIds)))
        all_data.append(new_df)

    # #############################

    if not os.path.isdir(data_path+'/tfRecords/MelSpect'):
        os.mkdir(data_path+'/tfRecords/MelSpect')

    with mp.Pool(processes=NCPU) as pool:
        pool.map(writeMelSpect, all_data)

    # #############################

    if not os.path.isdir(data_path+'/tfRecords/MFCC'):
        os.mkdir(data_path+'/tfRecords/MFCC')

    with mp.Pool(processes=NCPU) as pool:
        pool.map(writeMFCC, all_data)

    # #############################

    if not os.path.isdir(data_path+'/tfRecords/Chroma'):
        os.mkdir(data_path+'/tfRecords/Chroma')

    with mp.Pool(processes=NCPU) as pool:
        pool.map(writeChroma, all_data)
