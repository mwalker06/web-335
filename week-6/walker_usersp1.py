# Title: usersp1.py
# Author: Megan Walker
# Date: 04/23/23
# Description: usersp1.py for Web 335 Assign_6
# References: WEB 335 GitHub, & WEB 335 Assign_6,

# Import statements
from pymongo import MongoClient

# Connect to MongoDB Atlas cluster
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.1txnlsv.mongodb.net/web335DBretryWrites=true&w=majority")

# Configure the connection to the database    
db = client['web335DB']

# Call the find_one method to display a user document
print(db.users.find_one())

# Call the find_one method to display a user document with employee_id "1011"
print(db.users.find_one({"employee_id": "1011"}))

# Call the find_one method to display a user document with last_name "Mozart"
print(db.users.find_one({"last_name": "Mozart"}))
