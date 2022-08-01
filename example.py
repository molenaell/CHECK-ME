f = open('roses.txt', "a", encoding='utf-8') # the file contains list of roses types
f.write ("\nOld garden roses\n")
f.write ("Modern garden roses\n")
f.close()

with open('roses.txt') as f: # converting each line into a list and picking the necessary element
    lines = f.readlines()
    e = lines[0]
print(e)

