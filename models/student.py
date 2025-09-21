from models.courses_list import CoursesList
from models.course import Course

class Student:
    def __init__(self, name: str, seat_no: str):
        self._name = name
        self._seat_no = seat_no
        self._courses = CoursesList()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def seat_no(self):
        return self._seat_no

    @seat_no.setter
    def seat_no(self, value):
        self._seat_no = value

    @property
    def courses(self):
        return self._courses

    def enroll(self, course: Course) -> bool:
        return self._courses.add(course)

    def drop(self, code: str) -> bool:
        return self._courses.remove(code)

    def __repr__(self):
        return f"Student({self.seat_no}, {self.name})"

    def __str__(self):
        return f"{self.seat_no} - {self.name}, Courses: [{self.courses}]"

    def __eq__(self, other):
        return isinstance(other, Student) and self.seat_no == other.seat_no

    def __lt__(self, other):
        return self.seat_no < other.seat_no