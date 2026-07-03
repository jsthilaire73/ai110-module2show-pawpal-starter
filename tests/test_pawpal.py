from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_completion():
    """Verify that calling mark_complete() actually changes the task's status."""
    # Arrange: Create a task that starts as incomplete
    task = Task(description="Morning Walk", time="08:00", frequency="Daily")
    assert not task.is_completed

    # Act: Mark it complete
    task.mark_complete()

    # Assert: Verify state successfully changed
    assert task.is_completed


def test_task_addition():
    """Verify that adding a task to a Pet increases that pet's task count."""
    # Arrange: Create a pet and a task
    pet = Pet(name="Biscuit", species="Dog")
    task = Task(description="Afternoon Meds", time="14:00", frequency="Once")
    assert len(pet.tasks) == 0

    # Act: Add the task to the pet
    pet.add_task(task)

    # Assert: Verify the task list now contains our task
    assert len(pet.tasks) == 1
    assert pet.tasks[0] == task