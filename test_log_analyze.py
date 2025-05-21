import pytest
from io import StringIO
from unittest.mock import patch

# Assuming the analyze_log function is imported from ci_log_analyzer.py
from log_analyze import analyze_log

# Mock function for OpenAI API to simulate GPT responses
def mock_analyze_log(log_content):
    return "AI suggests checking the 'foo()' function for the return value."

# Test the analyze_log function with a mock log content
def test_analyze_log_success():
    mock_log = """
    =======================================================
    FAILURE: test_example.py::test_example1
    Traceback:
      File "test_example.py", line 15, in test_example1
        assert foo() == 10
    AssertionError: assert 5 == 10
    """
    result = analyze_log(mock_log)
    assert "suggest checking" in result
    # Patching the actual OpenAI API call to use the mock
    with patch('ci_log_analyzer.analyze_log', side_effect=mock_analyze_log):
        result = analyze_log(mock_log)
        
    assert result == "AI suggests checking the 'foo()' function for the return value."

# Test case for empty log content
def test_analyze_log_empty():
    result = analyze_log("")
    assert "No logs to analyze" in result
