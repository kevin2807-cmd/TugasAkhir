from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# =====================================================
# TEST 1: List dengan indeks langsung
# =====================================================

def test_list_index():
    supported_algs = [
        hashes.SHA256(),
        hashes.SHA512()
    ]

    algorithm = supported_algs[0]

    h = hmac.HMAC(b"secret-key", algorithm)
    h.update(b"Hello World")
    signature = h.finalize()
