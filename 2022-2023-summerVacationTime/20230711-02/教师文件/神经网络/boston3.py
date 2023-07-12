import tensorflow as tf
from keras.datasets import boston_housing
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

# 加载波士顿房价数据集
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

# 数据预处理
mean = x_train.mean(axis=0)
std = x_train.std(axis=0)
x_train = (x_train - mean) / std
x_test = (x_test - mean) / std

# 构建模型
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(13,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))

# 编译模型
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# 训练模型
history = model.fit(x_train, y_train, validation_data=(x_test, y_test),epochs=100, batch_size=32, verbose=1)

# 绘制损失值变化图
loss = history.history['loss']
epochs = range(1, len(loss) + 1)

plt.plot(epochs,history.history['loss'], label='Train Loss')
plt.plot(epochs,history.history['val_loss'], label='Test Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
# plt.legend()
plt.show()

# 进行预测
predictions = model.predict(x_test)

# 绘制预测值和标签值的变化图
plt.plot(range(len(predictions)), predictions, 'b', label='Predictions')
plt.plot(range(len(y_test)), y_test, 'r', label='Labels')
plt.title('Predictions vs Labels')
plt.xlabel('Samples')
plt.ylabel('House Price')
# plt.legend()
plt.show()
#真实值与预测值的散点图
plt.scatter(y_test,predictions)
plt.xlabel('y_test')
plt.ylabel('predictions')
# plt.legend()
plt.show()