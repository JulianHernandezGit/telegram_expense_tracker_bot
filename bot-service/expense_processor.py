import json
from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage
from config import OPENAI_API_KEY

# Predefined expense categories
EXPENSE_CATEGORIES = [
    "Housing", "Transportation", "Food", "Utilities", "Insurance", 
    "Medical/Healthcare", "Savings", "Debt", "Education", "Entertainment", "Other"
]

# Initialize GPT-4o
model = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

def is_expense_message(message_text: str) -> bool:
    """
    Determine if a message contains expense-related information.
    """
    prompt = f"""
    Determine if the following message refers to an expense (payment, purchase, or cost).
    Message: "{message_text}"

    Respond with only "yes" or "no".
    """

    response = model.invoke([HumanMessage(content=prompt)])
    return response.content.strip().lower() == "yes"


def extract_expense_details(message_text: str):
    """
    Extract expense details from a message using GPT-4o.

    Returns:
        dict with keys: description, amount, category — or None if parsing fails.
    """
    prompt = f"""
    Extract the expense details from the following message.

    Message: "{message_text}"

    Extract and return:
    1. A short description of the expense
    2. The amount spent (as a number)
    3. The best category from this list:
       {', '.join(EXPENSE_CATEGORIES)}

    Return ONLY a valid JSON object like:
    {{
      "description": "Pizza",
      "amount": 20,
      "category": "Food"
    }}
    """

    response = model.invoke([HumanMessage(content=prompt)])
    raw_content = response.content.strip()

    # Clean markdown-style formatting if present
    if raw_content.startswith("```json"):
        raw_content = raw_content.replace("```json", "").replace("```", "").strip()
    elif raw_content.startswith("```"):
        raw_content = raw_content.replace("```", "").strip()

    try:
        parsed = json.loads(raw_content)

        # Optional: validate parsed fields
        if not all(key in parsed for key in ["description", "amount", "category"]):
            return None

        # Validate category
        if parsed["category"] not in EXPENSE_CATEGORIES:
            parsed["category"] = "Other"

        # Ensure amount is numeric
        parsed["amount"] = float(parsed["amount"])

        return parsed

    except (json.JSONDecodeError, ValueError, TypeError) as e:
        print("⚠️ Failed to parse GPT response:", raw_content)
        print("⚠️ Error:", str(e))
        return None
