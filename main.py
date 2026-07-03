from pawpal_system import Owner, Pet, Task, Scheduler

def run_demo():
    print("--- PawPal+ System CLI Demo ---")
    
    # 1. Create an Owner
    owner = Owner(name="Jean")
    
    # 2. Create two Pets
    dog = Pet(name="Biscuit", species="Dog")
    cat = Pet(name="Luna", species="Cat")
    
    owner.add_pet(dog)
    owner.add_pet(cat)
    
    # 3. Add at least three Tasks out of chronological order
    task1 = Task(description="Evening Feeding", time="18:00", frequency="Daily")
    task2 = Task(description="Morning Walk", time="08:00", frequency="Daily")
    task3 = Task(description="Afternoon Meds", time="14:00", frequency="Once")
    # Adding an intentional conflict at 14:00 to test our checker
    task4 = Task(description="Cat Grooming", time="14:00", frequency="Weekly")
    
    dog.add_task(task1)
    dog.add_task(task2)
    dog.add_task(task3)
    cat.add_task(task4)
    
    # 4. Gather all tasks across all pets
    all_tasks = owner.get_all_tasks()
    
    # 5. Run Scheduler Algorithms: Conflict Detection
    conflicts = Scheduler.detect_conflicts(all_tasks)
    if conflicts:
        print("\n⚠️  SYSTEM WARNINGS:")
        for conflict in conflicts:
            print(f"  {conflict}")
            
    # 6. Run Scheduler Algorithms: Sorting
    sorted_tasks = Scheduler.sort_by_time(all_tasks)
    
    # 7. Print formatted, readable schedule output
    print(f"\n📅 Today's Sorted Schedule for {owner.name}'s Pets:")
    for task in sorted_tasks:
        status = "✅" if task.is_completed else "⏳"
        print(f"  {task.time} — {task.description} ({task.frequency}) [{status}]")

if __name__ == "__main__":
    run_demo()