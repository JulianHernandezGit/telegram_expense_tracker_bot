from supabase import create_client
from config import SUPABASE_URL, SUPABASE_API_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

def is_user_whitelisted(telegram_id):
    """Check if a Telegram user is in the whitelist."""
    response = supabase.table("users").select("*").eq("telegram_id", telegram_id).execute()
    return len(response.data) > 0

def get_user_id(telegram_id):
    """Get the user ID from the database."""
    response = supabase.table("users").select("id").eq("telegram_id", telegram_id).execute()
    if len(response.data) > 0:
        return response.data[0]["id"]
    return None

def save_expense(user_id, description, amount, category):
    """Save an expense to the database."""
    from datetime import datetime
    
    data = {
        "user_id": user_id,
        "description": description,
        "amount": amount,
        "category": category,
        "added_at": datetime.now().isoformat()
    }
    
    response = supabase.table("expenses").insert(data).execute()
    return response.data 