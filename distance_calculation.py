# %%%%("this programme will work out how far someone has travelled in miles if you enter speed and time time travelled.")
 
speed = int(input("please enter the speed the vehicle was driving at"))
 
time_hours = int(input("enter hours travelled"))
time_mins = int(input("Enter minutes travelled"))/60
time_sec = int(input("Enter seconds travelled"))/3600
 
totaltime = time_hours+time_mins+time_sec
 
distance = totaltime
distance = round(distance,1)
 
print("distance travelled by the vehicle is %%s miles")