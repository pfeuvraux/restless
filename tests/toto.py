
from src.restless.box import Box
from src.restless.utils import str_to_bytes

toto = {
  "data": str_to_bytes("vivelesdindes")
}

titi = Box(model=toto)

print(titi)
