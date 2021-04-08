from cryptography.hazmat.primitives.ciphers.aead import (
  AESGCM,
  ChaCha20Poly1305
)
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.hashes import SHA384
from restless.utils import rand_gen
class Ciphers:

  ciphers = {
    "aes-gcm": AESGCM,
    "chacha20": ChaCha20Poly1305
  }

class KDF:

  funcs = {
    "pbkdf2": PBKDF2HMAC,
    "scrypt": Scrypt
  }

  params = {
    "pbkdf2": {
      "algorithm": SHA384,
      "length": 32, # 256 bits
      "iterations": 15000
    },
    "scrypt": {
      "length": 32,
      "n": 2**14,
      "r": 8,
      "p": 1
    }
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
    data=model.data,
    nonce=model.iv,
    associated_data=model.auth_data
  )

def kdf(passphrase: bytes = None, kdf_func: str = "pbkdf2", salt: bytes = None):

  if passphrase is None:
    passphrase = rand_gen(64)

  _kdf = KDF.funcs[kdf_func]
  _kdf_obj = KDF.params[kdf_func]

  if salt is None:
    _kdf_obj['salt'] = rand_gen(8)
  else:
      if type(salt) is bytes:
        _kdf_obj['salt'] = salt
      else:
        raise TypeError

  _kdf = _kdf(**_kdf_obj)

  return (
    _kdf.derive(passphrase),
    _kdf_obj['salt']
  )
