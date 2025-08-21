
# Neural Network Image Classification – Quick Reference Notes

## 1. Import Libraries
```python
import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt
import math
```

- **tensorflow**: Core machine learning framework.
- **tensorflow_datasets**: Loads common datasets.
- **numpy**: Array manipulation.
- **matplotlib**: Visualization.

---

## 2. Load and Inspect Dataset
```python
dataset, metadata = tfds.load('fashion_mnist', as_supervised=True, with_info=True)
train_dataset, test_dataset = dataset['train'], dataset['test']

num_train_examples = metadata.splits['train'].num_examples
num_test_examples = metadata.splits['test'].num_examples
class_names = metadata.features['label'].names
```
- **fashion_mnist**: 28×28 grayscale clothing images.
- `as_supervised=True` returns `(image, label)` pairs.
- `metadata` contains info like label names and counts.

---

## 3. Normalize Data
```python
def normalize(images, labels):
    images = tf.cast(images, tf.float32) / 255.0
    return images, labels

train_dataset = train_dataset.map(normalize).cache()
test_dataset  = test_dataset.map(normalize).cache()
```
- Convert pixel values to `float32`.
- Scale pixels from 0–255 → 0–1.

---

## 4. Prepare Data for Training
```python
BATCH_SIZE = 32
train_dataset = train_dataset.shuffle(num_train_examples).batch(BATCH_SIZE).repeat()
test_dataset  = test_dataset.batch(BATCH_SIZE)
```
- **Shuffle**: randomize order.
- **Batch**: process groups of images together.
- **Repeat**: avoid running out of data during training.

---

## 5. Build the Model
```python
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28, 1)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
```
- **Flatten**: converts image to 1D vector.
- **Dense(128, relu)**: hidden layer with ReLU activation.
- **Dense(10, softmax)**: outputs probability for each of 10 classes.

---

## 6. Compile the Model
```python
model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=['accuracy']
)
```
- **Adam** optimizer: adaptive learning.
- **SparseCategoricalCrossentropy**: loss for integer labels.
- **Accuracy**: performance metric.

---

## 7. Train the Model
```python
model.fit(train_dataset, epochs=5,
          steps_per_epoch=math.ceil(num_train_examples / BATCH_SIZE))
```
- **epochs**: full passes through the dataset.
- **steps_per_epoch**: batches per epoch.

---

## 8. Evaluate / Predict
```python
for test_images, test_labels in test_dataset.take(1):
    test_images = test_images.numpy()
    test_labels = test_labels.numpy()

predictions = model.predict(test_images)
```
- Get model predictions on test images.

---

## 9. Predict Single Image
```python
img = test_images[0]
img = np.expand_dims(img, 0)  # batch of 1
predictions_single = model.predict(img)
```

---

## 10. Visualization Helpers
- Plot image with predicted label and confidence.
- Plot bar chart of probabilities.

---

## Quick Tips
- Increase `epochs` for better accuracy.
- Add more layers for complex patterns.
- Try `Conv2D` layers for better image performance.
- Adjust learning rate: `tf.keras.optimizers.Adam(learning_rate=...)`.
