#Create a Python script. 
#Implement all tasks using classes, objects, and methods.
#Include comments to explain your code.
#Submit to GitHub repository with completed work. 
# Part 1: Class Definition

#Create a class called 'Student' with the following attributes:
#name (String)
#email (String)
#grades (list of integers)

#Methods: 
#add_grade(grade): Adds a grade to the student's grades list.
#average_grade(): Returns the average of the student's grades.
#display_info(): Prints the student's name, email, and average grade.

class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        avg_grade = self.average_grade()
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Average Grade: {avg_grade:.2f}")

# Part 2: Working with Objects
student1 = Student("Alice", "alice@example.com")  # student1 = Alice
student2 = Student("Bob", "bob@example.com")      # student2 = Bob
student3 = Student("Charlie", "charlie@example.com")  # student3 = Charlie

student1.add_grade(90)
student1.add_grade(85)
student2.add_grade(78)
student2.add_grade(88)
student3.add_grade(92)
student3.add_grade(81)

student1.display_info()
student2.display_info()
student3.display_info()

#Part 3
#Create a dictionary called student_dict that maps each student’s email to their 
# corresponding Student object.
#Write a function get_student_by_email(email) that retrieves a student object from the 
# dictionary safely using .get().
#Create a set of all unique grades across all students and print it.

# Function to save students to a file
def save_students(students, filename):
    with open(filename, 'w') as file:
        for student in students:
            grades_str = ','.join(map(str, student.grades))
            file.write(f"{student.name},{student.email},{grades_str}\n")

def load_students(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            name, email, grades_str = line.strip().split(',', 2)
            grades = list(map(int, grades_str.split(','))) if grades_str else []
            student = Student(name, email)
            for grade in grades:
                student.add_grade(grade)
            students.append(student)
    return students

students = [student1, student2, student3]
save_students(students, 'students.txt')
loaded_students = load_students('students.txt')
for s in loaded_students:
    s.display_info()

# Part 4: Inheritance Example
#Part 4: Tuple Practice
#Add a method to the Student class called grades_tuple(self) that returns the grades as a tuple.
#Demonstrate that tuples are immutable by trying to change a value (catch the exception with 
# try/except and print a message).

# Example: Create a subclass for GraduateStudent
class GraduateStudent(Student):
    def __init__(self, name, email, thesis_title):
        super().__init__(name, email)
        self.thesis_title = thesis_title

    def display_info(self):
        super().display_info()
        print(f"Thesis Title: {self.thesis_title}")

grad_student = GraduateStudent("Dana", "dana@example.com", "AI in Education")
grad_student.add_grade(95)
grad_student.add_grade(88)
grad_student.display_info()

#Part 5: List Operations
#Remove the last grade from each student’s grades list using .pop().
#Access and print the first and last grade for each student.
#Print the number of grades each student has using len().

# Remove the last grade from each student's grades list
student1.grades.pop()
student2.grades.pop()
student3.grades.pop()

# Access and print the first and last grade for each student
print(f"{student1.name} - First grade: {student1.grades[0]}, Last grade: {student1.grades[-1]}")
print(f"{student2.name} - First grade: {student2.grades[0]}, Last grade: {student2.grades[-1]}")
print(f"{student3.name} - First grade: {student3.grades[0]}, Last grade: {student3.grades[-1]}")

# Print the number of grades each student has
print(f"{student1.name} has {len(student1.grades)} grades.")
print(f"{student2.name} has {len(student2.grades)} grades.")
print(f"{student3.name} has {len(student3.grades)} grades.")
