from datetime import datetime

def day_of_year_always_366(year, month, day):
    # 指定された年、月、日の日付を作成
    date = datetime(year, month, day)
    
    # その年の1月1日の日付を作成
    start_of_year = datetime(year, 1, 1)
    
    # 2つの日付の差分を計算し、日数に変換
    day_of_year = (date - start_of_year).days + 1
    
    # 閏年かどうかのチェック
    is_leap_year = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
    
    # 閏年でない場合、2月29日以降の日付を1日進める
    if not is_leap_year and (month > 2 or (month == 2 and day == 29)):
        day_of_year += 1
    
    return day_of_year

# 使用例
year = 2023  # 2月29日が無い年
month = 1
day = 31
print(f"The date {year}-{month}-{day} is day {day_of_year_always_366(year, month, day)} of the year.")

year = 2024  # 2月29日がある年（閏年）
month = 1
day = 31
print(f"The date {year}-{month}-{day} is day {day_of_year_always_366(year, month, day)} of the year.")
