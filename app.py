import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

# Set page configuration
st.set_page_config(page_title="PawPal+ Care Scheduler", page_icon="🐾", layout="wide")

st.title("🐾 PawPal+ Care Task Scheduler")
st.caption("Module 2 Project — Advanced Optimized Scheduling Engine with Task Editing")

# Initialize session state for persistent data handling across UI reloads
if "owner" not in st.session_state:
    # Try loading from JSON disk persistence layer first
    st.session_state.owner = Owner.load_from_json()
    if not st.session_state.owner.pets:
        # Seed default data if completely empty
        jean = Owner(name="Jean")
        biscuit = Pet(name="Biscuit", species="Dog")
        luna = Pet(name="Luna", species="Cat")
        
        # Seed Biscuit's tasks
        biscuit.add_task(Task("Evening Feeding", "18:00", "Daily", 15, 1))
        biscuit.add_task(Task("Morning Walk", "08:00", "Daily", 30, 2))
        biscuit.add_task(Task("Emergency Meds", "14:00", "Once", 10, 1))
        
        # Seed Luna's tasks
        luna.add_task(Task("Deep Cat Grooming", "14:00", "Weekly", 45, 3))
        
        jean.add_pet(biscuit)
        jean.add_pet(luna)
        st.session_state.owner = jean

owner = st.session_state.owner

# Sidebar: Profile Overview & Persistence Control
with st.sidebar:
    st.header("👤 Owner Profile")
    owner.name = st.text_input("Owner Name", value=owner.name)
    
    st.markdown("---")
    st.header("💾 Data Management")
    if st.button("Save Current State to Disk", use_container_width=True):
        owner.save_to_json()
        st.success("Successfully saved to pawpal_data.json!")
        
    st.markdown("---")
    st.header("🐾 Add a New Pet")
    new_pet_name = st.text_input("Pet Name")
    new_pet_species = st.selectbox("Species", ["Dog", "Cat", "Bird", "Other"])
    if st.button("Register Pet", use_container_width=True):
        if new_pet_name:
            owner.add_pet(Pet(name=new_pet_name, species=new_pet_species))
            st.success(f"Registered {new_pet_name}!")
            st.rerun()

# Main Interface Grid
col1, col2 = st.columns([1, 1])

