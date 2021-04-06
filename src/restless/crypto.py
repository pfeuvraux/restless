from cryptography.hazmat.primitives.ciphers.aead import (
  AESGCM,
  ChaCha20Poly1305
)
from cryptography.hazmat.primitives.kdf import (
  pbkdf2,
  scrypt
)

class Ciphers:

  ciphers = {
    "aes-gcm": AESGCM,
    "chacha20": ChaCha20Poly1305
  }

class KDF:

  funcs = {
    "pbkdf2": pbkdf2,
    "scrypt": scrypt
  }

def encrypt(model):

  cipher = Ciphers.ciphers[model.cipher]
  enc = cipher(model.key)

  return enc.encrypt(
    data=model.data,
    nonce=model.iv,
    associated_data=model.auth_data
  )

def decrypt(model):

  cipher = Ciphers.ciphers[model.cipher]
  enc = cipher(model.key)

  return enc.decrypt(
    data=model.data
    nonce=model.iv,
    associated_data=model.auth_data
  )

def kdf(passphrase: str, kdf: str):

  raise NotImplemented
  kdf = KDF.funcs[kdf]
