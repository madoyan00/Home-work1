# დავალება 1

x = eval(input("enter number: "))
arr = [44, 23, 11, 8, 20, 56, 33, 55]

if x in arr:
    print("The number in list")
else:
    print("The number not in list")

# დავალება 2

x = eval(input("enter number: "))
if x % 2 == 0:
 print("The number is even")
elif x % 2 == 1:
 print("The number is odd")
else:
   print("Error")

# დავალება 3

st1 = "xukas"
st2 = "gexam"

if st1 is st2:
    print("Same object")
else:
    print("Different object")

# დავალება 4


arr = [44, 23, 11, 8, 20, 56, 33, 55]
x = eval(input("enter number: "))

if arr[2] < x < arr[-1]:
    print("More than list elements")
if x == arr[5]:
    print("Equal")
else:
    print("None of the conditions were met")