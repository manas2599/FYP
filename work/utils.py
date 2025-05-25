import base64
from cryptography.fernet import Fernet

def generate_key():
    """Generate a Fernet key and return a readable ~22-char version."""
    key = Fernet.generate_key()
    return base64.urlsafe_b64encode(key)[:22].decode()  # ~22-char