def compare(s1, s2):
    return strip_end(s1) == strip_end(s2)


def strip_end(s):
    return s if s[-1] != '\n' else s[:-1]
