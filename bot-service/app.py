from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from expense_processor import is_expense_message, extract_expense_details
from database import is_user_whitelisted, get_user_id, save_expense
import uvicorn
from config import BOT_PORT

app = FastAPI()

class TelegramMessage(BaseModel):
    telegram_id: str
    message_text: str

@app.post("/process-message")
async def process_message(message: TelegramMessage):
    # Check if user is whitelisted
    if not is_user_whitelisted(message.telegram_id):
        return {"status": "ignored", "reason": "user not whitelisted"}
    
    # Check if message contains expense information
    if not is_expense_message(message.message_text):
        return {"status": "ignored", "reason": "not an expense message"}
    
    # Extract expense details
    expense_details = extract_expense_details(message.message_text)
    if not expense_details:
        return {"status": "error", "reason": "could not extract expense details"}
    
    # Get user ID
    user_id = get_user_id(message.telegram_id)
    if not user_id:
        return {"status": "error", "reason": "user id not found"}
    
    # Save expense to database
    try:
        save_expense(
            user_id=user_id,
            description=expense_details["description"],
            amount=expense_details["amount"],
            category=expense_details["category"]
        )
        
        return {
            "status": "success", 
            "message": f"{expense_details['category']} expense added ✅",
            "expense": expense_details
        }
    except Exception as e:
        return {"status": "error", "reason": str(e)}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=BOT_PORT, reload=True) 