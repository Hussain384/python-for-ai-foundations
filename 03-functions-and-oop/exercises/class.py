# Practice: create a class that stores state and protects its data.


class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")
        self.scores.append(score)

    def average_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def __repr__(self):
        return f"Student(name={self.name!r}, scores={self.scores!r})"

    def passed(self):
        """Return True if the average score is at least 60."""
        return self.average_score() >= 60


student = Student("Ada")
student.add_score(90)
student.add_score(84)
print(student)
print("Average:", student.average_score())
print("Passed:", student.passed())

student2 = Student("Grace")
student2.add_score(55)
print(student2)
print("Average:", student2.average_score())
print("Passed:", student2.passed())
