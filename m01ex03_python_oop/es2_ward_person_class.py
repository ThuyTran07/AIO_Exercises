class Person():
    def __init__(self, name:str, yob:int):
        self.name = name
        self.yob = yob

class Student(Person):
    def __init__(self, name, yob, grade:str):
        super().__init__(name, yob)
        self.grade = grade
    
    def describle(self):
        print (f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject:str):
        super().__init__(name, yob)
        self.subject = subject
    
    def describle(self):
        print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Grade: {self.subject}")

class Doctor(Person):
    def __init__(self, name, yob, specialist:str):
        super().__init__(name, yob)
        self.specialist = specialist
    
    def describle(self):
        print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Grade: {self.specialist}")

class Ward():
    def __init__(self, name):
        self.name = name
        self.list_of_person = []

    def add_person(self, person):
        new_person = {"class": person.__class__.__name__, **vars(person)}
        self.list_of_person.append(new_person)
    
    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.list_of_person:
            for key, value in person.items():
                print(f"{key.title()}: {value}" if key is not list(person.keys())[0] else value, end=" - " if key is not list(person.keys())[-1] else "")
            print()

    def count(self, occupation):
        count = 0
        for person in self.list_of_person:
            if person['class'] == occupation.title():
                count += 1
        print(f"Numer of {occupation.lower()}s: {count}")
        return count
    
    def sort_age(self):
        self.list_of_person = sorted(self.list_of_person, key=lambda x: x['yob'], reverse=True)
        return self.list_of_person
    
    def compute_average_yob(self, occupation):
        count = 0
        sum_yob = 0
        for person in self.list_of_person:
            if person["class"] == occupation.title():
                count += 1
                sum_yob += person["yob"]
        average_yob = sum_yob / count
        print(f"Average year of birth of {occupation.lower()}s: {average_yob:.0f}", )
        return average_yob




#test
# es2a)
student1 = Student(name="Student A", yob=2010, grade="7")
teacher1 = Teacher(name="Teacher A", yob=1969, subject="Math")
doctor1 = Doctor(name="Doctor A", yob=1945, specialist="Endocrinologists")

#es2b)
teacher2 = Teacher(name="Teacher B", yob=1995, subject="History")
doctor2 = Doctor(name="Doctor B", yob=1975, specialist="Cardiologists")

ward9 = Ward("Ward 9")
ward9.add_person(student1)
ward9.add_person(teacher1)
ward9.add_person(teacher2)
ward9.add_person(doctor1)
ward9.add_person(doctor2)

#es2d)
ward9.sort_age()
ward9.describe()

#es2c)
ward9.count("doctor")

#es2e)
ward9.compute_average_yob("Teacher")


