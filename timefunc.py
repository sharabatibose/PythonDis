import time
my_time=int(input("enter time in seconds:"))
#to countdown an input amount of seconds.
for x in range (my_time, 0, -1):
    seconds= x%60
    minutes= (x//60)%60
    hours= x//3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
#countdown at 1sec gaps 
    time.sleep(1)
