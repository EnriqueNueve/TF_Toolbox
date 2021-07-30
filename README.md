# TF_Toolbox
An organized repo for all things TensorFlow: tutorials, data, and models. 

## Lectures
---
1. Transformers: https://www.youtube.com/watch?v=XSSTuhyAmnI
2. Some intro to advance math topics: https://www.youtube.com/c/FacultyofKhan/playlists
3. Linear Algebra for ML: https://www.youtube.com/watch?v=Cx5Z-OslNWE&list=PLUl4u3cNGP63oMNUHXqIUcrkS2PivhN3k


## Code Resources
---
1. Tensorflow Prob: https://github.com/mohd-faizy/Probabilistic-Deep-Learning-with-TensorFlow
2. Einops: https://github.com/arogozhnikov/einops
3. Debugging book: https://www.debuggingbook.org/
4. CNN visualization callbacks: https://github.com/sicara/tf-explain
5. Seq2Seq learning in tf2: https://github.com/OpenNMT/OpenNMT-tf
6. Quantization library for keras in TensorFlow: https://github.com/google/qkeras
7. Tensorflow addons: https://github.com/tensorflow/addons
8. Torch2RT: https://github.com/NVIDIA-AI-IOT/torch2trt
9. Zero to Mastery TensorFlow for Deep Learning: https://dev.mrdbourke.com/tensorflow-deep-learning/
10. Keras-flops: https://pypi.org/project/keras-flops/
11. Numerical methods in Python: https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html
12. TF ML Production course: https://blog.tensorflow.org/2021/06/mlep-courses.html
13. Domain generalization: https://github.com/facebookresearch/DomainBed
14. Tensorflow garden: https://github.com/tensorflow/models
15. GLOM: https://github.com/Rishit-dagli/GLOM-TensorFlow
16. DL Forecasting tools: https://github.com/AIStream-Peelout/flow-forecast
17. TensorBoard: https://www.tensorflow.org/tensorboard
18. Tensorflow Best Practice Twitter: https://twitter.com/tfbestpractices?lang=en
19. Speech recognition: https://github.com/cosmoquester/speech-recognition
20. Generative models: https://github.com/an-seunghwan/generative
21. GCN example: https://github.com/kerighan/simple-gcn
22. Efficient-CapsNet: https://github.com/EscVM/Efficient-CapsNet
23. Retinanet: https://github.com/srihari-humbarwadi/retinanet-tensorflow2.x
24. YoloV4: https://github.com/taipingeric/yolo-v4-tf.keras
25. Gpu Monitor: https://github.com/sicara/gpumonitor
26. Normalizing Flow Reference: https://github.com/bgroenks96/normalizing-flows
27. GrapGallery: https://github.com/EdisonLeeeee/graphgallery
28. SingleShot: https://github.com/srihari-humbarwadi/ssd_tensorflow
29. YOLOACT: https://github.com/leohsuofnthu/Tensorflow-YOLACT

## Build principles
* Make a simple version first and iterate
* Draw out path of outcomes and consequences 

## Steps to implement a model
---
1. Implement custom functions.
2. Implement custom layers to store custom functions, if possible.
3. Implement custom model that joins custom functions and layers.
4. Test pass of random data and check dimensionality. 
5. Train model on one piece of data and make sure it learns.
6. Test on all training data.  

![GitHub Logo](/images/steps_implement_diagram.png)

---

## Tutorials 
---

0. tfRecord demo with tf==2.4.1
1. einsum demo 

---

## Models
#### Please read "model_standards.ipynb" to understand implementation guidelines!

---

0. model_a with tf==0.0.0
  * Notes: (yes/no)
  * Paper Link: [arxiv demo link ](https://arxiv.org/)
  * Additional Resources: (yes/no)
  * State: (stable, not stable)

---

1. VAE with tf==2.4.1
  * Notes: yes
  * Paper Link: [https://arxiv.org/pdf/1312.6114.pdf ](https://arxiv.org/pdf/1312.6114.pdf)
  * Additional Resources: yes
  * State: stable

---

2. NICE with tf==2.4.1 and tfp==0.12.1
  * Notes: yes
  * Paper Link: [https://arxiv.org/abs/1410.8516 ](https://arxiv.org/abs/1410.8516)
  * Additional Resources: yes
  * State: stable

---

3. MADE with tf==2.4.1 
  * Notes: No
  * Paper Link: [https://arxiv.org/abs/1502.03509 ](https://arxiv.org/abs/1502.03509)
  * Additional Resources: yes
  * State: stable

---

4. CVAE with tf==2.4.1
  * Notes: yes
  * Paper Link: [https://proceedings.neurips.cc/paper/2015/file/8d55a249e6baa5c06772297520da2051-Paper.pdf](https://proceedings.neurips.cc/paper/2015/file/8d55a249e6baa5c06772297520da2051-Paper.pdf)
  * Additional Resources: no
  * State: stable

---

5. MemAE with tf==2.4.1
  * Notes: yes
  * Paper Link: [https://arxiv.org/abs/1904.02639](https://arxiv.org/abs/1904.02639)
  * Additional Resources: no
  * State: stable

---

6. TransformerBlock with tf==2.5.0
  * Notes: yes
  * Paper Link: [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)
  * Additional Resources: yes
  * State: stable

---

7. IRMAE with tf==2.5.0
  * Notes: yes
  * Paper Link: [https://arxiv.org/abs/2010.00679](https://arxiv.org/abs/2010.00679)
  * Additional Resources: no
  * State: stable

---

8. Mixup with tf==2.5.0
  * Notes: no
  * Paper Link: [https://arxiv.org/abs/1710.09412](https://arxiv.org/abs/1710.09412)
  * Additional Resources: no
  * State: stable


---

9. AudioClassDemo with tf==2.5.0
  * Notes: no
  * Paper Link: no
  * Additional Resources: no
  * State: stable
