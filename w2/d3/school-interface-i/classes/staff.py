from classes.person import Person
import csv


class Staff(Person):
    def __init__(self, employee_id, **kwargs):
        super().__init__(**kwargs)
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        with open("data/staff.csv") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")

            staff_list = []
            for row in csv_reader:

                new_person = cls(**row)
                staff_list.append(new_person)
            return staff_list


# Ed = Staff(
#     {
#         "name": "Ed",
#         "age": 30,
#         "password": "password",
#         "role": "Teacher",
#         "employee_id": 1313,
#     }
# )
# print(Ed)
