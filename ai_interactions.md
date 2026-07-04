**AI Interactions Log**

Agent Workflow (SF7)

What task did you give the agent?

I asked the agent to implement the Scheduler's filter_by_time_budget method based on the established Owner/Pet/Task class structure.

What did the agent do?


The agent generated the logic to iterate through tasks across multiple pets, calculate the total duration, and compare it against the user-provided time budget.

What did you have to verify or fix manually?

The initial code failed to handle cases where a pet had no tasks assigned. I manually added an empty-list check and refined the type hints to ensure compatibility with my existing class hierarchy.

Prompt Comparison (SF11)

Option A

Model / tool used: Gemini

Prompt: Act as a software architect. Define OOP classes (Owner, Pet, Task, Scheduler) with specific attributes and JSON persistence methods.

Response summary: Provided highly modular, well-structured code with robust JSON handling and clear type hints.

What was useful: The persistence methods were ready-to-use and matched my UML design.

Problems noticed: Minor adjustments needed for logic flow and attribute naming.

Decision: Accepted as the foundation for the project.

Option B

Model / tool used: ChatGPT

Prompt: Act as a software architect. Define OOP classes (Owner, Pet, Task, Scheduler) with specific attributes and JSON persistence methods.

Response summary: Provided a functional base, but the JSON serialization logic was less robust and required more boilerplate code.

What was useful: Class hierarchy structure was correct.

Problems noticed: Persistence logic was fragile; required significant refactoring for production-level error handling.

Decision: Rejected as a primary codebase.

Which approach did you use in your final implementation and why?

I used the Gemini approach (Option A). The persistence logic provided was significantly cleaner and required less maintenance than the output from Option B, allowing for faster integration into my existing codebase.
