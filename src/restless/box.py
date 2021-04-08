from typing import Any
from restless.models import BoxModel
import restless.crypto
import restless.utils

class Box:

  def __init__(self, model: dict, gen_key: bool = False):
    if gen_key:
      model['key'] = restless.crypto.kdf()
    self.model = BoxModel(**model)

  def encrypt(self):
    self.model.data = restless.crypto.encrypt(self.model)
    self.model.encrypted = True
    return self.model

  def decrypt(self):
    self.model.data = restless.crypto.decrypt(self.model)
    self.model.encrypted = False
    return self.model

  def todict(self):
    return self.model.dict()

  def tojson(self):
    return self.model.json()
