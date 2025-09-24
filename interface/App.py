from models import *

class App:

    def __init__(self):
        pass

    @staticmethod
    def run():
        try:

            s1 = Student("Asad", "087")
            s2 = Student("Hasaan", "090")
            s3 = Student("Abdullah","010")

            c1 = Course("OOPs", "CS352")
            c2 = Course("Discrete Structures", "CS358")
            c3 = Course("DLD", "CS353")

            s1.enroll(c1)
            s1.enroll(c2)
            s2.enroll(c1)
            s2.enroll(c3)
            s3.enroll(c1)

            sl = StudentsList(capacity=5)
            sl.add(s1)
            sl.add(s2)
            sl.add(s3)

            try:
                sl.add(s1)
            # Duplicate entry handling
            except ValueError as e:
                print("Duplicate Error:", e)

            print("All Students:")
            print(sl)

            try:
                print("\nSearch 010 ->", sl.search("010"))
            # Invalid searching by seat number handling
            except ValueError as e:
                print("Search Error:", e)

            # Searching by student name
            try:
                print("Search by Name 'Hasaan' ->", sl.search("Hasaan"))
            except ValueError as e:
                print("Search Error:", e)

            # Sorting the list of students name
            try:
                print("\nSorted by Name:")
                sl.sort_by_name()
                print(sl)
            # Invalid sorting handling
            except Exception as e:
                print("Unexpected sorting error:", e)

        except Exception as e:
            print("Unexpected application error:", e)
