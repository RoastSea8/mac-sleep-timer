import os
from datetime import datetime, timedelta

now_plus_delta = (datetime.now() + timedelta(minutes = int(input("set sleep timer (mins): ")))).strftime('%H:%M:%S')
print("sleep timer set for ", now_plus_delta)
while (datetime.now().strftime('%H:%M:%S') != now_plus_delta):
	pass
os.system("pmset sleepnow")