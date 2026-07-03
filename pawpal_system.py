from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    description: str
    time: str          # Format: "HH:MM"
    frequency: str     # e.g., "Once", "Daily", "Weekly"
    is_completed: bool = False

    def mark_complete(self) -> None:
        """Marks the task as completed."""
        self.is_completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Adds a task to this pet's schedule."""
        self.tasks.append(task)

@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Registers a new pet under this owner."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Retrieves all tasks across all owned pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

class Scheduler:
    """Handles sorting, filtering, and conflict detection across tasks."""
    
    @staticmethod
    def sort_by_time(tasks: List[Task]) -> List[Task]:
        """Sorts a list of tasks chronologically by their HH:MM string format."""
        return sorted(tasks, key=lambda task: task.time)

    @staticmethod
    def filter_tasks(tasks: List[Task], status: bool = None, pet_name: str = None) -> List[Task]:
        """Filters tasks by completion status."""
        filtered = tasks
        if status is not None:
            filtered = [t for t in filtered if t.is_completed == status]
        return filtered

    @staticmethod
    def detect_conflicts(tasks: List[Task]) -> List[str]:
        """Finds if any tasks are scheduled at the exact same time."""
        conflicts = []
        times_seen = {}
        
        for task in tasks:
            if task.time in times_seen:
                conflicts.append(f"Conflict detected: Multiple tasks scheduled at {task.time}!")
            else:
                times_seen[task.time] = True
                
        return conflicts