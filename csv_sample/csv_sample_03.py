import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# データの読み込み
data = pd.read_csv('RNN_sample_data.csv')

# 結果を表示
print(data['date_count'], data['price'])

# データの長さを取得
length_of_sequences = len(data)

maxlen = 25

x = []
t = []

# x と t のデータを作成
for i in range(length_of_sequences - maxlen):
    x.append(data['price'][i:i+maxlen].values)
    t.append(data['price'][i+maxlen])

x = np.array(x).reshape(-1, maxlen, 1)
t = np.array(t).reshape(-1, 1)

# データをトレーニングセットと検証セットに分割
x_train, x_val, t_train, t_val = train_test_split(x, t, test_size=0.2, shuffle=False)

# 結果の確認
print("x_train shape:", x_train.shape)
print("x_val shape:", x_val.shape)
print("t_train shape:", t_train.shape)
print("t_val shape:", t_val.shape)
