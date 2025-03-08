import sys


def main():
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            contents = file.readlines()
        lines = contents[:]
        loc = []
        for line in lines:
            if not (line.lstrip().startswith(("'", "#", "\""))):
                loc.append(line)
        print(len(loc))
    else:
        print("something is wrong")
