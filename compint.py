duration= input("enter duration (yearly/monthly/halfyearly/quarterly): ")
principal= float(input("enter principal amt: "))
rate = 0.06
timeyears= 4
if duration=="yearly":
    y=1
if duration=="monthly":
    y=12
if duration=="quarterly":
    y=4
if duration=="halfyearly":
    y=2
ci= principal*(1+(rate/y))**(timeyears*y)-principal
print("compound interest is:", ci)


