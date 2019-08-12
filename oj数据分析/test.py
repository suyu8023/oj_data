import re

def write_grade(grade):
    with open('grade.txt', 'r+') as f:
        l = f.read()
        print(l)
        f.write(grade)
    f.close()
    with open('grade.txt', 'r+') as f:
        l = f.read()
        print(l)
        f.write(grade)
    f.close()

write_grade(grade='5')
