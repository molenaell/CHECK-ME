
# open file , creating another one and writing the chosen in first file info into the other file
f = open('roses.txt', "a", encoding='utf-8') # the file contains list of roses types
my_file = open("roses.update.txt", "w+")


with open('roses.txt') as f: # converting each line into a list and picking the necessary element
    lines = f.readlines()
    e = lines[0]
print(e)
my_file.write (e)

f.close()
my_file.close()
