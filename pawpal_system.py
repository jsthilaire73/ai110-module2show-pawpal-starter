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
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Adds a task to this pet's schedule."""
        pass


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Registers a new pet under this owner."""
        pass

    def get_all_tasks(self) -> List[Task]:
        """Retrieves all tasks across all owned pets."""
        pass


class Scheduler:
    """Handles sorting, filtering, and conflict detection across tasks."""
    
    @staticmethod
    def sort_by_time(tasks: List[Task]) -> List[Task]:
        """Sorts a list of tasks chronologically."""
        pass

    @staticmethod
    def filter_tasks(tasks: List[Task], status: bool = None, pet_name: str = None) -> List[Task]:
        """Filters tasks by completion status or pet name."""
        pass

    @staticmethod
    def detect_conflicts(tasks: List[Task]) -> List[str]:
        """Finds if any tasks are scheduled at the exact same time."""
        pass