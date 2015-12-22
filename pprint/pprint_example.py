import pprint

def main():
    stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
    stuff.insert(0, stuff[:])
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(stuff)

if __name__ == "__main__":
    main()
