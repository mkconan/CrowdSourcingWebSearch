import re


def extract_key(url: str) -> str:
    return re.search(r"\d{7}$", url).group(0)
