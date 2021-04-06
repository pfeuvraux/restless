from cryptography.hazmat.primitives.ciphers.aead import (
  AESGCM,
  ChaCha20Poly1305
)

class Ciphers:

  ciphers = {
    "aes-gcm": AESGCM,
    "chacha20": ChaCha20Poly1305
  }

def encrypt(model):

  cipher = Ciphers.ciphers[model.cipher]
  enc = cipher(model.key)

  return enc.encrypt(
    nonce=model.iv,
    data=model.data,
    associated_data=model.auth_data
  )
