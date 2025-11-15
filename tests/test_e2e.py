import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from unittest.mock import patch
from novamind import run_pipeline

@patch("novamind.OpenAI")
def test_e2e_full_pipeline(mock_openai):
    mock_client = mock_openai.return_value
    mock_client.chat.completions.create.return_value = {
            "choices": [
                {"message": {"content": "Mocked final ideas"}}
            ]
        }

    result = run_pipeline("AI", "build a project")

    assert "Mocked final ideas" in result

def test_e2e_validation():
    # invalid interests
    assert run_pipeline("", "goal") == "Invalid interests"

    # invalid goal
    assert run_pipeline("AI", "") == "Invalid goal"