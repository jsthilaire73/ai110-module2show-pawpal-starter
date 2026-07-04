import json
from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class Task:
    description: str
    time: str          # Format: "HH:MM"
    frequency: str     # e.g., "Once", "Daily", "Weekly"
    duration: int      # In minutes (e.g., 30, 45)
    priority: int      # 1 = High, 2 = Medium, 3 = Low
    is_completed: bool = False

    def mark_complete(self) -> None:
        """Marks the task as completed."""
        self.is_completed = True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "description": self.description,
            "time": self.time,
            "frequency": self.frequency,
            "duration": self.duration,
            "priority": self.priority,
            "is_completed": self.is_completed
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        return cls(
            description=data["description"],
            time=data["time"],
            frequency=data["frequency"],
            duration=data["duration"],
            priority=data["priority"],
            is_completed=data["is_completed"]
        )


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Adds a task to this pet's schedule."""
        self.tasks.append(task)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "species": self.species,
            "tasks": [t.to_dict() for t in self.tasks]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Pet':
        pet = cls(name=data["name"], species=data["species"])
        pet.tasks = [Task.from_dict(t) for t in data["tasks"]]
        return pet


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

    def save_to_json(self, filename: str = "pawpal_data.json") -> None:
        """Persists all owner, pet, and task data to a JSON file."""
        data = {
            "name": self.name,
            "pets": [p.to_dict() for p in self.pets]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_json(cls, filename: str = "pawpal_data.json") -> 'Owner':
        """Loads data from a JSON file to recreate the state."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            owner = cls(name=data["name"])
            owner.pets = [Pet.from_dict(p) for p in data["pets"]]
            return owner
        except FileNotFoundError:
            return cls(name="Default Owner")


class Scheduler:
    """Handles sorting, filtering, and constraint enforcement across tasks."""
    
    @staticmethod
    def sort_by_priority_and_time(tasks: List[Task]) -> List[Task]:
        """Sorts tasks by Priority first (1=Highest), then chronologically by Time."""
        return sorted(tasks, key=lambda x: (x.priority, x.time))

    @staticmethod
    def filter_by_time_budget(tasks: List[Task], available_minutes: int) -> List[Task]:
        """Advanced Scheduling Logic: Drops low priority tasks if time budget runs out."""
        sorted_tasks = Scheduler.sort_by_priority_and_time(tasks)
        scheduled_tasks = []
        total_timeUsed = 0
        
        for task in sorted_tasks:
            if total_timeUsed + task.duration <= available_minutes:
                scheduled_tasks.append(task)
                total_timeUsed += task.duration
        return scheduled_tasks

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

    @staticmethod
    def generate_schedule_reasoning(scheduled: List[Task], total_tasks: int, budget: int) -> str:
        """Agent Mode Feature: Generates natural language reasoning explaining the plan."""
        skipped_count = total_tasks - len(scheduled)
        time_spent = sum(t.duration for t in scheduled)
        
        reasoning = f"Analysis complete. Scheduled {len(scheduled)} out of {total_tasks} tasks within a {budget}-minute limit.\n"
        reasoning += f"Reasoning: High-priority (Priority 1) items were prioritized chronologically. "
        if skipped_count > 0:
            reasoning += f"Dropped {skipped_count} lower-priority items to prevent exceeding your time budget (Used {time_spent}/{budget} mins)."
        else:
            reasoning += "All tasks fit safely inside your daily available timeframe."
        return reasoning