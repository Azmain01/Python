class Student:
    def __init__(self, sid, name, age, grade, gender, email, phone, marks):
        self.sid = sid
        self.name = name
        self.age = age
        self.grade = grade
        self.gender = gender
        self.email = email
        self.phone = phone
        self.marks = marks

    def average(self):
        return round(sum(self.marks.values()) / len(self.marks), 2)

    def display(self):
        print("-" * 50)
        print(f"ID       :  {self.sid}")
        print(f"Name     :  {self.name}")
        print(f"Age      :  {self.age}")
        print(f"Grade    :  {self.grade}")
        print(f"Gender   :  {self.gender}")
        print(f"Email    :  {self.email}")
        print(f"Phone    :  {self.phone}")
        print(f"Marks    :")
        for sub, mark in self.marks.items():
            print(f"  {sub:<8}: {mark}")
        print(f"Average  :  {self.average()}")
        print("-" * 50)


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student, silent=False):
        if student.sid in self.students:
            if not silent:
                print("Student added successfully")

    def update_student(self, sid):
        s = self.students.get(sid)
        if not s:
            print("Student not found")
            return
        
        s.name = input("New Name:  ")
        s.age = int(input("New Age:  "))
        s.grade = int(input("New Grade:  "))
        s.gender = input("New Gender:  ")
        s.email = input("New Email:  ")
        s.phone = input("New Phone:  ")
        s.marks = {
            "Math": int(input("Math :  ")),
            "Science": int(input("Science :  ")),
            "English": int(input("English :  "))
        }

        print("Student updated successfully")