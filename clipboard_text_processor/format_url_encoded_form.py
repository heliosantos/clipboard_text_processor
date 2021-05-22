import re
from .decorators import use_clipboard


@use_clipboard
def format_url_encoded_form(raw):
    output = list(filter(None, [l.strip() for l in raw.split('&')]))
    output = sorted(output)
    return '\r\n'.join(output)


if __name__ == '__main__':
    format_url_encoded_form()
