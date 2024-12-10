import pandas as pd

# 日付を2006年1月1日から何日経過したか（常に366日）に変換する関数
def days_since_2006_start(date_str):

    date_str = str(date_str)  # 文字列に変換
    year = int(date_str[:4])
    month = int(date_str[4:6])
    day = int(date_str[6:8])
    
    date = pd.Timestamp(year, month, day)
    start_date = pd.Timestamp(2006, 1, 1)
    days_since = (date - start_date).days + 1
    
    return days_since

# データの読み込み
data = pd.read_csv('sample_data.csv')

# 日付データを変換
data['date_count'] = data['date'].apply(days_since_2006_start)

# 必要なデータの選択
newdata = data[['date_count', 'price']]  # 'date_count'と'price'を選択

# データの書き込み
newdata.to_csv('RNN_sample_data.csv', index=False)
