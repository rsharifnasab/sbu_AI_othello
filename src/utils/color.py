class colors(object):
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    BOLD = '\u001b[1m'
    RESET = '\u001b[0m'
    CLEAR = '\u001b[0m'

def error(text):
    print(f"{colors.BOLD}{colors.RED}{text}{colors.RESET}")
