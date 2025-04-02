import pytest
from expense_processor import is_expense_message, extract_expense_details

def test_is_expense_message():
    # Test positive cases
    assert is_expense_message("Pizza 20 bucks") == True
    assert is_expense_message("Paid 50 for gas today") == True
    
    # Test negative cases
    assert is_expense_message("Hello, how are you?") == False
    assert is_expense_message("What's the weather like?") == False

def test_extract_expense_details():
    # Test extraction
    result = extract_expense_details("Pizza 20 bucks")
    assert result["description"] == "Pizza"
    assert result["amount"] == 20
    assert result["category"] == "Food" 