"""
Task 3-4: File Search Tool

Wrap the FileSearchAgent as a tool that can be used by other agents.
This enables delegation - other agents can ask for file searches.

Complete the TODOs below to implement the search tool.
"""

import langroid as lr
from langroid.pydantic_v1 import Field
# TODO 1: Import the file_search_agent from file_search_agent.py

from file_search_agent import file_search_agent
class FileSearchTool(lr.ToolMessage):
    """Tool to search for files by delegating to FileSearchAgent."""
    
    # TODO 2: Set the request name for this tool -- NO SPACES!
    # This is the name that  agents will use to invoke this tool
    request: str = "file-search"
    
    # TODO 3: Add a clear purpose description, so LLM knows what this tool does
    purpose: str = "TODO: The purpose of this tool is too search for files "  # "To... "
    
    # TODO 4: Add a query field with description
    # (behind the scenes, the field descriptions are added to the system message)
    query: str = Field(
        ...,
        description="The query of what to search for"
    )

    # TODO 5: Add a directory field with description
    directory: str = Field(
        ...,
        description="TODO: The directory whose contents and files you are searching for"
    )
    
    def handle(self) -> str:
        """Search for files by delegating to FileSearchAgent."""
        # TODO 6: Create a non-interactive Task with the imported file_search_agent
        # (Set interactive=False)
        task = lr.Task(file_search_agent,interactive=False)  # Replace with lr.Task instance
        
        # TODO 7: Create a prompt for the file_search_agent,
        #  for the specific query and directory
        # (use self.query etc to access the fields)
        prompt = f"Search the directory '{self.directory}' for files matching the query:{self.query}"
        
        # TODO 8: Run the task and get the result
        result = task.run(prompt)  # your code here to run the task
        
        # TODO 9: Return the content from the result
        # Hint: result is a ChatDocument, which has a `content` field of type str
        return result.content  # Replace with return statement