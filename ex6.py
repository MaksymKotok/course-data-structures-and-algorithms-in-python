def reverse(string):
    return string[-1] + reverse(string[:-1]) if string != "" else ""
