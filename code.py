import sqlite3
from datetime import date, timedelta, datetime

# 1. Database Connection and Table Creation
def connect_db():
    # Connects to or creates the SQLite database file
    conn = sqlite3.connect('pharmacy_inventory.db')
    c = conn.cursor()
    # Create a table with an added 'expiry_date' column (stored as TEXT in 'YYYY-MM-DD' format)
    c.execute('''
        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            expiry_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn

# Connect on script start
conn = connect_db()
conn.close()

def add_medicine(name, quantity, price, expiry_date):
    conn = connect_db()
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO medicines (name, quantity, price, expiry_date) VALUES (?, ?, ?, ?)",
            (name, quantity, price, expiry_date)
        )
        conn.commit()
        print(f"Added: {name} with expiry {expiry_date}")
    except Exception as e:
        print(f"Error adding medicine: {e}")
    finally:
        conn.close()

def view_all_medicines():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM medicines")
    medicines = c.fetchall()
    conn.close()
    return medicines

# Example usage (for demonstration)
# print(view_all_medicines())

def check_expiry_alerts(days_threshold=30):
    conn = connect_db()
    c = conn.cursor()

    # 1. Check for **Expired** items (expiry_date is before today)
    c.execute("""
        SELECT name, quantity, expiry_date FROM medicines
        WHERE expiry_date < DATE('now')
    """)
    expired_items = c.fetchall()

    # 2. Check for **Near Expiry** items (expiry_date is between today and the threshold)
    c.execute("""
        SELECT name, quantity, expiry_date FROM medicines
        WHERE expiry_date BETWEEN DATE('now') AND DATE('now', ?)
    """, (f'+{days_threshold} days',))
    near_expiry_items = c.fetchall()

    conn.close()

    alerts = {}
    if expired_items:
        alerts['expired'] = expired_items
    if near_expiry_items:
        alerts['near_expiry'] = near_expiry_items
    
    return alerts

# --- DEMONSTRATION ---

# 1. Add some sample data (Dates are YYYY-MM-DD)
# Expiry: October 2025 (Expired)
add_medicine("Old Painkiller", 50, 5.99, "2025-10-15")
# Expiry: Within 30 days (Near Expiry - assuming today is Nov 2025)
future_near = date.today() + timedelta(days=20)
add_medicine("Vitamin C", 100, 12.50, future_near.strftime('%Y-%m-%d'))
# Expiry: Far in the future (Good Stock)
future_far = date.today() + timedelta(days=365)
add_medicine("Cough Syrup", 25, 8.00, future_far.strftime('%Y-%m-%d'))


# 2. Run the expiry check
print("\n--- Expiry Check Results ---")
alerts = check_expiry_alerts(days_threshold=30)

if 'expired' in alerts:
    print("🚨 **EXPIRED ITEMS** 🚨")
    for name, qty, exp_date in alerts['expired']:
        print(f"- {name}: {qty} units (Expired on {exp_date})")

if 'near_expiry' in alerts:
    print("\n⚠️ **NEAR EXPIRY (within 30 days)** ⚠️")
    for name, qty, exp_date in alerts['near_expiry']:
        print(f"- {name}: {qty} units (Expires on {exp_date})")

if not alerts:
    print("✅ No immediate expiry concerns found.")

# You will need to install Tkinter if you want a GUI, but the core logic works without it.