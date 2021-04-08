import sys
import os
import pytest
import json

curr_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, "src")

from restless.box import Box

class Test_encrypt:

  no_key_payload = {
    "data": b"This is my super unciphered text"
  }
  no_key_genkey = True
  no_key_expected = "This is my super unciphered text"

  self_generated_key_payload = {
    "key": os.urandom(32),
    "salt": os.urandom(8),
    "data": b"Vivelesdindes"
  }
  self_generated_key_genkey = False
  self_generated_key_expected = "Vivelesdindes"

  @pytest.mark.parametrize("payload,genkey, expected",
    [
      (no_key_payload, no_key_genkey, no_key_expected),
      (
        self_generated_key_payload,
        self_generated_key_genkey,
        self_generated_key_expected
      )
    ]
  )
  def test_encrypted_then_decrypted_data(
    self,
    payload: dict, genkey: bool, expected: str
  ):

    b = Box(model=payload, gen_key=genkey)
    encrypted_b = b.encrypt()
    print(encrypted_b)

    decrypted_b = b.decrypt()
    print(decrypted_b)

    json_obj = json.loads(b.tojson())

    assert json_obj['data'] == expected
