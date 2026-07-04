 PAWPAL+ PROJECT REFLECTION

SYSTEM DESIGN
a. Initial design
Our initial system design consists of four core classes:
Owner: Tracks the owner's name and a list of pets. It handles adding new pets and pulling all combined tasks.
Pet: Tracks individual pet profiles (name and species) and manages their specific task lists.
Task: Represents a single care activity, storing its description, time, frequency, duration, priority, and completion status.
Scheduler: The system's algorithmic brain. It handles cross-pet sorting, filtering, and conflict detection.
Core User Actions Supported:
Add a Pet: Handled by Owner.add_pet()
Schedule a Routine: Handled by Pet.add_task()
View Today's Tasks: Handled by Owner.get_all_tasks() and processed by the Scheduler.

b. Design changes
Yes, our design evolved significantly during implementation to accommodate realistic, multi-pet household requirements.
The Change: Initially, the system was designed to handle task sorting and filtering on a per-pet level. However, during implementation, we realized that an owner managing a household of multiple animals needs a unified view. Pets do not live in isolation; their care tasks compete for the exact same pool of owner time.
Why We Made It: If we kept tasks isolated to individual Pet instances, we could not easily detect conflicts. We refactored the design to aggregate all tasks up to the Owner level using owner.get_all_tasks(). This combined list is then processed by static utility methods in the Scheduler class. This decoupled architecture made both global conflict resolution and multi-pet daily scheduling extraordinarily clean and straightforward.

SCHEDULING LOGIC AND TRADEOFFS
a. Constraints and priorities
The scheduler considers three distinct types of constraints and metadata:
Priority Rank (Hard Constraint): Tasks are evaluated in order of priority level (Priority 1 = High, 3 = Low).
Chronological Due Time (Ordering Constraint): Within the same priority level, tasks are ordered chronologically by scheduled time.
Daily Time Budget (Upper Bound Constraint): The owner sets a limit on their available minutes for the day. The system processes the sorted tasks and drops lower-priority items when the running duration exceeds this budget.
We decided that Priority was the most important constraint. If an owner has limited time, critical tasks must always take precedence over optional activities, regardless of what time of day they are scheduled.

b. Tradeoffs
Our scheduler makes a classic greedy algorithmic tradeoff. In Scheduler.filter_by_time_budget, we sort tasks strictly by priority first, then pack them into the available time budget. If a higher-priority task fits, it is added. If a task is too long for the remaining budget, it is skipped, but the scheduler continues to evaluate the remaining items and will schedule a lower-priority task if it fits the remaining scraps of time.
Why this is reasonable: While this doesn't guarantee a mathematically perfect knapsack optimization, it perfectly mirrors real-world human preferences. Owners would always prefer to guarantee their pet gets their critical 10-minute medicine rather than fitting three minor 20-minute play sessions just to maximize "completed" tasks.

AI COLLABORATION
a. How you used AI
AI tools were heavily utilized during this project as structural architects, debugging assistants, and testing advisors:
Design Brainstorming: Used AI to translate the original project description into clean class structures.
Test Suite Expansion: Prompted AI to help draft comprehensive pytest assertions for edge-case scheduling behaviors.
UI Integration: Collaborated with the AI to map raw class data changes directly into Streamlit's session_state.

b. Judgment and verification
A major moment of intervention occurred during the development of Scheduler.detect_conflicts. The initial AI suggestion was a nested loop that matched tasks against themselves and raised duplicate alerts.
How I verified and evaluated: I rejected the naive nested-loop solution. Instead, I structured a single-pass evaluation using a Python dictionary tracker. I mapped out specific unit tests to manually inspect and prove that my refined, single-pass conflict tracker resolved overlaps correctly.

TESTING AND VERIFICATION
a. What you tested
The test suite in tests/test_pawpal.py targets five critical system capabilities:
Task Completion Status (test_task_completion): Assures marking a task completed correctly mutates its boolean state.
Task Addition Mechanics (test_task_addition): Confirms that appending a task to a Pet correctly scales up the collection state.
Multi-Key Sorting (test_priority_and_time_sorting): Verifies sorting handles numerical priority hierarchy first, then falls back to chronological string comparisons.
Time Budget Filtering (test_time_budget_filter): Assures that the budget engine skips over items that exceed constraints but successfully schedules later items that fit.
State File Persistence (test_json_persistence): Verifies JSON serialization and deserialization write and restore the identical state graph.

b. Confidence
I am highly confident that the scheduler works correctly. The entire test suite compiles and passes successfully in under 0.15 seconds.

REFLECTION
a. What went well
I am incredibly satisfied with how cleanly the data persistence layer integrated with the interactive Streamlit UI.

b. What you would improve
In a future iteration, I would implement interval-based scheduling instead of simple hour-minute string checks. Integrating a library like datetime would allow the scheduler to prevent overlapping time segments entirely.

c. Key takeaway
My biggest takeaway is that system architecture is a living, breathing entity. Decoupling logic into small, testable utility classes is the best way to keep a growing app stable.
