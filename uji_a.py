# uji_a.py — keygen dan encrypt dalam satu fungsi
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def satu_fungsi():
    key = AESGCM.generate_key(bit_length=256)
    aes_object = AESGCM(key)
    nonce = os.urandom(12)
    return aes_object.encrypt(nonce, b"data", None)
