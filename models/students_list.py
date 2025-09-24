from models.student import Student
from typing import List, Optional

class StudentsList:
    def __init__(self, capacity: int = 10):
        self._students: List[Student] = []
        self._capacity = capacity

    def add(self, student: Student) -> bool:
        try:
            if not isinstance(student, Student):
                raise TypeError("Only Student objects can be added.")
            if len(self._students) >= self._capacity:
                raise OverflowError("Student list capacity reached.")
            self._students.append(student)
            return True
        except Exception as e:
            print(f"Error adding student: {e}")
            return False

    def remove(self, seat_no: str) -> bool:
        try:
            for s in self._students:
                if s.seat_no.strip().lower() == seat_no.strip().lower():
                    self._students.remove(s)
                    return True
            raise ValueError(f"Student with seat_no {seat_no} not found.")
        except Exception as e:
            print(f"Error removing student: {e}")
            return False

    def search(self, key: str) -> Optional[Student]:
        try:
            key = key.strip().lower()
            student = next(
                (
                    s for s in self._students
                    if s.name.lower() == key or s.seat_no.strip().lower() == key
                ),
                None
            )
            if student is None:
                raise LookupError(f"No student found for key '{key}'.")
            return student
        except Exception as e:
            print(f"Error searching student: {e}")
            return None

    def sort_by_name(self):
        try:
            self._students.sort(key=lambda s: s.name.lower())
        except Exception as e:
            print(f"Error sorting by name: {e}")

    def sort_by_seat(self):
        try:
            self._students.sort(key=lambda s: s.seat_no.lower())
        except Exception as e:
            print(f"Error sorting by seat: {e}")

    def __iter__(self):
        return iter(self._students)

    def __str__(self):
        return "\n".join(str(s) for s in self._students)
