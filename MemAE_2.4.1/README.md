# Memory Augmented AutoEncoder with tf==2.4.1
## Stable: Yes

---

## Folder tree 
```bash
.
├── /Fmnist
└── MemoryAEE.ipynb
```

---

## Paper Link
[https://arxiv.org/abs/1904.02639](https://arxiv.org/abs/1904.02639)

---

## Data
* Download data from [https://www.kaggle.com/zalando-research/fashionmnist](https://www.kaggle.com/zalando-research/fashionmnist)

---


## Model declaration and parameters

```Python
model = MemAE()
model.compile(optimizer=keras.optimizers.Adam())
model.fit(X_train,validation_data=(X_valid,X_valid), epochs=50, batch_size=32)
```

