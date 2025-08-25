#Write a function student_profile(**kwargs) that prints the key-value pairs passed (e.g., name, age, grade). Call it with at least three named arguments.
def student_profile(**kwargs) : 
    print(kwargs)
# s1 = {'name' : "ram", 'age' : 10, 'grade' : 5}
# student_profile(**s1)
student_profile(name = "ram", age = 15, grade = 10)