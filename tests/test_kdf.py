import os

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA384
from restless.crypto import kdf
from restless.utils import str_to_bytes
import cryptography

kdf_func_passphrase_pbkdf = "vivelesdindes"


class Test_kdf:

  def test_pbkdf2(
    passphrase: bytes = kdf_func_passphrase_pbkdf,
    salt: bytes = os.urandom(8)
  ):

    derived_key, salt = kdf(
      passphrase=str_to_bytes(kdf_func_passphrase_pbkdf),
      kdf_func="pbkdf2",
      salt=salt
    )

    kdf_obj = PBKDF2HMAC(
      algorithm=SHA384,
      length=32,
      salt=salt,
      iterations=15000
    )
    test_derived_key = kdf_obj.derive(b"vivelesdindes")

    print(derived_key)
    print(test_derived_key)

    assert test_derived_key == derived_key
