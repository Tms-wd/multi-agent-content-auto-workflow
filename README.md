# Multi-Agent Content Auto Workflow
## Project Overview
This project is an AI automated content generation and distribution workflow system based on multi-agent collaboration. It addresses the pain points of traditional content production, including heavy reliance on manual labor, fragmented processes, and inability to automatically iterate and optimize strategies.

The system adopts the collaboration of three types of intelligent agents: Planner, Executor and Reviewer. Leveraging the long-chain reasoning capability of large language models, it realizes full-link automation covering topic decomposition, content generation, self-inspection and revision, and standardized output. It also establishes a closed loop of operation log data backflow and feedback to continuously optimize prompts and execution strategies.

## Core Capabilities
- Division and collaboration of multi-role agents, with task decomposition and automatic flow
- LLM-driven end-to-end content generation, polishing and review
- Complete operation log recording, enabling traceability of each round of invocation and reasoning process
- Reusable standardized processes, supporting automated execution of batch tasks

## System Architecture
- **Planner Agent**: Requirement analysis, task splitting, and execution link planning
- **Executor Agent**: Invoke large language models to complete content generation and copywriting creation
- **Reviewer Agent**: Content self-inspection, compliance revision, and quality evaluation
- **Pipeline**: Overall scheduling, log recording, result output and feedback backflow

## Operation Method
1. Configure API credentials for large language model invocation
2. Run `pipeline_runner.py` to start the workflow
3. Automatically complete full-process tasks and output results
4. Operation logs are automatically saved to the `/logs` directory

## Project Deliverables & Verification Materials
- Complete runnable project source code
- Real operation log records
- Screenshots of workflow architecture and processes
- Actual usage records of continuous large language model invocation

## Application Scenarios
Implementation of AI Agent capabilities, practical application of LLM APIs, construction of automated workflows, and mass production and optimization of content.
