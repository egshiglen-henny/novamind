import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from novamind import validate_input

# valid inputs
@pytest.mark.parametrize("valid_input", [
    "AI/ML", "C++", "3D design", 
    "Machine Learning", "Python 3",
    "AI & Robotics", "DevOps - Automation",
    "data_pipeline"
])

def test_valid_inputs(valid_input):
    # make sure valid inputs pass
    assert validate_input(valid_input) is True

@pytest.mark.parametrize("invalid_input", [
    "", "   ", "1234", "@@@@", "!!!!", 
    "sadfagfsasa", "aaaaaa"
])

def test_invalid_inputs(invalid_input):
    # make sure invalid or gibberish inputs fail
    assert validate_input(invalid_input) is False

def test_repeated_character_pattern():
    # reject repeated characters
    assert validate_input("aaaaa") is False
    assert validate_input("zzzzz") is False

def test_long_random_word():
    # reject long gibberish strings
    assert validate_input("asdfasdfdsafas") is False

def test_invalid_single_letter_a():
    assert validate_input("a") is False

def test_valid_single_letter_r():
    assert validate_input("R") is True

def test_valid_single_letter_c():
    assert validate_input("C") is True

def test_mixed_case_valid():
    # pass mixed case
    assert validate_input("Web Design") is True

def test_numbers_with_letters():
    # pass alphanumeric words
    assert validate_input("Python3") is True
