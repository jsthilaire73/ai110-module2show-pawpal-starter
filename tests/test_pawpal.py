import os
from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_completion():
    """Verify that calling mark_complete() actually changes the task's status."""
    task = Task(description="Morning Walk", time="08:00", frequency="Daily", duration=30, priority=1)
    assert not task.is_completed
    task.mark_complete()
    assert task.is_completed

def test_task_addition():
    """Verify that adding a task to a Pet increases that pet's task count."""
    pet = Pet(name="Biscuit", species="Dog")
    task = Task(description="Afternoon Meds", time="14:00", frequency="Once", duration=15, priority=1)
    assert len(pet.tasks) == 0
    pet.add_task(task)
    assert len(pet.tasks) == 1
    assert pet.tasks[0] == task

def test_priority_and_time_sorting():
    """Verify tasks are sorted by priority first, then chronologically by time."""
    t1 = Task("Low Priority Morning Walk", "08:00", "Daily", 30, priority=3)
    t2 = Task("High Priority Evening Feed", "18:00", "Daily", 15, priority=1)
    t3 = Task("High Priority Morning Meds", "07:00", "Once", 10, priority=1)
    
    unsorted_list = [t1, t2, t3]
    sorted_list = Scheduler.sort_by_priority_and_time(unsorted_list)
    
    assert sorted_list[0] == t3  # Priority 1, 07:00
    assert sorted_list[1] == t2  # Priority 1, 18:00
    assert sorted_list[2] == t1  # Priority 3, 08:00

def test_time_budget_filter():
    """Verify Scheduler skips lower priority tasks when available time runs out."""
    t1 = Task("Important Vet Visit", "10:00", "Once", 45, priority=1)
    t2 = Task("Grooming Brush", "11:00", "Daily", 30, priority=2)
    t3 = Task("Quick Walk", "12:00", "Daily", 15, priority=3)
    
    all_tasks = [t1, t2, t3]
    scheduled = Scheduler.filter_by_time_budget(all_tasks, available_minutes=60)
    
    assert t1 in scheduled
    assert t3 in scheduled
    assert t2 not in scheduled

def test_json_persistence():
    """Verify saving and loading state from disk via JSON serialization works."""
    temp_filename = "test_temp_pawpal_data.json"
    if os.path.exists(temp_filename):
        os.remove(temp_filename)
        
    try:
        owner = Owner(name="Jean")
        pet = Pet(name="Luna", species="Cat")
        task = Task("Grooming", "14:00", "Weekly", 45, priority=2)
        
        pet.add_task(task)
        owner.add_pet(pet)
        owner.save_to_json(temp_filename)
        
        assert os.path.exists(temp_filename)
        loaded_owner = Owner.load_from_json(temp_filename)
        
        assert loaded_owner.name == "Jean"
        assert len(loaded_owner.pets) == 1
        assert loaded_owner.pets[0].tasks[0].description == "Grooming"
        assert loaded_owner.pets[0].tasks[0].duration == 45
        
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)