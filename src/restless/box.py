from typing import Any
from restless.models import BoxModel
import restless.crypto
import restless.utils

class Box:

  def __init__(self, model: dict, gen_key: bool = True):
    if gen_key:
      model['key'] = restless.crypto.kdf()
    self.model = BoxModel(**model)

  def encrypt(self):
    self.model.data = restless.crypto.encrypt(self.model)
    return self.model

  def decrypt(self):
    self.model.data = restless.crypto.decrypt(self.model)
    return self.model

  def __dict__(self):
    return self.model.dict()

  def tojson(self):
    return restless.utils.tojson(
      data=self.__dict__()
    )
