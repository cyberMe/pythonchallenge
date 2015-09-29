""" Python challenge task 2
"""


def get_statistic(source_text):
    """ Counting all symbols in text.
    """
    symbols = {s: 0 for s in bytes(range(0, 256))}
    for symbol in source_text:
        symbols[symbol] += 1
    return symbols


def get_ordered(statistic, source_text):
    """ Return all symbols from statistic in order as they placed in source_text.
    """
    ordered = []
    list_statictic = list(statistic.keys())
    for symbol in source_text:
        if symbol in list_statictic:
            ordered.append(chr(symbol))
    return ordered


def challenge_ocr():
    """ Challenge 2 runner
    """
    url = """http://www.pythonchallenge.com/pc/def/ocr.html"""
    from chlg import get_text
    text = get_text(url)
    stat = get_statistic(text)
    filtered = {k: v for k, v in stat.items() if v == 1}
    result = get_ordered(filtered, text)
    print(result)

if __name__ == "__main__":
    challenge_ocr()
