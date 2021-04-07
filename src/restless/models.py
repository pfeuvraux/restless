from pydantic import (
  BaseModel,
  validator,
  StrictInt,
  StrictStr
)
from typing import Optional
import restless.crypto
from restless.utils import rand_gen

class BoxModel(BaseModel):
  key: bytes
  data: bytes
  iv: Optional[bytes] = rand_gen(12)
  auth_data: Optional[bytes] = rand_gen(12)
  cipher: Optional[str] = "aes-gcm"

  @validator("cipher")
  def cipher_must_be_implemented(cls, val):
    if not val in restless.crypto.Ciphers.ciphers:
      raise ValueError(f"{val} is ain't supported.")
    return val
