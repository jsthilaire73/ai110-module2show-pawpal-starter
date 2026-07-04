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
    
    # 3. Add tasks with explicit Time, Duration (mins), and Priority (1=High, 3=Low)
    task1 = Task(description="Evening Feeding", time="18:00", frequency="Daily", duration=15, priority=1)
    task2 = Task(description="Morning Walk", time="08:00", frequency="Daily", duration=30, priority=2)
    task3 = Task(description="Emergency Meds", time="14:00", frequency="Once", duration=10, priority=1)
    task4 = Task(description="Deep Cat Grooming", time="14:00", frequency="Weekly", duration=45, priority=3)
    
    dog.add_task(task1)
    dog.add_task(task2)
    dog.add_task(task3)
    cat.add_task(task4)
    
    all_tasks = owner.get_all_tasks()
    
    # 4. Conflict Detection
    conflicts = Scheduler.detect_conflicts(all_tasks)
    if conflicts:
        print("\n⚠️  SYSTEM WARNINGS:")
        for conflict in conflicts:
            print(f"  {conflict}")
            
    # 5. Advanced Scheduling Logic: Apply a 60-Minute Daily Time Budget Constraint
    TIME_BUDGET = 60
    scheduled_tasks = Scheduler.filter_by_time_budget(all_tasks, available_minutes=TIME_BUDGET)
    
    # 6. Print Sorted Schedule Output
    print(f"\n📅 Today's Optimized Schedule for {owner.name}'s Pets (Budget: {TIME_BUDGET} mins):")
    for task in scheduled_tasks:
        status = "✅" if task.is_completed else "⏳"
        print(f"  [{task.time}] P{task.priority} ({task.duration}m) — {task.description} [{status}]")
        
    # 7. Agent Mode Execution Explanation
    print("\n🤖 Scheduler Engine Reasoning:")
    explanation = Scheduler.generate_schedule_reasoning(scheduled_tasks, len(all_tasks), TIME_BUDGET)
    print(f"  {explanation}")

    # 8. Data Persistence Layer Verification
    print("\n💾 Testing Data Persistence...")
    owner.save_to_json("pawpal_data.json")
    print("  State safely written to pawpal_data.json!")

if __name__ == "__main__":
    run_demo()