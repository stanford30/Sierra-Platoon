from classes.person import Person
import csv


class Student(Person):
    def __init__(self, school_id, **kwargs):
        super().__init__(**kwargs)
        self.school_id = school_id

    @classmethod
    def all_students(cls):
        with open("data/students.csv") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")

            student_list = []
            for row in csv_reader:

                new_person = cls(**row)
                student_list.append(new_person)
            return student_list


print(Student.all_students())

# stanford = Student("Stanley", 21, "TA", "12341", 1111)
# print(type(stanford.password))

# student_info = {
#     "name": "Diana",
#     "password": "password",
#     "school_id": 12345,
#     "age": 17,
#     "role": "Student",
# }
# Diana = Student(**student_info)
# print(Diana)
