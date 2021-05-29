from datetime import datetime
import playsound
import time

obj_now = datetime.now()

print("Welcome to Kishan's Health Management System")


def playwis():
    playsound.playsound("wis.mp3")


def playmsg():
    playsound.playsound("msg.mp3")


def mask():
    playsound.playsound("mask.mp3")


def answer():
    print("did you completed the following task???")


a = 0
while a < 3:
    time.sleep(0.9)
    print("sanitize")
    playwis()
    answer()
    ans = input("1 for yes || 2 for no")
    if ans == "1":
        f = open("report.txt", "a")
        # f2 = obj_now.hour, ":", obj_now.minute, ":", obj_now.second
        f3 = f.write(f"sanitized at {datetime.now()}")
        # f1 = f.write(str(f2))
        f4 = f.write("\n")

        f.close()

    elif ans == "2":
        print("to kar na")

    else:
        print("enter valid number")

    time.sleep(3.6)
    print("dont remove mask")
    mask()

    time.sleep(1.8)
    print("\nhandwash time")
    playmsg()
    answer()
    ans1 = input("1 for yes || 2 for no")
    if ans1 == "1":
        f = open("report.txt", "a")
        f2 = f.write(f"hand wash at {datetime.now()}")
        # f3 = obj_now.hour, ':', obj_now.minute, ':', obj_now.second
        # f1 = f.write(str(f3))
        f4 = f.write("\n")
        f.close()

    elif ans1 == "2":
        print("to kar na.......")

    a = a+1
