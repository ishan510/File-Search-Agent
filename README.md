# File Search Agent

An intelligent file search agent built with Langroid that uses LLM-powered reasoning to search through files and find content matching user queries. The agent can explore directories, examine file contents, and return relevant results with explanations.

## Description

This project implements a specialized **FileSearchAgent** that intelligently searches through files using natural language queries. The agent leverages file manipulation tools (ListDirTool, ReadFileTool) to explore directory structures and examine file contents, then uses LLM reasoning to determine relevance and return matching files.

The agent is also wrapped as a **FileSearchTool** that can be used by other agents in a multi-agent system, enabling delegation of file search tasks.

**Key Features:**
- 🔍 Intelligent file search using LLM reasoning
- 📁 Directory exploration and file content analysis
- 🛠️ Tool-based architecture for extensibility
- 🤖 Multi-agent compatible (can be used as a tool by other agents)
- 📊 Detailed HTML logs for debugging and transparency

## Objective

Create a specialized FileSearchAgent that can search through files to find content matching a user's query. Then wrap this agent as a tool (FileSearchTool) that can be used by other agents.

## What You'll Build

1. **FileSearchAgent** - A specialized agent that:
   - Accepts search queries
   - Uses ListDirTool to explore directories
   - Uses ReadFileTool to examine file contents
   - Returns relevant files with explanations
   - Uses DoneTool to indicate completion

2. **FileSearchTool** - A tool wrapper that:
   - Allows other agents to delegate search tasks
   - Runs the FileSearchAgent non-interactively
   - Returns search results

## Files to Complete

- `file_search_agent.py` - Implement the FileSearchAgent
- `search_tool.py` - Implement the FileSearchTool wrapper

## Provided Files

- `file_tools.py` - Basic file manipulation tools (ListDirTool, ReadFileTool)
  (you built these in a prior assignment)
- `myfiles/` - Sample files to search through -- DO NOT CHANGE THESE!
- `test.py` - Tests to verify your implementation

## Getting Started

### 1. Install UV (if not already installed):

```bash
# On macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows:
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or using pip:
pip install uv
```

### 2. Navigate to the assignment folder and create a virtual environment:

**⚠️ CRITICAL**: All scripts and tests MUST be run from the assignment folder. 
Do not run them from parent directories or other locations.

```bash
# First, navigate to the assignment folder
cd <assignment-folder>

# Create a virtual environment with Python 3.11
uv venv --python 3.11

# Activate it
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```

### 3. Install dependencies:

```bash
# Install all dependencies from pyproject.toml
uv sync
```

### 4. Configure environment variables:

Create a `.env` file with the below settings; use the API credentials given by your 
instructors.

```bash
# .env file
OPENAI_API_KEY=your_api_key_here
# If using an API proxy/base URL:
OPENAI_API_BASE=https://your-api-base-url
OPENAI_CHAT_MODEL=gemini-2.5-flash  # or another model
```

### 5. Start implementing:

Look for TODO comments in the Python files - these indicate exactly where you need to 
add code. Some TODOs include hints to help guide your implementation. 
As a reminder, these are the files you need to complete:

- `file_search_agent.py` - Implement the FileSearchAgent
- `search_tool.py` - Implement the FileSearchTool wrapper


```bash
# You can run tests to check your progress:
pytest test.py -v
```

## Implementation Steps

1. Start with `file_search_agent.py`:
   - Complete the FileSearchAgentConfig class
   - Implement the run_file_search function
   - Create and export the file_search_agent instance

2. Then complete `search_tool.py`:
   - Implement the FileSearchTool class
   - Add proper field definitions
   - Implement the handle method

## Testing

Run tests as below. The language model is picked up from the environment variable 
`OPENAI_CHAT_MODEL`, but you can override it with the `--model` flag as shown
(you may not need to do this, but it's useful to know).

You must continue implementing your code until all tests pass.

```bash
# Run all tests
pytest test.py -v

# Run with a specific model
pytest test.py -v --model gemini-2.5-flash

# Run a specific test
pytest test.py::test_file_search_direct -v --model gemini-2.5-flash
```

### Debugging Tip

When running your agents, Langroid generates HTML logs that are extremely useful for debugging. Look for log messages like:

```
WARNING - 📊 HTML Log: file:///Users/.../logs/FileSearchAgent.html
```

This path is clickable in most terminals:
- **Mac**: Hold Cmd and click the path
- **Windows**: Ctrl+click the path
- **Linux**: Ctrl+click or right-click and select "Open Link"
- **If clicking doesn't work**: Copy the entire path and paste it into your browser

These HTML logs show:
- The complete system message sent to the LLM
- All LLM outputs and responses
- Tool calls made by the agent
- Results returned from tool calls
- The full conversation history

Open these HTML files in your browser to see exactly what your agent is doing and help debug any issues.

## Tips

- The FileSearchAgent should be thorough in its search
- Use clear, informative system messages
- Remember to enable all necessary tools (including DoneTool)
- The agent should explain which files it found and why they're relevant
- Handle cases where no files match the query