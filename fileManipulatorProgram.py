import sys
import shutil

args = sys.argv
print(args)
l = len(args)
cmd = args[1]

if cmd == 'reverse':
    if l != 4:
        print('Error!')
        sys.exit()
    else:
        inputpath = args[2]
        outputpath = args[3]
        try:
            with open(inputpath) as f:
                contents = f.read()
            with open(outputpath, 'w') as f:
                f.write(contents[::-1])
        except FileNotFoundError:
            print('File not found error')
    
if cmd == 'copy':
    if l != 4:
        print('Error!')
        sys.exit()
    else:
        inputpath = args[2]
        outputpath = args[3]
        try:
            shutil.copy(inputpath, outputpath)
        except FileNotFoundError:
            print('File not found error')
        
if cmd == 'duplicate-contets':
    if l != 4:
        print('Error!')
        sys.exit()
    else:
        inputpath = args[2]
        n = args[3]
        try:
            with open(inputpath) as f:
                contents = f.read()
            for i in n:
                str = contents
                with open(inputpath, 'w') as f:
                    f.write(contents + str)
        except FileNotFoundError:
            print('File not found error')
    
elif cmd == 'replace-string':
    if l != 5:
        print('Error!')
        sys.exit()
    else:
        inputpath = args[2]
        try:
            with open(inputpath) as f:
                contents = f.read()
            with open(inputpath, 'w') as f:
                str = contents.replace('needle', 'newstring')
                f.write(str)
        except FileNotFoundError:
            print('File not found error')