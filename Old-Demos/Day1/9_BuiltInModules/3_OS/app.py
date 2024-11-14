import os
# print(os.name)
# print(os.getcwd())

# os.mkdir('myDir')
# os.rename('myDir', 'someDir')
# os.rmdir('someDir')

# print(os.listdir("c:\\python27"))
# print(os.listdir())    # Current Dir

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for fname in myFiles:
    print(os.path.join(os.getcwd(), fname))
