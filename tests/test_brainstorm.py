import sys
import os
# make sure novamind module is found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest.mock import patch # avoid real OpenAI requests
from novamind import brainstorm



@patch("novamind.OpenAI")
def test_brainstorm_generate_ideas(mock_openai):
    # check brainstorm function calls OpenAI and prints ideas as instructed

    # mock response structure similar to real api output
    mock_client = mock_openai.return_value
    mock_client.chat.completions.create.return_value = type(
        "MockResponse", (), {
            "choices": [
                {"message": {"content": "Idea 1: Alpha\nIdea 2: Beta\nIdea 3: Gamma"}}
            ]
        }
    )

    # run brainstorm function
    brainstorm("AI/ML", "build a project")

    # verify API call made
    mock_client.chat.completions.create.assert_called_once()

@patch("novamind.OpenAI")
def test_brainstorm_handles_api_error(mock_openai, capsys):
    # test brainstorm() function handles API failure
    mock_client = mock_openai.return_value
    mock_client.chat.completions.create.side_effect = Exception("API Error")

    brainstorm("AI", "learn something new")

    captured = capsys.readouterr()
    assert "Oops! Something went wrong" in captured.out
    assert "API Error" in captured.out