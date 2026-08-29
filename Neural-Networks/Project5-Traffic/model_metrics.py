import tensorflow as tf
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from traffic import load_data

model = tf.keras.models.load_model("model.h5")
images, labels = load_data("gtsrb")
labels = tf.keras.utils.to_categorical(labels)

x_train, x_test, y_train, y_test = train_test_split(
    np.array(images), np.array(labels), test_size=0.4, random_state=42
)

y_pred = model.predict(x_test)
y_pred_onehot = np.argmax(y_pred, axis=1)
y_true_onehot = np.argmax(y_test, axis=1)

matrix = confusion_matrix(y_true_onehot, y_pred_onehot)
print(matrix)

report = classification_report(y_true_onehot, y_pred_onehot)
print(report)
