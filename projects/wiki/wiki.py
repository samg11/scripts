import sys

import wikipedia

def main():
    summary = wikipedia.summary(sys.argv[1]) + '\n'
    sys.stdout.write(summary)



if __name__ == "__main__":
    main()