# დავალება 1

# number = int(input("შეიყანეთ  რიცხვი "))
# i = 1

# sum = 0
# while i <= number:
#     sum += i
#     i += 1
# print("ჯამი =", sum)

# # დავალება 2

# number = int(input("შეიყანეთ  რიცხვი "))

# while number > 0:
#     print(number)
#     number -= 1

# დავალება 3
   
# from random import randint

# num = randint(1, 100)
# i = 1

# print("თქვენ უნდა გამოიცნოთ რანდომ რიცხვი თქვენ გაქვთ 7 ცდა")

# while True:
#   guess = int(input(f"ცდა: #{i}. შეიყავანეთ რიცხვი "))

#   if guess == num:
#    print(f"You win!!! it was {num}")
#    break
#   elif guess > num:
#    print("To great!")
#   else:
#    print("To less!")
#    print()
#   i += 1
  

# დავალება 4

total_sum = 0

while True:
 k = eval(input("შეიყვანეთ რიცხვი "))
 if k == sum:
  print(f"Game Over {total_sum}")
 elif k > 0:
  total_sum = total_sum + k
 else:
  continue
 