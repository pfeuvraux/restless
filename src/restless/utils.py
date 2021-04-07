from os import urandom
from json import dumps
from typing import Any
import base64

def rand_gen(size: int = 64) -> bytes:
  return urandom(size)

def tojson(data: Any):
  return dumps(obj=data, indent=2)

def str_to_bytes(data: str) -> bytes:
  return data.encode()

def bytes_to_str(data: bytes) -> str:
  return data.decode()

def bytes_to_base64(data: bytes) -> str:
    return bytes_to_str(
      data=base64.encode(data)
    )
