# file_reader = open("python.png", "rb")
# file_writer = open("python-copy.png", "wb")

# # while True:
# #     byte = file_reader.read(1)
# #     if not byte:
# #         break
# #     file_writer.write(byte)

# file_writer.write(file_reader.read())

# file_reader.close()
# file_writer.close()

# print("File Copied...")

# -----------------------------

import shutil
from pathlib import Path

source_path = Path.home() / "Desktop" / "python.png"
print(source_path)
shutil.copy("python.png", "python-copy2.png")
print("File Copied...")
