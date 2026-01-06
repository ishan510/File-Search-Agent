"""
Task 3-4: File Search Agent

Create a specialized agent that can search through files to find content
matching a user's query. The agent should use file tools to explore
directories and examine file contents.

Complete the TODOs below to implement the file search agent.
"""

import os
from dotenv import load_dotenv
import langroid as lr
import langroid.language_models as lm
from langroid.agent.tools.orchestration import DoneTool
from file_tools import ListDirTool, ReadFileTool

# Load environment variables from .env file
load_dotenv()

# Get model from environment, default to Gemini if not set
CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gemini/gemini-2.0-flash-exp")


class FileSearchAgentConfig(lr.ChatAgentConfig):
    """Configuration for the file search specialist agent."""
    
    # TODO 1: Set a descriptive name for the agent
    name: str = "File_Search_Agent"
    
    # TODO 2: Configure the LLM
    # Hint: Use lm.OpenAIGPTConfig with chat_model=CHAT_MODEL
    llm: lm.OpenAIGPTConfig = lm.OpenAIGPTConfig(chat_model=CHAT_MODEL)  # Replace with proper configuration

    # IMPORTANT -- this nudges the agent to use tools when it forgets
    handle_llm_no_tool:str = f"""
    You FORGOT to use one of your TOOLs! Remember that:
    - You must use a combination of {ListDirTool.name()} and {ReadFileTool.name()} 
        to search for files;
    - You should use {DoneTool.name()} to return your results;
    """

    # TODO 3: Write a system message that:
    # - Explains the agent is a file search specialist
    # - Describes the search process:
    #   1. Use ListDirTool to list files
    #   2. Use ReadFileTool to examine contents
    #   3. Check if content matches the query
    #   4. Track all matching files
    # - Explains what makes a file match (keywords, topics, relevance)
    # - IMPORTANT: (a) Must use DoneTool to return results, with content field
    #   containing the string response.
    # - IMPORTANT: (b) If no matches, the content field must be EMPTY!
    # Note when naming tools in the system message, keep in mind that the
    # LLM does not know about the Tool Class names like ListDirTool, etc.
    # Instead, it is aware of the `request` value in the Tool's definition,
    # which is the name used in the system message. You should access this
    # value using the Tool's static method name(), e.g. ListDirTool.name(),
    # so you must use that in the system message when mentioning a tool.
    system_message: str = f"""
    TODO: You are a helpful file search assistant that can help list files, read files to examine contents, 
    check if the content matches the query, and track all matching files. A file match occurs when there is match with keywords, topics, or relevance.


    `{ListDirTool.name()}`: Use this to list the contents of a directory.
    `{ReadFileTool.name()}`: Use this to read and return the name of a file.
    `{DoneTool.name()}`: Use this when your task is complete to return the final result.

    IMPORTANT: If NO matches, the content field must be EMPTY!

    When your task is complete, you MUST use the `{DoneTool.name()}` tool to 
    indicate completion, and use the `content` field to return any response you wish to 
    provide. It is CRITICAL to use the `content` field to return any results 
    sought by the user, since they will NOT be able to see anything outside of this tool!
    """


def run_file_search(directory: str, query: str) -> str:
    """
    Create and run a file search agent to find files matching a query.
    
    Args:
        directory: The directory to search in
        query: The search query to match against file contents
        
    Returns:
        A string listing the matching files, or a message if no matches
    """
    # TODO 4: Create the FileSearchAgentConfig
    config = FileSearchAgentConfig()  # Replace with config instance
    
    # TODO 5: Create the ChatAgent
    agent = lr.ChatAgent(config)  # Replace with agent instance
    
    # TODO 6: Enable agent to use the required tools
    ... # your code here
    agent.enable_message(ListDirTool)
    agent.enable_message(ReadFileTool)
    agent.enable_message(DoneTool)

    # TODO 7: Create a Task with interactive=False
    task = lr.Task(agent,interactive=False)  # Replace with task instance
    
    # TODO 8: Create a prompt for the agent
    # Different from system message (which is a generic instruction),
    # this prompt should be specific to the current search task of
    # searching in a directory with a query.
    prompt = f"Search the directory '{directory}' for files whose contents match the query '{query}'. "  # Replace with your prompt
    
    # TODO 9: Run the task and get the result
    result = task.run(prompt)
    
    # TODO 10: Return the result content
    # Hint: Result is of type ChatDocument, which has a content field of type str
    return result.content # Replace with return statement


# TODO 11: Create and export the agent for use by other modules
# This allows the search tool to import and use this agent
# Steps:
# 1. Create a FileSearchAgentConfig instance
# 2. Create a ChatAgent with that config
# 3. Enable the required tools on the agent
# (can be done in 2 lines of code)
file_search_agent = lr.ChatAgent(FileSearchAgentConfig()) # 1st line to create the agent
file_search_agent.enable_message(ListDirTool)
file_search_agent.enable_message(ReadFileTool)
file_search_agent.enable_message(DoneTool)# 2nd line to enable tools
