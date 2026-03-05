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
         
    def delete_student(self,said):
        if self.students.pop(sid, None):
            print("Student removed successfully")
        else:
            print("Student not found")

    def search_student(self, sid):
        s = self.students.get(sid)
        if s:
            s.display()
        else:
            print("Student not found")

    def display_all(self):
        if not self.students:
            print("No records found")
            return
        for s in self.students.values():
            s.display()

    def load_demo_data(self):
        demo = [
            ("S001","Nishaj Ronak",9,3,"Male","nishaj@gmail.com","01711111111",{"Math":85,"Science":90,"English":78}),

            ("S002","Abrar Abdullah",8,3,"Male","abrar@gmail.com","01711111112",{"Math":88,"Science":91,"English":80}),

            ("S003","Safwana Hossain",7,2,"Female","safwana@gmail.com","01711111113",{"Math":92,"Science":89,"English":87}),

            ("S004","Sarjita Somadder",6,1,"Female","sarjita@gmail.com","01711111114",{"Math":81,"Science":85,"English":79}),

            ("S005","Rahim Uddin",10,4,"Male","rahim@gmail.com","01711111115",{"Math":77,"Science":80,"English":75}),

            ("S006","Karim Ahmed",11,5,"Male","karim@gmail.com","01711111116",{"Math":84,"Science":83,"English":82}),

            ("S007","Nusrat Jahan",12,6,"Female","nusrat@gmail.com","01711111117",{"Math":89,"Science":92,"English":90}),

            ("S008","Arif Khan",13,7,"Male","arif@gmail.com","01711111118",{"Math":78,"Science":75,"English":80}),

            ("S009","Sadia Rahman",14,8,"Female","sadia@gmail.com","01711111119",{"Math":91,"Science":93,"English":89}),

            ("S010","Tamim Iqbal",15,9,"Male","tamim@gmail.com","01711111120",{"Math":86,"Science":84,"English":88})]
        for s in demo:
            self.add_student(Student(*s), silent=True)
def menu():
    print("\nSTUDENT MANAGMENT SYSTEM")
    print("1. Show All Students")
    print("2. Search Student")
    print("3. Add student ")
    print("4. Update Student")
    print("5. Dlete Student")
    print("0. Exit")
    print("-" * 50)

def main():
    sm = studentManager()
    sm.load_demo_data()

    while True:
        menu()
        ch = input("Select Option:  ")

        if ch == "1":
            sm.display_all()

        elif ch == "2":
            sm.search_student(input("Student ID:  "))

        elif ch == "3":
            sid = input("ID:  ")
            name = input("Name:  ")
            age = int("Age:  ")
            grade = int("Grade:  ")
            gender = input("Gender:  ")
            email  = input("Email:  ")
            phone  = input("Phone:  ")
            marks = {
                "Math": int(input("Math: ")),
                "Science": int(input("Science:  ")),
                "English": int(input("English:  "))
            }
            sm.add_student(Student(sid, name, age, grade, gender, email, phone, marks))

        elif ch == "4":
            sm.update_student(input("Student ID:  "))
        
        elif ch == "5":
            sm.delete_student(input("Student ID:  "))

        elif ch == "0":
            print("System closed successfully")
            break

        else:
            print("Invalid selection")

if __name__== "__main__":
    main()