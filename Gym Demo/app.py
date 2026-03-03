import os
import sqlite3
import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_mailman import Mail, EmailMessage
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app, resources={r"/*": {
    "origins": "*",
    "methods": ["GET", "POST", "OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization"]
}})  # Allows Vue to talk to Flask

# 1. SECURITY: Rate Limiting (Prevents DDoS/Spam)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

# 2. NOTIFICATIONS: Email Setup
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MY_EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('MY_PASSWORD')  
mail = Mail(app)

# 3. STORAGE: Database Initialization
def init_db():
    conn = sqlite3.connect('gym_leads.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS leads 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, goal TEXT, timestamp DATETIME)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/api/enquiry', methods=['POST'])
@limiter.limit("2 per minute") # Strict anti-spam limit
def handle_enquiry():
    data = request.json
    
    # 4. SECURITY: Honeypot Check (Trap for Bots)
    if data.get('website'): 
        return jsonify({"status": "error", "message": "Bot detected"}), 403

    name = data.get('name', '').strip()
    # email = data.get('email', '').strip() 
    phone = data.get('phone', '').strip()
    goal = data.get('goal', 'General')

    if not name or len(phone) < 10: #add email here to mail back to sender
    # and then generate a simple otp or we can use subsription otp service
        return jsonify({"status": "error", "message": "Invalid Details"}), 400

    # 5. SAVE TO DATABASE
    conn = sqlite3.connect('gym_leads.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO leads (name, phone, goal, timestamp) VALUES (?, ?, ?, ?)',
                   (name, phone, goal, datetime.datetime.now()))
    conn.commit()
    conn.close()

    # 6. SEND INSTANT EMAIL TO OWNER
    msg = EmailMessage(
        subject=f"🔥 NEW LEAD: {name}",
        body=f"Name: {name}\nPhone: {phone}\nGoal: {goal}\nSent via Andrew+Gemini's GymBot 2026",
        to=[os.getenv('OWNER_EMAIL')  ] # Replace with owner's email
    )
    msg.send()

    return jsonify({"status": "success", "message": "Lead Saved & Owner Notified!"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
