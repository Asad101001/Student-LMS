from models.course import Course
from typing import *

class CoursesList:
    def __init__(self, size: int = 10):
        self._courses: List[Course] = []
        self._size = size

    def add(self, course: Course) -> bool:
        if len(self._courses) < self._size:
            self._courses.append(course)
            return True
        return False

    def remove(self, code: str) -> bool:
        for c in self._courses:
            if c.code == code:
                self._courses.remove(c)
                return True
        return False

    def search(self, key: str) -> Optional[Course]:
        return next((c for c in self._courses if c.name.lower() == key.lower() or c.code == key), None)

    def sort_by_code(self):
        self._courses.sort()

    def sort_by_name(self):
        self._courses.sort(key=lambda c: c.name.lower())

    def __iter__(self):
        return iter(self._courses)

    def __add__(self, other):
        merged = CoursesList(self._size + other._size)
        for c in self._courses + other._courses:
            merged.add(c)
        return merged

    def __str__(self):
        return ", ".join(str(c) for c in self._courses)