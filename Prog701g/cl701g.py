class Person:
    def __init__(self, fn, ln):
        self._first = fn
        self._last = ln

    def get_name(self):
        return self._first + " " + self._last


class Student(Person):
    def __init__(self, fn, ln, gpa):
        super().__init__(fn, ln)  # or Person.__init__(fn, ln)
        self.gpa = gpa


class Teacher(Person):
    def __init__(self, fn, ln, num_stu):
        super().__init__(fn, ln)
        self.num_stu = num_stu


class Admin(Person):
    def __init__(self, fn, ln, fav_word):
        super().__init__(fn, ln)
        self.fav_word = fav_word
