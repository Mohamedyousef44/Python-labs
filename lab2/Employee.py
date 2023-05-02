
from Model import Database
import config

db = Database(config.host, config.user, config.password, config.database)
db.connect()


class Employee:

    emplist = []

    def __init__(self, id, fname, lname, salary, age, dept):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.age = age
        self.dept = dept
        self.emplist.append(self)
        db.insert(
            "INSERT INTO employee (id ,fname,lname,age,salary,dept) VALUES {}".format((id, fname, lname, age, salary, dept)))

    def transfer(self, newdept):
        self.dept = newdept
        db.update("UPDATE employee SET dept='{}' WHERE id={}".format(
            self.dept, self.id))

    def show(self):
        print({'name': self.fname + ' ' + self.lname, 'age': self.age,
              'department': self.dept, 'salary': self.salary})

    @ classmethod
    def fire(cls, i):
        try:
            cls.emplist.remove(cls.specific_obj(cls.emplist, i))
            db.delete("employee", "id={}".format(i))

        except Exception as e:
            print(e)

    @ classmethod
    def list_employees(cls):

        for emp in cls.emplist:
            emp.show()

    @staticmethod
    def specific_obj(li, i):
        obj = list(filter(lambda x: x.id == i, li))
        return obj[0]


class Manager(Employee):

    def __init__(self, id, fname, lname, salary, age, dept, manageddept):
        super().__init__(id, fname, lname, salary, age, dept)
        self.manageddept = manageddept

    def show(self):
        print({'name': self.fname + ' ' + self.lname, 'age': self.age,
              'department': self.dept, 'salary': 'confidential', 'managed_department': self.manageddept})


flag = True

while (flag):

    emp: any

    print("""
        hi sir, please follow instructions below:
            a: add new employee
            r: remove user
            e: edit department
            q: quit
        press for letter to do what you want

        """)
    action = input()

    match action:
        case "a":
            print('please enter emp id')
            id = int(input())
            print('please enter emp fname')
            fname = input()
            print('please enter emp lname')
            lname = input()
            print('please enter emp salary')
            salary = int(input())
            print('please enter emp age')
            age = int(input())
            print('please enter emp dept')
            dept = input()
            emp = Employee(id, fname, lname, salary, age, dept)
        case "r":
            print('please enter emp id')
            id = int(input())
            Employee.fire(id)
        case "e":
            print("please enter new department")
            newdept = input()
            Employee.transfer(emp, newdept)
        case "q":
            flag = False

        case _:
            print("Invalid input data!")


Employee.list_employees()

emp1 = Employee(1, 'mohamed', 'yossef', 1500, 26, 'os')

emp1.list_employees()
