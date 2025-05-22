import hashlib

# Input string
text = "hello world"

# Convert to bytes
encoded_text = text.encode()

# Create a hash using SHA-256
hash_object = hashlib.sha256(encoded_text)

# Get the hexadecimal digest
hex_dig = hash_object.hexdigest()

print("Original text:", text)
print("SHA-256 hash:", hex_dig)
