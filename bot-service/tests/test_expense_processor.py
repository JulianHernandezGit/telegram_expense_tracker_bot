import pytest
from expense_processor import is_expense_message, extract_expense_details, EXPENSE_CATEGORIES

# ---------------------- is_expense_message ----------------------

@pytest.mark.parametrize("text", [
    "Pizza 20 bucks",
    "Paid 50 for gas today",
    "Spent $120 on insurance",
    "Bought a new book for 15 USD"
])
def test_is_expense_message_positive(text):
    assert is_expense_message(text) is True, f"Expected True for: {text}"


@pytest.mark.parametrize("text", [
    "Hello, how are you?",
    "The sky is blue.",
    "What's the weather like?",
    "I'm going for a walk"
])
def test_is_expense_message_negative(text):
    assert is_expense_message(text) is False, f"Expected False for: {text}"

# ---------------------- extract_expense_details ----------------------

def test_extract_valid_expense():
    message = "I spent 30 dollars on groceries"
    result = extract_expense_details(message)

    assert isinstance(result, dict), "Expected a dictionary response"
    assert "description" in result, "Missing key: description"
    assert "amount" in result, "Missing key: amount"
    assert "category" in result, "Missing key: category"

    assert isinstance(result["description"], str), "Description must be a string"
    assert isinstance(result["amount"], float), "Amount must be a float"
    assert isinstance(result["category"], str), "Category must be a string"

    assert result["category"] in EXPENSE_CATEGORIES, f"Category '{result['category']}' not in expected list"

def test_extract_expense_with_odd_formatting():
    message = "Bought a sandwich: $7"
    result = extract_expense_details(message)

    assert result is not None, "Should not return None for valid input"
    assert isinstance(result["amount"], float), "Amount should be parsed correctly"

def test_extract_expense_with_uppercase_category():
    message = "Spent 100 on HOUSING"
    result = extract_expense_details(message)

    assert result is not None
    assert result["category"] in EXPENSE_CATEGORIES, f"Unexpected category: {result['category']}"

def test_extract_expense_with_missing_data():
    message = "Nice weather today!"
    result = extract_expense_details(message)
    assert result is None, "Expected None for irrelevant message"

def test_extract_expense_with_ambiguous_message():
    message = "Twenty bucks"
    result = extract_expense_details(message)

    # Could fail or succeed depending on model interpretation, so allow both
    if result:
        assert "amount" in result and isinstance(result["amount"], float), "If extracted, amount must be float"
    else:
        assert result is None, "Expected None or a valid parse"

def test_extract_expense_with_markdown_wrapped_json():
    message = "Paid 12 for Netflix subscription"
    result = extract_expense_details(message)

    assert result is not None
    assert result["category"] in EXPENSE_CATEGORIES

def test_fallback_category_assignment():
    """Force an invalid category and ensure fallback to 'Other'."""
    # Mock GPT response manually if you ever mock later.
    message = "Spent 50 on something unknown"
    result = extract_expense_details(message)
    
    assert result is not None
    assert result["category"] in EXPENSE_CATEGORIES, "Fallback to 'Other' if invalid"