# NICE with tf==2.4.1 & tfp==0.12.1
## Stable: Yes

---

## Folder tree 
```bash
.
├── NICE.ipynb
├── Notes\ NICE_formulas.pdf
├── mnist_784.csv
└── nice_weights.h5
```

---

## Paper Link
[https://arxiv.org/pdf/1410.8516.pdf](https://arxiv.org/pdf/1410.8516.pdf)

---

## Data
* Data is collected from [https://www.kaggle.com/scolianni/mnistasjpg](https://www.kaggle.com/scolianni/mnistasjpg)

---

## Notes
* NICE_formulas.pdf: shows how to calculate loss, foward pass, and inverse pass.

---

## Aditional Resources:
* Normalizing flow[ blog](https://lilianweng.github.io/lil-log/2018/10/13/flow-based-deep-generative-models.html#glow)

---

## Model declaration and parameters
* input_dim(int): dimensions of input vector 
* n_couple(int): number of couple layers 
* couple_dim(int): dimensions of hidden layers in couple layers
```Python
lr_schedule = keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=3e-4,
    decay_steps=10000,
    decay_rate=0.9)
opt = keras.optimizers.Adam(learning_rate=lr_schedule)

model = NICE(input_dim=784,n_couple=4,couple_dim=1000)
model.compile(optimizer=opt)

history = model.fit(X_train, y_train, validation_data=(X_val, y_val),\
                    epochs=100, batch_size=200)
to-do
```
