""" Common functions for python challenge.
"""

def get_text(url):
    """ Extract commented text from url.
    """
    from urllib import request
    page_raw = request.urlopen(url).read()
    start = page_raw.rfind(b'<!--') + len(b'<!--')
    end = page_raw.rfind(b'-->')
    return page_raw[start:end]
