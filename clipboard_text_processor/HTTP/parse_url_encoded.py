import re
from .decorators import use_clipboard


@use_clipboard
def parse_url_encoded(raw):
    output = raw.split('&')
    output = sorted(output)
    return '\r\n'.join(output)


if __name__ == '__main__':
    parse_url_encoded()
