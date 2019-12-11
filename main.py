from getplate import get_vno
from pehchaan import get_det
import re

print("1. Enter vehicle number manually to get its details")
print("2. Detect vehicle number")
print("3. Auto detect vehicle number, and get its details")
ch = input("Enter your choice: ")

if ch == "1":
    vno = input("Enter your vehicle registration number : ")
    pattern = re.compile("^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{3,4}")
    if pattern.match(vno):
        count = 1
        while count >= 1 and count <= 3:
            titles, res = get_det(vno)
            if res == [] or res == list():
                titles, res = get_det(vno)
                count += 1
            else:
                break
        if count == 4:
            count = 1
            print("Invalid Vehicle Number.")
        else:
            print("\n")
            print("--------------------------------------------")
            for i in range(len(titles)):
                print(titles[i], end=" ")
                print(res[i])
            print("--------------------------------------------")
    else:
        print("Enter a valid vehicle registration number")

if ch == "2":
    vno = get_vno("Images/1.jpg")
    print(vno)

if ch == "3":
    vno = get_vno("Images/1.jpg")
    pattern = re.compile("^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{3,4}")
    if pattern.match(vno):
        count = 1
        while count >= 1 and count <= 3:
            titles, res = get_det(vno)
            if res == [] or res == list():
                titles, res = get_det(vno)
                count += 1
            else:
                break
        if count == 4:
            count = 1
            print("Invalid Vehicle Number.")
        else:
            print("\n")
            print("--------------------------------------------")
            for i in range(len(titles)):
                print(titles[i], end=" ")
                print(res[i])
            print("--------------------------------------------")
    else:
        print("Enter a valid vehicle registration number")
