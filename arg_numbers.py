import argparse
parser = argparse.ArgumentParser()
# positional
parser.add_argument("a", type = int, help = "first argument")
parser.add_argument("b", type = int, help = "second argument")
parser.add_argument("-a", "--action" , help = "You can summirize or find square value", required = True)
args = parser.parse_args()
print(args)

def summarize(a,b):
    print("The sum of the numvers are ", a + b)

def square(a,b):
    print("The square of the first number is ", a**2, "The square of the second number is ", b**2)

if args.action == "sum":
    summarize(args.a, args.b)
elif args.action == "square":
    square(args.a, args.b)
