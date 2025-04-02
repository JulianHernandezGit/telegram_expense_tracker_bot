from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage
from config import OPENAI_API_KEY

# Define expense categories
EXPENSE_CATEGORIES = [
    "Housing", "Transportation", "Food", "Utilities", "Insurance", 
    "Medical/Healthcare", "Savings", "Debt", "Education", "Entertainment", "Other"
]

# Initialize GPT-4o
model = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

def is_expense_message(message_text):
    """Determine if a message contains expense information."""
    prompt = f"""
    Determine if the following message contains an expense (cost, payment, purchase) information.
    Message: "{message_text}"
    
    Answer with only "yes" or "no".
    """
    
    response = model.invoke([HumanMessage(content=prompt)])
    return response.content.strip().lower() == "yes"

def extract_expense_details(message_text):
    """Extract expense details from a message."""
    prompt = f"""
    Extract expense information from the following message.
    Message: "{message_text}"
    
    Parse out:
    1. A brief description of the expense
    2. The amount spent (in numeric form)
    3. The most appropriate category from this list: {', '.join(EXPENSE_CATEGORIES)}
    
    Format your response as a JSON object with keys: "description", "amount", "category".
    """
    
    response = model.invoke([HumanMessage(content=prompt)])
    
    # Parse the JSON response
    import json
    try:
        result = json.loads(response.content)
        return result
    except json.JSONDecodeError:
        # Fallback for non-JSON responses
        return None 