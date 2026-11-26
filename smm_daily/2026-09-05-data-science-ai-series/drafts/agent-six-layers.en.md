# Understanding the Six Layers of an AI Agent

![Six layers of an AI agent](../assets/agent-six-layers-light-en-v1.png)

“Find out why sales fell last month and prepare a report.”

A model can describe the steps. Delivering a trustworthy report requires more. In our agent development work, we separate that responsibility into six layers. This is an engineering framework, not a universal standard or a requirement for six separate agents.

## 1. Intent routing: define the task

Does the user want a number, an explanation, or a file? Establish the goal, data scope, and available capabilities. Ask for missing information before committing to an answer.

## 2. Context engineering: supply the relevant information

Does revenue include refunds? Should new stores be excluded? Each step needs the right definitions, data, and latest constraints. The system may store the full history; the model only needs the parts relevant to its current decision.

## 3. Reasoning and planning: adapt to results

Inspect the data, compare channels, and build charts. If inspection reveals a missing week, request more data or narrow the conclusion. The important loop is action, observation, and revision—not simply following the initial plan.

## 4. Tools and skills: execute the work

Queries, calculations, charts, and exports need real tools with clear inputs, outputs, and errors. A skill can package a procedure using several tools. A claim that the report is ready must correspond to an actual file.

## 5. Runtime harness: control execution

The harness manages state, permissions, retries, budgets, and logs. Planning chooses the next action; the harness controls execution and persists progress. After an export timeout, check whether it succeeded before retrying. Permission to create a report does not grant permission to email it to customers.

## 6. Verification and evaluation: check the result

Do totals reconcile? Does the file open? Are causal claims supported? Use programmatic checks for precise criteria and explicit rubrics for judgment. Verification checks this task; evaluation compares performance across a set of cases. Check intermediate results too.

The layers form a feedback loop. Tool results update context, failed checks can trigger replanning, and the harness manages execution throughout.

Start small: read one file, calculate one metric, and export one result. Then introduce missing data, a failed tool, and a changed requirement. Each layer now has a concrete problem to solve.

For AI learning and agent-project coaching, [find me on MentorCruise](https://mentorcruise.com/mentor/jaywang/). Explore [Curify](https://curify-ai.com/) for our visual creation and design workflow work.
