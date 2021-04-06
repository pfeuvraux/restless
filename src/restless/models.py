from pydantic import (
  BaseModel,
  validator,
  StrictInt
)
from typing import Optional
import restless.crypto
from restless.utils import rand_gen

class BoxModel(BaseModel):
  key: Optional[bytes] = rand_gen(size=32) # FIXME: iomplem KDF
  data: bytes
  nonce: Optional[bytes] = rand_gen()
  iv: Optional[bytes] = rand_gen()
  auth_data: Optional[bytes] = rand_gen()
  cipher: Optional[str] = "aes-gcm"
  blocklength: Optional[StrictInt] = 64

  @validator("blocklength")
  def must_be_secure(cls, val):
    if val < 64:
      raise ValueError("Blocklength must be greater than 64.")
    return val

  @validator("cipher")
  def cipher_must_be_implemented(cls, val):
    if not val in restless.crypto.Ciphers.ciphers:
      raise ValueError(f"{val} is ain't supported.")
    return val
