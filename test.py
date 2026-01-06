"""
Tests for Task 3-4: File Search Agent and Tool
"""

import pytest
from file_search_agent import run_file_search
from search_tool import FileSearchTool


def test_file_search_direct():
    """Test the file search agent directly."""
    # Search for music-related files
    result = run_file_search("myfiles", "music")
    
    # Should find multiple music files
    assert "beethoven.md" in result or "beyonce.md" in result or "bill_evans.md" in result
    assert len(result) > 50  # Should have substantial content


def test_file_search_finance():
    """Test searching for finance-related content."""
    result = run_file_search("myfiles", "finance investment budget")
    
    # Should find finance files
    assert any(term in result.lower() for term in ["investment", "budget", "debt", "finance"])
    assert len(result) > 50  # Should have substantial content


def test_file_search_specific():
    """Test searching for specific content."""
    result = run_file_search("myfiles", "jazz piano")
    
    # Should find Bill Evans file
    assert "bill_evans" in result.lower()
    assert "jazz" in result.lower()


def test_search_tool():
    """Test the FileSearchTool wrapper."""
    tool = FileSearchTool(query="classical music", directory="myfiles")
    result = tool.handle()
    
    # Should find Beethoven file
    assert "beethoven" in result.lower()
    assert len(result) > 20


def test_search_tool_no_results():
    """Test search with no expected results."""
    tool = FileSearchTool(query="quantum physics astronomy", directory="myfiles")
    result = tool.handle()
    
    # Should handle no results gracefully
    assert result.lower() == ""


# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])