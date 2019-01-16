def compare(s1, s2):
    if s1 is None or s2 is None:
        return False
    return strip_end(s1) == strip_end(s2)


def strip_end(s):
    return s if s == '' or s[-1] != '\n' else s[:-1]
