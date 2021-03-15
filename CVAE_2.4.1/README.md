# CVAE with tf==2.4.1
## Stable: Yes

---

## Folder tree 
```bash
.
├── Notes
│   └── CVAE_Notes.pdf
├── cvae.ipynb
└── data
    ├── test.csv
    └── train.csv
```

---

## Paper Link
[https://proceedings.neurips.cc/paper/2015/file/8d55a249e6baa5c06772297520da2051-Paper.pdf](https://proceedings.neurips.cc/paper/2015/file/8d55a249e6baa5c06772297520da2051-Paper.pdf)

---

## Data
* Download data from [https://www.kaggle.com/zalando-research/fashionmnist](https://www.kaggle.com/zalando-research/fashionmnist)
* Will only use the files train.csv and test.csv from download

---

## Notes
* CVAE_Notes.pdf: shows objective for CVAE

---

## Model declaration and parameters
* codings_size(int): gives dimension of latent space
```Python
model = CVAE(codings_size=20)
model.compile(optimizer="rmsprop")
history = model.fit([X_train,y_train], X_train, epochs=50, batch_size=128,validation_data=([X_valid,y_valid], X_valid))
```
