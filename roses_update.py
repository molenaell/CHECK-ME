
import argparse
parser = argparse.ArgumentParser()
# positional
parser.add_argument("f", default = "roses.txt", nargs = '?' , help = " file path with the list of elements")
parser.add_argument("nf", default = "rose_update.txt", nargs = '?',  help = "adding element to the list")
parser.add_argument("-a", "--action" , action = "store_true", help = "Add ", default = "creat" )
args = parser.parse_args()

print(args.f)
print(args.nf)

def creat(f, nf):
    # file = open(f, "a", encoding='utf-8') # the file contains list of roses types
    file = open(f, "a", encoding='utf-8') # the file contains list of roses types
    nf = open(nf, "w+")
    with open(f) as file: # converting each line into a list and picking the necessary element
        lines = file.readlines()
        e = lines[1]
        nf.write(e)    
        print(e)
if args.action == "creat":
    creat(args.f, args.nf)   
