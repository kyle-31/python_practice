class Student:
    def __init__(self, name , studen_id):
        self.name = name
        self.studen_id = studen_id
        self.grades = {"國文":0 , "數學":0 , "英文":0}

    def set_grade(self, course , grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"學生{self.name} (學號{self.studen_id})的成績為:")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}")


chen = Student("小陳" , "1005336")
# zeng = Student("小曾" , "6566346")

# print(chen.name)
# zeng.set_grade("數學" , 95)
# print(zeng.grades)

chen.set_grade("國文", 95)
chen.set_grade("數學", 69)

chen.print_grades()
