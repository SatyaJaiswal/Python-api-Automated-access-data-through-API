import pymongo

# Connect to the MongoDB server running locally. You can customize the connection URL as needed.
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select or create a database (change "mydatabase" to your preferred database name).
db = client["patient"]

# Create a collection (similar to a table in SQL) for storing data (change "mycollection" to your preferred collection name).
collection = db["patient_database"]

# Take user input
name = input("Enter a name: ")
mobile_number = int(input("Enter Contact number:"))
DOB = input("Enter your DOB :")
age = int(input("Enter an age: "))
Address = input("Enter your address here....")

# Create a document (record) to insert into the collection
data = {
    "name": name,
    "mobile_number": mobile_number,
    "Dob": DOB,
    "age": age,
    "Address" : Address
}

# Insert the document into the collection
result = collection.insert_one(data)

# Print the result of the insertion
print("Data inserted with ID:", result.inserted_id)

# Close the MongoDB connection
client.close()
