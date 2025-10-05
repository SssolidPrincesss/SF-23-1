import datetime
import time

for i in range(5):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)