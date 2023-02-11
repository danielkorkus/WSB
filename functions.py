# def multiply(x, y):
#     if isinstance(x, (int, float)) and isinstance(y, (int, float)):
#         return round(x * y, 5)
#     else:
#         return x * y
#
#
# def no_of_letter(text):
#     return len(str(text))


def fissbuzz(i):
    if isinstance(i, (str, float)): return int(i)
    if i <= 0: return None
    if i % 3 == 0 and i % 5 == 0:
        return "fissbuzz"
    elif i % 5 == 0:
        return "buzz"
    elif i % 3 == 0:
        return "fiss"
    else:
        return i