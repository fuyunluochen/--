from Datetime import datatime
from playsound import playsound

alarm_time = input("请输入闹钟时间，实例:09：50：00 am\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("完成闹钟设置")
while True:
    now = datatime.now()
    current_hour = now.strftime("%I")
    currend_minute = now.strftime("%M")
    currend_seconds = now.strftime("%S")
    currend_period = now.strftime("%P")
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == currend_minute:
                if alarm_seconds == currend_seconds:
                    print("起来啦")
                    playsound('break.mp3')
                    break
