""" Python challenge task 3.
    Find substring.
    One small letter, surrounded by EXACTLY three big bodyguards on each
    of its sides.
"""


def parse_text(text):
    """ Search by text with RegExp
    """
    from re import findall
    found = findall(b"[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]", text)
    return b"".join([x[4:5] for x in found])


def challenge_equality():
    """ Challenge equality solver
    """
    url = """http://www.pythonchallenge.com/pc/def/equality.html"""
    from chlg import get_text
    text = get_text(url)
    translated = text.translate(None, b'\n')
    parsed = parse_text(translated)
    print(parsed)

if __name__ == "__main__":
    challenge_equality()
