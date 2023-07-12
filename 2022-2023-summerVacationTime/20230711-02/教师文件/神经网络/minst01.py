from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

# 加载MNIST数据集
mnist = keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 数据预处理
X_train = X_train / 255.0
X_test = X_test / 255.0
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# 编译模型
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
# 训练模型
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test), verbose=0)

# 绘制训练误差和测试误差随迭代次数的变化曲线
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Test Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
# 绘制训练精度和测试精度随迭代次数的变化曲线
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
#真实值与预测值的散点图
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)
plt.scatter(y_test,predicted_classes)
plt.xlabel('y_test')
plt.ylabel('predicted_classes')
plt.legend()
plt.show()