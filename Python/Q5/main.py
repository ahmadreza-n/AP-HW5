import os
import re


def getInput(prog):
    commandList = []
    inputMessage = "Enter your command, type quit or exit to exit: \n"
    while len(commandList) != 3:
        inputStr = input(inputMessage)
        if(inputStr == 'quit' or inputStr == 'exit'):
            return ['quit', None, None]
        temp = prog.match(inputStr)
        if temp is None:
            inputMessage = "wrong format, please try again\n"
        else:
            commandList = list(temp.groups())

    if len(commandList[2]) == 0:
        commandList[2] = os.getcwd()

    return commandList


def find(name, path):
    result = []
    for root, _, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


pattern = r'(.+)\((.+), *(.*)\)'  # input format
prog = re.compile(pattern)

while(True):
    [command, name, path] = getInput(prog)
    if command == 'quit':
        break

    if command == 'create_dir':
        try:
            os.mkdir(os.path.join(path, name))  # creating new directory
        except OSError:
            print(f"Creation of the directory {name} in {path} failed")
        else:
            print(f"Successfully created the directory {path}")

    elif command == 'create_file':
        try:
            os.mknod(os.path.join(path, name))  # creating new file
        except OSError:
            print(f"Creation of the file {name} in {path} failed")
        else:
            print(f"Successfully created the file {name} in {path}")

    elif command == 'delete':
        try:
            os.remove(os.path.join(path, name))  # removing exsisting file
        except OSError:
            print(f"Deletion of the file {name} in {path} failed")
        else:
            print(f"Successfully deleted the file {name} in {path}")

    elif command == 'find':
        try:
            result = find(name, path)  # finding existing file
        except OSError:
            print(f"Finding of the file {name} failed")
        else:
            print(f"Successfully found the file(s) {name}")
            print(result)

    else:
        print("No such command")
