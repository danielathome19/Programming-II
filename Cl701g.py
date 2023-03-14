class Person:
  def __init__(self, fn, ln):
    self._first = fn
    self._last = ln

  def getName(self):
    return self._first + " " + self._last


class Student(Person):
  def __init__(self, fn, ln, gpa):
    super().__init__(fn, ln)
    # or Person.__init__(fn, ln)
    self.gpa = gpa


class Teacher(Person):
  def __init__(self, fn, ln, numStu):
    super().__init__(fn, ln)
    self.numStudents = numStu


class Admin(Person):
  def __init__(self, fn, ln, favW):
    super().__init__(fn, ln)
    self.favWord = favW