---
name: smart-shot
description: Zero-shot enhancer. Use when the user invokes smart-shot or asks very ambiguos and short prompt
---

Do not draft or decide deliverables until the Intent Resolver returns. Do not pick quick resolution path but follow the skill instructions. Treat the user prompt as a surface request, not automatically as the task. Spawn intent subagent that will run 5 why on user prompt to infer hidden user intents, objectives, consequencial objectives and requirements. Instruct it to create a plan how to address all of them. Objective is to deliver intents. Plan may contain multiple deliverable types. Each deliverable type must be covered explicitly and bounded by output contract. Subagent must return all intents, objectives and the plan with deliverable types and output contracts. Superlatives need a comparison set from the prompt, not from the available context. Infer success criteria before creating the plan.
Infer expert domains from the material and required for the design trees. Infer what each expert is responsible for. Infer what LLM Judges experts are needed. Spawn expert subagents for each identified domain and role. Expert subagents must act as practitioners of their inferred profession and responsibilities, applying the highest standards expected in real work rather than giving generic advice. Use best market practices when choosing appraoches and methodologies, e.g. for software development, sales funnel presentation, ASO and AISO, specific analysis analysis, etc. Use credible sources and expert opinions. Each responsible expert’s answer becomes binding for its aspect. Experts must refine the success criteria before the plan is finalized.
No more than 5 active subagents at a time.
Interview responsible expert subagents relentlessly about every responsible aspect of plan until understanding is reached. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question expert subagent provides the recommended answer. All deliverable types and output contracts must be processed.
Be aware of the subagent context window. Respawn a subagent if at risk it would reach 70% of the context window.
Review and adjust design tree after the response and the feedback before continuing with the next very small batch of questions.
After expert decisions are resolved, write execution specification. Execute the specification.
For software development type deliverables use SOLID and TDD.
Continue PDCA until the execution specification and final output satisfy the inferred intent.
Subagents are encouraged to perform Context Discovery using means available. Including to performing actions.
The final output must address every objective or explicitly mark it out of scope. Infer what the user wants back.
