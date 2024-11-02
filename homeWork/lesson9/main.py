# დავალება 1

# int_list = [10,20,30,40]

# def add(numb):
#     numb = eval(input("enter number "))
#     int_list.append(numb)
#     print(int_list)
    
# add(int_list)

# დავალებ 2

def func1(list1):
   list1 = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
   sum = 0
   for i in list1:
      sum += i 
   print(sum)
func1(sum)
    
# დავალება 3

# gl_str = "Global"

# def localFunc():
#     gl_str = "local"
#     return gl_str

# print(localFunc())


# დავალება 4

# def sum(numb):
#     numb = int(input("enter number "))
#     strNUmb = str(numb)
#     sumOfNumb = 0
#     for i in strNUmb:
#       intStrNumb = int(i)
#       sumOfNumb += intStrNumb
#     print(sumOfNumb)
# sum(numb=0)

# 4/1

# def sum(n):    
#     if n == 0 :
#         return 0
#     else:
#         return  n % 10 + sum(n // 10)
# number = 521
# print(sum(number))

# დავალება 5

# def reversStr(str):
#    str = input("enter string ")
#    return str[::-1] 
# print(reversStr(str)) 



# 5/1


# def reversString(s):

#     if len(s) == 0:
#         return s
#     else:
#         return s[-1] + reversString(s[:-1])
# s1 = "vazgen"
# print(reversString(s1))
    
