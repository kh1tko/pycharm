# 1) Створіть клас Студент, в ньому обявіть дві змінні імя де збережети імя студента, та список його оцінок.
# створіть два метода в цьому класі, перший метод який буде вітатись і при вітання використовувати імя студента.
# другий метод буде виводити оцінки. Методи виводять результат через прінти.
#
# Створіть два екземпляра цього класу, в другому екземплярі змніть імя на своє(не міняючи нічого в класі).
# Вивідіть дві функції цих екземплярів, що б кожен студент привітався та сказав свої оцінки.


class Student:
    name = 'Arestovych'
    grades = [12, 13, 5, 76, 87, 43, 34]

    def greets_by_name(self):
        print(f'Привіт! Я студент {self.name}')

    def student_grades(self):
        print(f'Мої оцінки {self.grades}')


class StudentTwo:
    name = 'Aртем'
    grades = [12, 13, 5, 76, 87, 43, 34]

    def greets_by_name(self):
        print(f'Привіт! Я студент {self.name}')

    def student_grades(self):
        print(f'Мої оцінки {self.grades}')


obj_1 = Student()
obj_1.greets_by_name()
obj_1.student_grades()
print()
obj_2 = StudentTwo()
obj_2.greets_by_name()
obj_2.student_grades()
