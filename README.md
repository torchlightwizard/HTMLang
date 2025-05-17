# 🔧 Core Principles
1. No centralized controller
Each module should be self-contained and only aware of what it needs. Data flows, not commands.

2. Composable, swappable pieces
Think plug-and-play. You want to swap out the LLM, retriever, memory, or agent logic like LEGO blocks.

3. Minimal base contracts/interfaces
Interfaces for tools, chains, memory, models, etc., but no "uber-framework" that binds them all.

4. Runtime wiring over static inheritance
Instead of huge class trees, focus on functions, DI (dependency injection), and runtime composition.


# 🏠 Architecture
We go layer by layer. The lowest layer will be described first then we go upwards.

1. Each Model is a standalone component that
    1. Takes task (command + args = prompt)
    2. Runs task
    3. Outputs results
2. 