# import os, csv

# os.makedirs("files", exist_ok=True)
# inputID = 6
# inputNAme = input("enter  name ")
# inputAge = input("enter age ")
# inputGrade = input("enter  grade ")
# inputSubjectName = input("enter  subject name ")
# inputMark = input("enter mark ")




# head = ["id", "name", "age", "grade", "subject_name", "mark"]

# data = [
#     [inputID, inputNAme, inputAge, inputGrade, inputSubjectName, inputMark]
#     ]


# with open("files/data.csv", mode="w", encoding="utf-8", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(head)
    
# -------------------------------------------------------------------------------

# with open("files/data.csv", mode="a", encoding="utf-8", newline="") as file:
    
#     addData = csv.writer(file)
#     addData.writerows(data)

# -------------------------------------------------------------------------------
# 2

# with open("files/data.csv", mode="r", encoding="utf-8") as file:
#     readFile = csv.reader(file)
#     x1 = 7
#     x2 = 14
    
#     for row in readFile:
#            print(f"  {row[0]:<{x1}} {row[1]:<{x2}} {row[2]:<{x1}} {row[3]:<{x1}} {row[4]:<{x2}} {row[5]}")
#            print("-" * 62)
    




# with open("files/data.csv", mode="r", encoding="utf-8") as file:
#     readFile = csv.reader(file)
#     x1 = 7
#     x2 = 14
#     enterId = input(f"enter student  id from 1 to 6 ")
#     for row in readFile:
#         if row[0] == enterId:
#            print(f"  {row[0]:<{x1}} {row[1]:<{x2}} {row[2]:<{x1}} {row[3]:<{x1}} {row[4]:<{x2}} {row[5]}")
#            print("-" * 62)
        
# 3
# ----------------------------------------------------------------

# with open("files/data.csv", mode="r", encoding="utf-8") as file:
#    readFile = csv.reader(file)
#    sumIntRow = 0
#    list1 = []
#    inputSubjectName = input("enter subject_name ")
#    for row in readFile:
       
#        if row[4] == inputSubjectName:
#           intRow = int(row[5])
          
#           sumIntRow += intRow
#           list1.append(intRow)
# quantOfList1 = len(list1)
# print(f"average =  {sumIntRow / quantOfList1}")

# ---------------------------------------------------------------
# 4

# with open("files/data.csv", mode="r+", encoding="utf-8", newline="") as file:
#     reader = list(csv.reader(file))
#     writer = csv.writer(file)
    
#     enterID = int(input("enter student id ")) 
#     inputMark = int(input("enter mar "))
    
#     reader[enterID][5] = inputMark
     
#     file.seek(0)
#     writer.writerows(reader)
       
    # inputID += 1















# with open("files/data.csv", mode="r", encoding="utf-8") as file:
#     readFile = csv.reader(file)
#     x1 = 7
#     x2 = 14
#     riko = []
#     for row in readFile:
#            print(f"  {row[0]:<{x1}} {row[1]:<{x2}} {row[2]:<{x1}} {row[3]:<{x1}} {row[4]:<{x2}} {row[5]}")
#            print("-" * 62)
#            if row[0] == "id":
#               continue
#            else:
#               rik = int(row[0])
#               riko.append(rik)
#     sortRik = sorted(riko)
#     print(sortRik)