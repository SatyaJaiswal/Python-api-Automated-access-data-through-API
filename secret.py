import secrets
import string

# Define the length of your API key
key_length = 32  # You can adjust the length as needed

# Generate a random API key
api_key = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(key_length))

print("Generated API Key:", api_key)
