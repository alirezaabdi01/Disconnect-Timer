import subprocess
import os
import pause
from datetime import datetime
from datetime import timedelta
import ctypes, os

try:
    exit_after_finish = False
    Index = -1
    clear = lambda: os.system('cls')
    selected_adapter = ""

    print("Welcome to Adapter Timer Program!")
    print("Made by: https://github.com/alirezaabdi01")
    print("You can select your adapter and set a timer for disabling and enabling your adapter")

    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if not is_admin:
        print("Error! Please Run As Administator!")
        print("Press Enter To Exit")
        input()

    adaptors_list = str(subprocess.check_output('wmic nic get name,index')).split("\\r\\r\\n")

    adaptors_list[0] = adaptors_list[0][2:]
    adaptors_list.pop()

    for adapter in adaptors_list:
        print(adapter)
        print('')

    print("Enter your Adapter Index:")
    index = int(input())

    while 0 > index or index > int(adaptors_list[-2].split("     ")[0]):
        print()
        print('Error! Wrong index!')
        print()
        print("Enter your Adapter Index:")
        index = int(input())

    for adapter in adaptors_list:
        if not adapter.startswith("I"):
            if int(adapter.split("     ")[0]) == index:
                selected_adapter = adapter.split("     ")[1]
                break

    while True:
        clear()

        print("Selected_adapter:" + selected_adapter)
        print()
        print("1. Enable Adapter")
        print("2. Disable Adapter")
        print("3. Set time to Enable Adapter")
        print("4. Set time to Disable Adapter")
        print("5. Exit")
        print("Please Enter Your Command Number:")

        _input = int(input())

        while _input < 0 or _input > 6:
            print()
            print("Wrong Number!")
            print()
            print("Please Enter Your Command Number:")

            _input = int(input())

        if _input == 1:
            subprocess.check_output('wmic path win32_networkadapter where index=' + str(index) + ' call enable')
        elif _input == 2:
            subprocess.check_output('wmic path win32_networkadapter where index=' + str(index) + ' call disable')
        elif _input == 3:
            exit_after_finish = True

            print("Please Enter Your Desired Time: (h:m) (4 pm is 16 => For Example: 16:15) (If the hour of the time you enter is past in your day, timer will set your time for tommorow)")
            input_time = input().split(":")
            
            mydatestring = str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(datetime.now().day)

            mydate = datetime.strptime(mydatestring, "%Y-%m-%d")

            if int(input_time[0]) < datetime.now().hour or (int(input_time[0]) == datetime.now().hour and int(input_time[1]) < datetime.now().minute):
                mydate = mydate + timedelta(days=1)

            print("Timer set for " + str(datetime(mydate.year,
                        mydate.month, mydate.day, int(input_time[0]), int(input_time[1]), 0)))
            print("To cancel the program you can close the program")

            pause.until(datetime(mydate.year,
                        mydate.month, mydate.day, int(input_time[0]), int(input_time[1]), 0))

            subprocess.check_output(
                'wmic path win32_networkadapter where index=' + str(index) + ' call enable')

        elif _input == 4:
            exit_after_finish = True
            print("Please Enter Your Desired Time: (h:m) (4 pm is 16 => For Example: 16:15) (If the hour of the time you enter is past in your day, timer will set your time for tommorow)")
            input_time = input().split(":")
            
            mydatestring = str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(datetime.now().day)

            mydate = datetime.strptime(mydatestring, "%Y-%m-%d")

            if int(input_time[0]) < datetime.now().hour or (int(input_time[0]) == datetime.now().hour and int(input_time[1]) < datetime.now().minute):
                mydate = mydate + timedelta(days=1)

            print("Timer set for " + str(datetime(mydate.year,
                        mydate.month, mydate.day, int(input_time[0]), int(input_time[1]), 0)))
            print("To cancel the program you can close the program")

            pause.until(datetime(mydate.year,
                        mydate.month, mydate.day, int(input_time[0]), int(input_time[1]), 0))

            subprocess.check_output(
                'wmic path win32_networkadapter where index=' + str(index) + ' call disable')

        elif _input == 5:
            break

        if exit_after_finish:
            break

except:
    print('Error! Press Enter to Close')
    input()