# Practice: use a dataclass for a small data-focused object.

from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    priority: int = 1
    completed: bool = False
    labels: list[str] = field(default_factory=list)
    description: str = ""

    def complete(self):
        self.completed = True

    def add_label(self, label):
        self.labels.append(label)

    def is_high_priority(self):
        """Return True if the priority is 3 or more."""
        return self.priority >= 3


first_task = Task("Study dataclasses", priority=2)
first_task.add_label("python")
first_task.complete()

second_task = Task("Practice composition")
second_task.add_label("oop")

print("First task:", first_task)
print("Completed:", first_task.completed)
print("Second task:", second_task)
print("Labels are independent:", first_task.labels != second_task.labels)
print("Same task values:", first_task == Task(
    "Study dataclasses", 2, True, ["python"]
))

third_task = Task("High priority task", priority=3)
print("Is high priority:", third_task.is_high_priority())


print("Description:", first_task.description)   
print("Description:", second_task.description)   
print("Description:", third_task.description)   

first_task.description = "Learn how to use dataclasses in Python."
print("Updated description:", first_task.description)
second_task.description = "Practice using composition in OOP."
print("Updated description:", second_task.description)
third_task.description = "This task is of high priority."
print("Updated description:", third_task.description)
