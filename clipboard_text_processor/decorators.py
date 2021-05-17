import clipboard

def use_clipboard(func):
    def wrapper():
        result = func(clipboard.paste())
        clipboard.copy(result)
    return wrapper
