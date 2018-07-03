import time
import webbrowser

total_breaks = 3
break_count = 0

while (break_count < total_breaks):
    time.sleep(60 * 75)
    webbrowser.open("http://blog.csdn.net/luosec/article/details/61645925")
    break_count = break_count + 1

