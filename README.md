# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

* Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
* Consider constraints (time available, priority, owner preferences)
* Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

* Let a user enter basic owner + pet info
* Let a user add/edit tasks (duration + priority at minimum)
* Generate a daily schedule/plan based on constraints and priorities
* Display the plan clearly (and ideally explain the reasoning)
* Include tests for the most important scheduling behaviors

## Getting started

### Setup

```
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

```
--- PawPal+ System CLI Demo ---

⚠️  SYSTEM WARNINGS:
  Conflict detected: Multiple tasks scheduled at 14:00!

📅 Today's Optimized Schedule for Jean's Pets (Budget: 60 mins):
  P1 (10m) — Emergency Meds [⏳]
  P1 (15m) — Evening Feeding [⏳]
  P2 (30m) — Morning Walk [⏳]

🤖 Scheduler Engine Reasoning:
  Analysis complete. Scheduled 3 out of 4 tasks within a 60-minute limit.
Reasoning: High-priority (Priority 1) items were prioritized chronologically. Dropped 1 lower-priority items to prevent exceeding your time budget (Used 55/60 mins).

💾 Testing Data Persistence...
  State safely written to pawpal_data.json!

```

## 🧪 Testing PawPal+

```
# Run the full test suite:
python -m pytest

```

Sample test output:

```
============== test session starts ==============
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\jeanm\Desktop\ai110-module2show-pawpal-starter
plugins: anyio-4.14.0
collected 5 items                                

tests\test_pawpal.py .....                 [100%]

=============== 5 passed in 0.14s ===============

```

## 📐 Smarter Scheduling

| **Feature** | **Method(s)** | **Notes** |
| --- | --- | --- |
| Task sorting | `sort_by_priority_and_time` | Organizes tasks strictly by priority rank (1=High, 3=Low), breaking numerical ties chronologically by scheduled time. |
| Filtering | `filter_by_time_budget` | Advanced constraint checking. Dynamically drops lower priority items when total task durations exceed the owner's available free minutes. |
| Conflict handling | `detect_conflicts` | Iterates across all registered pets under an owner to warn if tasks share identical execution times. |
| Agent Reasoning | `generate_schedule_reasoning` | Synthesizes an analytical summary explaining exactly why tasks were chosen or dropped relative to budget constraints. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. **Initialize System Profiles:** An instance of `Owner` is initialized along with multiple instances of `Pet` objects (e.g., Biscuit the Dog, Luna the Cat, and Tweety the Bird).
2. **Assign Task Constraints:** Multiple care tasks are assigned to the pets, configured with designated times, strict priority levels (1–3), and specific durations in minutes.
3. **Execute System Evaluation:** The `Scheduler` engine runs cross-pet diagnostics to detect overlapping time slots and trigger visual alerts in the terminal window.
4. **Enforce Time Boundaries:** The system optimizes the schedule by matching task demands against a set daily allocation ceiling (60 minutes), prioritizing higher importance care items first.
5. **Interactive Custom Adjustments:** Users can switch to the edit tab to modify task duration or priority and toggle checkboxes to mark tasks completed, triggering real-time schedule updates.
6. **Serialize Application State:** The system calls its built-in persistence layer to output the operational graph out to `pawpal_data.json` to store current configurations between runs.