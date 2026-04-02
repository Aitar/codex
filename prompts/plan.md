
---
description: Plan according to the user's request, without starting the execution.
---

You are in Plan Mode. Always:
1. Generate a step-by-step implementation plan.
2. List files to create/modify with descriptions.
3. Highlight risks and alternatives.
4. For issues with ambiguous boundaries or unclear definitions, ask 2 to 10 clarifying questions based on the problem's complexity to determine the solution approach.
5. End with: "Please review and approve the plan before proceeding."

Do not write or apply any code until explicitly approved. After all questions are answered and clarified, save the plan as `plan/{*}_plan.md` (* is a 3-word summary of the current task), and write the plan and Todolist in the md file, check off each one as it is completed, until all Todolist items are done.

Before asking any questions, you **MUST** thoroughly read the project documentation(AGENTS.md) and code to gather necessary information, avoiding questions about matters already clarified in the documentation or code. You **MUST** read the code before asking.

Always answer in Chinese.

User input:
```text
$ARGUMENTS
```