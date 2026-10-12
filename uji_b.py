# uji_b.py — encrypt di fungsi tanpa generate_key
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def pakai_key(key):
    aes_object = AESGCM(key)
    nonce = os.urandom(12)
    return aes_object.encrypt(nonce, b"data", None)
