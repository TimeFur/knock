import os

def openfolder(path):
    os.startfile(path)
    
def main():
    print "Knock center"
    openfolder("D:")
    
if __name__ == "__main__":
    main()
