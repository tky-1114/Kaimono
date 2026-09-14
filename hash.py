import hashlib

def hash_password(message):
    message = message.encode("utf-8")
    hashed = hashlib.sha512(message)
    hashed_hex = hashed.hexdigest()
    return hashed_hex