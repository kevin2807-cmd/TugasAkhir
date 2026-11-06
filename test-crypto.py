
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# =====================================================
# CASE 1: Key dibuat menggunakan generator CSPRNG
# =====================================================

def case_1_generated_key():
    key = Fernet.generate_key()

    cipher = Fernet(key)

    encrypted = cipher.encrypt(b"Hello World")

    print("[CASE 1] Generated Key")
    print("Key generated:", key)
    print("Encrypted:", encrypted)


# =====================================================
# CASE 2: Key ditulis langsung (HARDCODED)
# =====================================================

def case_2_hardcoded_key():
    key = b"01234567890123456789012345678901"

    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(b"1234567890123456")
    )

    print("[CASE 2] Hardcoded Key")
    print("Key:", key)
    print("Cipher:", cipher)


# =====================================================
# CASE 3: Key berasal dari environment variable
# =====================================================

def case_3_external_key():
    key = os.environ.get("SECRET_KEY")

    if key is None:
        print("[CASE 3] SECRET_KEY not configured")
        return

    key_bytes = key.encode()

    cipher = Cipher(
        algorithms.AES(key_bytes),
        modes.CBC(b"1234567890123456")
    )

    print("[CASE 3] External Key")
    print("Cipher:", cipher)


# =====================================================
# CASE 4: Key berasal dari proses derivasi (KDF)
# =====================================================

def case_4_derived_key():
    password = b"example-password"
    salt = b"example-salt-1234"

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )

    key = kdf.derive(password)

    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(b"1234567890123456")
    )

    print("[CASE 4] Derived Key")
    print("Cipher:", cipher)


# =====================================================
# CASE 5: Key tidak diketahui (UNKNOWN)
# =====================================================

def case_5_unknown_key(key):
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(b"1234567890123456")
    )

    print("[CASE 5] Unknown Key")
    print("Cipher:", cipher)


if __name__ == "__main__":
    case_1_generated_key()
    case_2_hardcoded_key()
    case_3_external_key()
    case_4_derived_key()

    # Nilai key hanya diberikan ketika program dijalankan
    runtime_key = os.urandom(32)
    case_5_unknown_key(runtime_key)
