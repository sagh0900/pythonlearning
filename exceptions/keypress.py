"""Key press - A Module for detectung a single keypress"""

try:
    import msvcrt


    def getkey():
        """Wait for a keypress and return a single character string"""
        return msvcrt.getch()

except ImportError:

    import sys
    import tty
    import termios


    def getkey():
        """Wait for a keypress and return a single character string"""
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgettattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRIAN, original_attributes)
            return ch


# If either of the unix-specific tty or termios or not found
# We allow to ImportError to propogate from here.