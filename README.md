# restless

Relies on [AN END-TO-END ENCRYPTED PROTOCOL FOR CLOUD STORAGE SOLUTIONS](https://drive.google.com/file/d/1WWaENjSxAOjdSJqD1EiCcVycP-1oygoi/view).

**Don't use it for production purposes**, at your own risks.

# Usage

```py
# That should work, idk.
# Just check the written tests at ./tests/ if you 
# seek for an advanced usage.

import restless.box
from restless.utils import str_to_bytes

plaintext = "Vive les dindes" # "Long live turkeys", literally, or "turkeys rock"

data = {
    "data": str_to_bytes(plaintext),
}

b = restless.box.Box(data, gen_key=True)
b.encrypt()

encrypted_json = b.tojson() # every value of bytes type will be base64-encoded
encrypted_dict = b.todict()

b.decrypt()

decrypted_json = b.tojson()
decrypted_dict = b.todict()
```

The other way around should work as well:

```py
import restless.box
from restless.utils import str_to_bytes

plaintext = "totolafrite" # "toto the French fries"

data = {
    "data": str_to_bytes(plaintext),
}

b = restless.box.Box(data, gen_key=True)
encrypted_data = b.encrypt()

print(encrypted_data.data)
# b'\x8e$\x9eR\xec0[\xfb\xb4\x1e\x80\xe1-\x907\xd02\x07\xbd&T"f\xfe_\x0e\x96\x0c\x08'

encrypted_data_to_dict = encrypted_data.todict()
t = restless.box.Box(**encrypted_data_to_dict)
print(t.decrypt())
```

# Tests

```sh

pipenv sync &&
pipenv run pytest -vvv -s
```
