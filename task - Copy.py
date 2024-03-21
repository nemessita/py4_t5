# Maliyyə Sənayesi:
# Tapşırıq: Büdcə aləti yaradın
# Təsvir: Tələbələr aylıq xərclər və gəlirlər üçün daxil olan Python proqramı yaradacaqlar. 
# Funksiya ümumi xərcləri, ümumi gəliri almalı və ayın qalan büdcəsini hesablamalıdır.



def my_def(income, expenses):
    total = income - expenses
    return total

students = ["student1", "student2", "student3", "student4", "student5"]

i = int(input("Select a student to add (1-5): "))
if 1 <= i <= len(students):
    print(students[i - 1])
else:
    print("Invalid input. Please select a number between 1 and 5.")

income = int(input("Add income: "))
expenses = int(input("Add expenses: "))

total = my_def(income, expenses)
print("Total:", total)


