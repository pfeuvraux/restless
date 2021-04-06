from typing import Any
from restless.models import BoxModel
import restless.crypto
import restless.utils

class Box:

  def __init__(self, model: dict):
    self.model = BoxModel(**model)

  def encrypt(self):
    self.model.data = restless.crypto.encrypt(self.model)
    return self.model

  def __dict__(self):
    return self.model.dict()

  def tojson(self):
    return restless.utils.tojson(
      data=self.__dict__()
    )
