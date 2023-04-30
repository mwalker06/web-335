# Title: usersp2.py
# Author: Megan Walker
# Date: 04/27/23
# Description: usersp2.py for Web 335 Assign_7
# References: WEB 335 GitHub, & WEB 335 Assign_7

# Import statements
from pymongo import MongoClient
import _datetime

# Connect to MongoDB Atlas cluster
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.dbdc0d0.mongodb.net/web335DBretryWrites=true&w=majority")

# Print the connection string
print(client)

# Configure the connection to the database
db = client.web335DB

# Write the Python code to create a new user document.
db.users.insert_one({ 
    "first_name": "John",
    "last_name": "Doe",
    "email": "jdoe@test.com",
    "employee_id": "1474",
    "date_created": _datetime.datetime.utcnow()
})

# Write the Python code to display the newly created document.
print(db.users.find_one({
    "first_name": "John",
    "last_name": "Doe",
}))

# Write the Python code to update the email address from the newly created document.
db.users.update_one(
    {"first_name": "John", "last_name": "Doe"},
    {"$set": {"email": "jdoe@testing.org"}}
)

# Write the Python code to display the updated document.
print(db.users.find_one({
    "first_name": "John",
    "last_name": "Doe",
}))

# Write the Python code to delete the document you created.
db.users.delete_one({
    "first_name": "John",
    "last_name": "Doe",
})

# Write the Python code to prove you have deleted the document.
print(db.users.find_one({
    "first_name": "John",
    "last_name": "Doe",
}))



