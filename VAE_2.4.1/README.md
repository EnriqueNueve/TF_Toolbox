# VAE with tf==2.4.1
## Stable: Yes

---

## Folder tree 
```bash
.
├── data
│   ├── test.csv
│   └── train.csv
└── vae.ipynb
```

---

## Paper Link
[https://arxiv.org/pdf/1312.6114.pdf](https://arxiv.org/pdf/1312.6114.pdf)

---

## Data
* Download data from [https://www.kaggle.com/zalando-research/fashionmnist](https://www.kaggle.com/zalando-research/fashionmnist)
* Will only use the files train.csv and test.csv from download

---

## Notes
The notes give info on ...

---

## Aditional Resources:
* a
* b

---

## Model declaration and parameters
* codings_size(int): gives dimension of latent space
```Python
model = VAE(codings_size=20)
model.compile(optimizer="rmsprop")
history = model.fit(X_train, X_train, epochs=25, batch_size=128,validation_data=(X_valid, X_valid))
```
