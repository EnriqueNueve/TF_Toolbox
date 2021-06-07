# IRMAE with tf==2.5.0
## Stable: Yes

---

## Folder tree 
```bash
.
├── Notes/irmae_diagram
└── irmae.ipynb
```

---

## Paper Link
[https://arxiv.org/abs/2010.00679](https://arxiv.org/abs/2010.00679)

---

## Data
* Imported from keras
---

## Model declaration and parameters
```Python
irmae = IRMAE((32,32,1))
irmae.compile(optimizer='adam')
irmae.fit(X_train, X_train, validation_data=(X_val, X_val),epochs=30, batch_size=32)
```
