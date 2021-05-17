import re
from .decorators import use_clipboard


@use_clipboard
def format_http_request(raw):
    output = []
    lines = [l.strip('\r\n') for l in raw.split('\n')]

    output.append(lines.pop(0))

    headers = []
    headersDict = {}
    while h := lines.pop(0):
        headers.append(h)
        if m := re.search(r'([^:]+):\s*(.*)', h, re.IGNORECASE):
            headersDict[m.group(1).lower()] = m.group(2)
    headers = sorted(headers, key=lambda x: x.lower())
    output.extend(headers)
    output.append('')

    contentType = headersDict.get('content-type', '')
    for l in lines:
        if 'application/x-www-form-urlencoded' in contentType:
            entries = l.split('&')
            output.extend(sorted(entries, key=lambda x: x.lower()))
        else:
            output.append(l)

    return '\r\n'.join(output)


if __name__ == '__main__':
    format_http_request()
