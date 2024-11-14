# try:
#     import pqrs
#     print(pqrs)
# except:
#     print("No Module Imported..")

try:
    # Microsoft Visual C++ Runtime (MSVCRT) - Only on Windows OS
    import msvcrt

    def getkey():
        return msvcrt.getch()

except:
    import sys
    import tty
    import termios

    def getkey():
        """Wait for a keypress and return a single character string."""
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch

print("Press any key to exit...")
getkey()