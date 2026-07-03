# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

Our initial system design consists of four core classes:
- **Owner**: Tracks the owner's name and a list of pets. It handles adding new pets and pulling all combined tasks.
- **Pet**: Tracks individual pet profiles (name and species) and manages their specific task lists.
- **Task**: Represents a single care activity, storing its description, time, frequency, and completion status.
- **Scheduler**: The system's algorithmic brain. It handles cross-pet sorting, filtering, and conflict detection.

Core User Actions Supported:
- **Add a Pet:** Handled by `Owner.add_pet()`
- **Schedule a Routine:** Handled by `Pet.add_task()`
- **View Today's Tasks:** Handled by `Owner.get_all_tasks()` and processed by the `Scheduler`.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