with col1:
    # Tab layout to separate Adding new tasks vs. Editing existing tasks
    task_tab1, task_tab2 = st.tabs(["➕ Add Task", "✏️ Edit / Delete Task"])
    
    with task_tab1:
        st.subheader("Add Pet Care Task")
        if not owner.pets:
            st.warning("Please add a pet in the sidebar first!")
        else:
            target_pet_name = st.selectbox("Select Pet", [p.name for p in owner.pets], key="add_target_pet")
            task_desc = st.text_input("Task Description (e.g., Bathing, Feeding)", key="add_task_desc")
            
            c1, c2 = st.columns(2)
            with c1:
                task_time = st.text_input("Due Time (HH:MM format)", value="08:00", key="add_task_time")
            with c2:
                task_freq = st.selectbox("Frequency", ["Daily", "Once", "Weekly"], key="add_task_freq")
                
            c3, c4 = st.columns(2)
            with c3:
                task_duration = st.slider("Duration (minutes)", min_value=5, max_value=120, value=30, step=5, key="add_task_duration")
            with c4:
                task_priority = st.selectbox("Priority Level", ["1 - High", "2 - Medium", "3 - Low"], key="add_task_priority")
                
            if st.button("Add Task to Schedule", use_container_width=True):
                if task_desc and task_time:
                    p_rank = int(task_priority.split(" ")[0])
                    new_task = Task(
                        description=task_desc,
                        time=task_time,
                        frequency=task_freq,
                        duration=task_duration,
                        priority=p_rank
                    )
                    for pet in owner.pets:
                        if pet.name == target_pet_name:
                            pet.add_task(new_task)
                            st.success(f"Added '{task_desc}' for {pet.name}!")
                            st.rerun()
                            
    with task_tab2:
        st.subheader("Modify Existing Task")
        all_tasks_flat = []
        task_options_labels = []
        
        # Build a flat list of tasks mapped to strings for the dropdown selection
        for pet in owner.pets:
            for t in pet.tasks:
                all_tasks_flat.append((pet, t))
                task_options_labels.append(f"{pet.name}: {t.description} ({t.time})")
                
        if not all_tasks_flat:
            st.info("No tasks available to edit.")
        else:
            selected_task_idx = st.selectbox("Select Task to Edit/Delete", range(len(task_options_labels)), format_func=lambda x: task_options_labels[x])
            selected_pet, selected_task = all_tasks_flat[selected_task_idx]
            
            # Populate edit fields with current task data
            edit_desc = st.text_input("Edit Description", value=selected_task.description)
            edit_time = st.text_input("Edit Due Time (HH:MM)", value=selected_task.time)
            edit_freq = st.selectbox("Edit Frequency", ["Daily", "Once", "Weekly"], index=["Daily", "Once", "Weekly"].index(selected_task.frequency))
            
            c1, c2 = st.columns(2)
            with c1:
                # The user can drag this slider to instantly modify an existing task's duration!
                edit_duration = st.slider("Edit Duration (minutes)", min_value=5, max_value=120, value=int(selected_task.duration), step=5)
            with c2:
                edit_priority = st.selectbox("Edit Priority Level", ["1 - High", "2 - Medium", "3 - Low"], index=selected_task.priority - 1)
                
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                if st.button("Apply Changes", use_container_width=True, type="primary"):
                    selected_task.description = edit_desc
                    selected_task.time = edit_time
                    selected_task.frequency = edit_freq
                    selected_task.duration = edit_duration
                    selected_task.priority = int(edit_priority.split(" ")[0])
                    st.success(f"Updated '{edit_desc}' successfully!")
                    st.rerun()
            with btn_col2:
                if st.button("🗑️ Delete Task", use_container_width=True):
                    selected_pet.tasks.remove(selected_task)
                    st.warning(f"Deleted task '{selected_task.description}'!")
                    st.rerun()

    # Section to view raw configured tasks per pet
    st.markdown("---")
    st.header("📋 Registered Tasks Registry")
    if not owner.get_all_tasks():
        st.info("No tasks created yet.")
    else:
        for pet in owner.pets:
            if pet.tasks:
                st.subheader(f"{pet.name}'s Base Tasks")
                for idx, t in enumerate(pet.tasks):
                    is_done = st.checkbox(f"[{t.time}] {t.description} ({t.duration}m) — P{t.priority}", value=t.is_completed, key=f"{pet.name}_task_{idx}")
                    if is_done != t.is_completed:
                        t.is_completed = is_done
                        st.rerun()

with col2:
    st.header("⚡ Optimized Daily Scheduler Engine")
    
    # Scheduling Constraint Slider
    time_budget = st.slider("Your Available Time Allocation (Minutes)", min_value=15, max_value=240, value=60, step=15)
    
    all_tasks = owner.get_all_tasks()
    
    # 1. Run Algorithmic Conflict Evaluation
    conflicts = Scheduler.detect_conflicts(all_tasks)
    if conflicts:
        for conflict in conflicts:
            st.error(f"⚠️ {conflict}")
            
    # 2. Run Algorithmic Time Constraint & Priority Evaluation Filter
    optimized_schedule = Scheduler.filter_by_time_budget(all_tasks, available_minutes=time_budget)
    
    # 3. Output Generation Narrative Explanation
    st.subheader("🤖 Scheduler Reasoning & Context")
    explanation = Scheduler.generate_schedule_reasoning(optimized_schedule, len(all_tasks), time_budget)
    st.info(explanation)
    
    # 4. Render Final Structured Dashboard Layout
    st.subheader("📅 Your Optimized Timeline Plan")
    if not optimized_schedule:
        st.warning("No tasks could be scheduled within this time threshold.")
    else:
        for task in optimized_schedule:
            status_badge = "✅ Done" if task.is_completed else "⏳ Pending"
            associated_pet = "Unknown"
            for p in owner.pets:
                if task in p.tasks:
                    associated_pet = p.name
                    
            st.markdown(f"""
            **🕒 {task.time}** | **{task.description}** ({associated_pet})  
            * Priority Rank: P{task.priority} | Duration: {task.duration} mins | Status: `{status_badge}`
            ---
            """)