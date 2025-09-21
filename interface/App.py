from models import *

class App:
 
 def __init__(self):
  pass

 @staticmethod
 def run():
    s1 = Student("Asad", "087")
    s2 = Student("Hasaan", "090")
    s3 = Student("Abdullah","010")

    c1 = Course("OOPs", "CS352")
    c2 = Course("Discrete Structures", "CS351")
    c3 = Course("DLD", "CS350")

    s1.enroll(c1)
    s1.enroll(c2)
    s2.enroll(c1)
    s2.enroll(c3)
    s3.enroll(c1)

    sl = StudentsList(capacity=5)
    sl.add(s1)
    sl.add(s2)
    sl.add(s3)

    print("All Students:")
    print(sl)

    print("\nSearch S088 ->", sl.search("S088"))
    print("Search by Name 'Hasaan' ->", sl.search("Hasaan"))

    print("\nSorted by Name:")
    sl.sort_by_name()
    print(sl)

