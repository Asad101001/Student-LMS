class Course:
    def __init__(self, name: str, code: str):
        self._name = name
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    def __repr__(self):
        return f"Course({self.code}, {self.name})"

    def __str__(self):
        return f"{self.code}: {self.name}"

    def __eq__(self, other):
        return isinstance(other, Course) and self.code == other.code

    def __lt__(self, other):
        return self.code < other.code