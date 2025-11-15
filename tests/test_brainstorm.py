import sys
import os
# make sure novamind module is found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import patch # avoid real OpenAI requests
from novamind import brainstorm



@patch("novamind.OpenAI")
def test_brainstorm_generate_ideas(mock_openai):
    # check brainstorm function calls OpenAI and prints ideas as instructed

    # mock response structure similar to real api output
    mock_client = mock_openai.return_value
    mock_client.chat.completions.create.return_value = {
            "choices": [
                {"message": {"content": "Idea 1\nIdea 2\nIdea 3"}}
            ]
        }

    # run brainstorm function
    result = brainstorm("AI/ML", "build a project")

    assert "Idea 1" in result
    assert "Idea 2" in result
    assert "Idea 3" in result

    # verify API call made
    mock_client.chat.completions.create.assert_called_once()

@patch("novamind.OpenAI")
def test_brainstorm_handles_api_error(mock_openai):
    # test brainstorm() function handles API failure
    mock_client = mock_openai.return_value
    mock_client.chat.completions.create.side_effect = Exception("API Error")

    result = brainstorm("AI", "learn something new")

    assert "ERROR" in result
    assert "API Error" in result