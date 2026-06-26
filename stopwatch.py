import time 
my_time = int(input("enter the time to stop at : "))
for x in range (my_time,0,-1):
    seconds = x % 60 
    minutes = int(x / 60 ) % 60 
    hours = int(x/ 120) % 120

    time.sleep(1)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
print("times up !!!")
