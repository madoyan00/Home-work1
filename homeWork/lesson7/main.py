# დავალება 1

# set1 = set(input("number ").split())

# print(set1, type(set1))

# დავალება 2

# fset = frozenset({eval(input("number "))})
# print(fset, type(fset))

# დავალება 3

# set1 = {1, 22, 3, 4, 5}
# set2 = {11, 22, 33, 44, 55}

# print(tuple(set1.intersection(set2)))

# დავალება 4

# tuple = (eval(input("enter number ")))
# list = []
# for i in tuple:
#     if i not in list:
#      list.append(i)
# print(list)
# number = list(set(tuple(map(eval, input("enter number ").split()))))
# print(number)

# დავალება 5

# list = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
# for i in list:
#    name = i[0]
#    age = i[1]
#    print(f"name: {name}, age: {age}")

# დავალება 6

list1 = ["Irakli", "Giorgi", "Nona", "Oto"]
list2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
for i in list1:
    for x in list2:
        if i == x:
            print(i)
#მეექვსე დავალება  შეიძლება არასწორად იყოს რაღაცა  ვერ გავიგე ნორმალურად ფუნქცია დავწერე რო  დაბეჭდოს ის ელემენტებიო რომლებიც არიან ორივე სიაშიც