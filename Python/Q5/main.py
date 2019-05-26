import os


def getInput():
    while(True):
        inputStr = input("Enter your command, type quit or exit to exit: \n")
        if(inputStr == 'quit' or inputStr == 'exit'):
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
                path = temp[1][:-1]
                if path.startswith(' '):
                    path = path[1:]
                name = temp[0]
                command = command.lower()
                return [command, path, name]


def find(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

if __name__ == "__main__":
    while(True):
        try:
            [command, path, name] = getInput()
            if(len(path) == 0):
                path = os.getcwd()
        except:
            break
        if command == 'create_dir':
            try:
                os.mkdir(path + '/' + name)
            except OSError:
                print(f"Creation of the directory {name} in {path} failed")
            else:
                print(f"Successfully created the directory {path}")
        elif command == 'create_file':
            try:
                os.mknod(path + '/' + name)
            except OSError:
                print(f"Creation of the file {name} in {path} failed")
            else:
                print(f"Successfully created the file {name} in {path}")
        elif command == 'delete':
            try:
                os.remove(path + '/' + name)
            except OSError:
                print(f"Deletion of the file {name} in {path} failed")
            else:
                print(f"Successfully deleted the file {name} in {path}")
        elif command == 'find':
            try:
                result = find(name, path)
            except OSError:
                print(f"Finding of the file {name} failed")
            else:
                print(f"Successfully found the file(s) {name}")
                print(result)
        else:
            print("wrong format")
