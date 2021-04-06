from os import urandom
from json import dumps
from typing import Any

def rand_gen(size: int = 64) -> bytes:
  return urandom(size)

def tojson(data: Any):
  return dumps(obj=data, indent=2)

def str_to_bytes(data: str, encoding: str = "utf-8"):
  return str.encode(encoding)
