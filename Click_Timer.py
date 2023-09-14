from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import pause
from datetime import datetime
from datetime import timedelta

print("Welcome to Click Timer Program!")
print("To cancel the program you can close the program")
print("Bring your mouse arrow on where you want to be clicked on your time and unplug your mouse")
print("Please Enter Your Desired Time: (h:m) (4 pm is 16 => For Example: 16:15) (If the hour of the time you enter is past in your day, timer will set your time for tommorow)")

try:
    input_time = input().split(":")

    mydatestring = str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(datetime.now().day)

    mydate = datetime.strptime(mydatestring, "%Y-%m-%d")

    if int(input_time[0]) < datetime.now().hour or (int(input_time[0]) == datetime.now().hour and int(input_time[1]) < datetime.now().minute):
        mydate = mydate + timedelta(days=1)

    print("Timer set for " + str(datetime(mydate.year,
                mydate.month, mydate.day, int(input_time[0]), int(input_time[1]), 0)))


    pause.until(datetime(mydate.year,
                mydate.month, mydate.day, int(input_time[0]), int(input_time[1]), 0))

    mouse = Controller()
    mouse.click(Button.left)

except:
    print('Error! Press Enter to Close')
    input()