 Pharmacy Inventory & Expiry Tracker

A lightweight and handy Python tool for keeping track of medicine stock. Instead of manually checking dates, this script remembers everything for you. It manages your inventory and—most importantly—gives you a heads-up before your medicines go bad.

📌 What It Does

✔ Zero Setup Needed – Just run the script, and it builds the database (pharmacy_inventory.db) automatically.

✔ Spots Expired Items – Instantly flags anything that is past its use-by date.

✔ Early Warning System – Warns you about items expiring soon (e.g., within the next 30 days) so you can act fast.

✔ Crash-Proof – Includes error handling so a typo doesn't break the program.

✔ Smart Sorting – Automatically categorizes your stock:

🚨 Expired :-Throw it out

⚠️ Near Expiry :-Use it soon!

✅ Safe :-Good for now

 Technologies used

Python 3.x

SQLite3 (Built-in database)

Datetime (Handles the math for days and months)

▶ How to Run the project

Make sure you have Python installed.

Save the code as pharmacy_tracker.py.

Open your terminal or command prompt in that folder.

Run it by typing:

Bash

python pharmacy_tracker.py
The script will create the database, add some test medicines, and show you the alerts immediately.

📊 How It Decides What to Flag

The system looks at today's date and compares it to the medicine's expiry date to decide its status.

Date is in the past,   Expired,🚨             EXPIRED ITEMS
Date is within         30 days ,Near           Expiry,⚠️ NEAR EXPIRY
Date is far in the     future ,Safe Stock,     ✅ No Alert
