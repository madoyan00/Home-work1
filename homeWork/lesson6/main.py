my_dict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}

print("studentebis ID: 20, 25, 100, 56, 1232, 846723")
studentsId =  int(input("enter studnet ID "))

for student in my_dict.get("students"):
    studentId = student["id"]
    studentName = student["name"]
    studentAge = student["age"]
    
    for grades in my_dict.get("subjects"):
        subjectId = grades["id"]
        subjectName = grades["name"]
        subjectGrade = grades["grades"][f"{studentsId}"]
        
  
        if studentId == studentsId:
           studentInformation = (f"id: {studentId}, name: {studentName}, age:{studentAge},")
           studentInformation1 = (f"subject: {subjectName}, grade: {subjectGrade}")
           print(studentInformation1)
print(studentInformation)

# საინტერესო დავალება იყო ბევრი ვარიანტები განვიხილე ყველაზე ოპტიმალუ ვარიანტი ეს მიმაჩნია  