import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars


def generate_random_password(pwd_length: int = 8) -> str:
    password: str = ''.join(secrets.choice(alphabet) for i in range(pwd_length))
    return password
