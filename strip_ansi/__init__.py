import re
__version__ = '0.1.0'

def strip_ansi(o: str) -> str:
    """
    Removes ANSI escape sequences from `o`, as defined by ECMA-048 in
    http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-048.pdf
    
    >>> strip_ansi("\\033[33mLorem ipsum\\033[0m")
    'Lorem ipsum'
    
    >>> strip_ansi("Lorem \\033[38;25mIpsum\\033[0m sit\\namet.")
    'Lorem Ipsum sit\\namet.'
    
    >>> strip_ansi("")
    ''
    
    >>> strip_ansi("\\x1b[0m")
    ''
    
    >>> strip_ansi("Lorem")
    'Lorem'
    
    >>> strip_ansi('\\x1b[38;5;32mLorem ipsum\\x1b[0m')
    'Lorem ipsum'
    
    >>> strip_ansi('\\x1b[1m\\x1b[46m\\x1b[31mLorem dolor sit ipsum\\x1b[0m')
    'Lorem dolor sit ipsum'
    """
    
    # pattern = re.compile(r'/(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]/')
    pattern = re.compile(r'\x1B\[\d+(;\d+){0,2}m')
    stripped = pattern.sub('', o)
    return stripped

if __name__ == "__main__":
    import doctest
    doctest.testmod()
