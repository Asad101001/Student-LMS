from Student import Student
from typing import List, Optional
class StudentList:
    def __init__(self, capacity: int = 10):
        self._students: List[Student] = []
        self._capacity = capacity

    def add(self, student: Student) -> bool:
        if len(self._students) < self._capacity:
            self._students.append(student)
            return True
        return False

    def remove(self, seat_no: str) -> bool:
        for s in self._students:
            if s.seat_no == seat_no:
                self._students.remove(s)
                return True
        return False

    def search(self, key: str) -> Optional[Student]:
        return next((s for s in self._students if s.name.lower() == key.lower() or s.seat_no == key), None)

    def sort_by_name(self):
        self._students.sort(key=lambda s: s.name.lower())

    def sort_by_seat(self):
        self._students.sort()

    def __iter__(self):
        return iter(self._students)

    def __str__(self):
        return "\n".join(str(s) for s in self._students)
