# MADE with tf==2.4.1
## Stable: Yes

---

## Folder tree 
```bash
.
├── binarized_mnist.npz
└── made.ipynb
```

---

## Paper Link
[https://arxiv.org/abs/1502.03509](https://arxiv.org/abs/1502.03509)

---

## Data
* Download data from [https://github.com/aiddun/binary-mnist/tree/master/original_28x28/binary_digits_all_pixels](https://github.com/aiddun/binary-mnist/tree/master/original_28x28/binary_digits_all_pixels)
* Or you can just use any version of mnist and then round the values to 0 or 1

---

## Aditional Resources:
* [Video commentary](https://www.youtube.com/watch?v=7q4ueFiJjAY)

---

## Model declaration and parameters
* n_mask(int): gives number of masks
* input_dim(int): gives dimension of input 
* hidden_dim(int): gives dimension of hidden layers
* hid_layers(int): gives number of hidden layers
```Python
n_mask = 8
input_dim = 784
hidden_dim = 500
hid_layers = 1

lr_schedule = keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=1e-3,
    decay_steps=10000,
    decay_rate=0.9)
opt = keras.optimizers.Adam(learning_rate=lr_schedule)

model = MADE(n_mask,input_dim,hidden_dim,hid_layers)
#model.compile(optimizer=opt,run_eagerly=True)
model.compile(optimizer=opt) 

history = model.fit(X_train, X_train, epochs=25, batch_size=100,validation_data=(X_val, X_val))
```

