def multiply(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return round(x * y, 5)
    else:
        return x * y


def no_of_letter(text):
    return len(str(text))
