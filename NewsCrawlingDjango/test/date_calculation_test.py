import datetime

input_start_date = input('시작 날짜를 입력하세요(YYYYMMDD) : ')
print(int(input_start_date[0:4]), int(input_start_date[4:6]), int(input_start_date[6:8]))
startdate = datetime.date(int(input_start_date[0:4]), int(input_start_date[4:6]), int(input_start_date[6:8]))
input_finish_date = input('끝나는 날짜를 입력하세요(YYYYMMDD) : ')
finishdate = datetime.date(int(input_finish_date[0:4]), int(input_finish_date[4:6]), int(input_finish_date[6:8]))

day_count = (finishdate - startdate).days + 1
for d in (startdate + datetime.timedelta(n) for n in range(day_count)):
        date = str(d)
        date = str(date[0:4]) + str(date[5:7]) +str(date[8:10])
        print(date)