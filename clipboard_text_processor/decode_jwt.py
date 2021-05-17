import base64
import json
from .decorators import use_clipboard


@use_clipboard
def decode_jwt(rawJwt):
    jwtencodedpayload = rawJwt.split('.')[1]
    padding = '=' * (len(jwtencodedpayload) % 4)
    jwtpayload = base64.b64decode(jwtencodedpayload + padding)
    j = json.loads(jwtpayload)
    return json.dumps(j, indent=4)


if __name__ == '__main__':
    decode_jwt()
