import argparse
parser = argparse.ArgumentParser()
# positional
parser.add_argument("description"  action = "store", default = "the input file is roses.txt", nargs = "+", help = "adding element to the list of roses type")
f = open('roses.txt', "a", encoding='utf-8') # the file contains list of roses types
my_file = open("roses.update.txt", "w+")
if "input_file" == "roses.txt":
    with open('roses.txt') as f: # converting each line into a list and picking the necessary element
        lines = f.readlines()
        e = lines[1] 
        print(e)
    my_file.write ( e)
else:
    print("Please specify the file")
    

args = parser.parse_args()
print(vars(args))
