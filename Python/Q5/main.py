import os


def getInput():
    while(True):
        inputStr = input("Enter your command, type quite or exit to exit: \n")
        if(inputStr == 'quite' or inputStr == 'exit'):
            raise Exception("Good Bye")
        inputStr = inputStr.split('(')
        if(len(inputStr) != 2):
            print("wrong format")
        else:
            command = inputStr[0]
            temp = inputStr[1].split(',')
            if(len(temp) != 2):
                print("wrong format")
            else:
                path = temp[1][:-1] + '/' + temp[0]
                if(len(temp[1][:-1]) == 0):
                    path = path[1:]
                return [command, path]


while(True):
    try:
        [command, path] = getInput()
        print(command, path)
    except:
        break

    if command == 'create_dir':
        try:
            os.mkdir(path)
        except OSError:
            print(f"Creation of the directory {path} failed")
        else:
            print(f"Successfully created the directory {path}")
    elif command == 'create_file':
        try:
            os.mknod(path)
        except OSError:
            print(f"Creation of the file {path} failed")
        else:
            print(f"Successfully created the file {path}")
    elif command == 'delete':
        try:
            print(path)
            os.remove(path)
        except OSError:
            print(f"Deletion of the file {path} failed")
        else:
            print(f"Successfully deleted the file {path}")
    elif command == 'find':
        try:
            pass
        except OSError:
            print(f"Creation of the directory {path} failed")
        else:
            print(f"Successfully created the directory {path}")
    else:
        print("wrong format")
