import hashlib
import base64


def calculate_base64_hash(base64_string):
    # Decode base64 string
    binary_data = base64.b64decode(base64_string)

    # Calculate SHA-256 hash
    sha256_hash = hashlib.sha256(binary_data).digest()

    # Convert hash to hexadecimal string
    hash_hex = sha256_hash.hex()

    return hash_hex
