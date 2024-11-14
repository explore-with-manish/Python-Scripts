# Create a code to copy file

# fileRead = open("python.png", "rb")
# fileWrite = open("python-copy.png", "wb")

# # while True:
# #     byte = fileRead.read(1)
# #     if not byte:
# #         break
# #     fileWrite.write(byte)

# fileWrite.write(fileRead.read())

# fileRead.close()
# fileWrite.close()

# print("File Copied...")

# ---------------------------------------------------------------------
# fileRead = open("python.png", "rb")
# fileWrite = open("python-copy.png", "wb")

# with open("python.png", "rb") as fileRead, open("python-copy.png", "wb") as fileWrite:
#     # while True:
#     #     byte = fileRead.read(1)
#     #     if not byte:
#     #         break
#     #     fileWrite.write(byte)

#     fileWrite.write(fileRead.read())

# print("File Copied...")


# ---------------------------------------------------------------------
import shutil
shutil.copy("python.png", "python-copy2.png")
print("File Copied...")
