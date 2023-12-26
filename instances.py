class Student:
    pass

class Marks:
    pass

# Creating instances of the classes
student_instance = Student()
marks_instance = Marks()

# Checking if instances are of the specified classes
is_student_instance = isinstance(student_instance, Student)
is_marks_instance = isinstance(marks_instance, Marks)

# Checking if the classes are subclasses of the built-in object class
is_student_subclass = issubclass(Student, object)
is_marks_subclass = issubclass(Marks, object)

# Displaying the results
print(f"Is student_instance an instance of Student? {is_student_instance}")
print(f"Is marks_instance an instance of Marks? {is_marks_instance}")
print(f"Is Student a subclass of object? {is_student_subclass}")
print(f"Is Marks a subclass of object? {is_marks_subclass}")
