import os

#get the input file
def fileLoader():
    fname = raw_input('Enter the file name: ')
    try:
        global fhand, sz
        fhand = open(fname)
        sz = os.path.getsize(fname)
    except:
        print 'File cannot be opened: ', fname
        exit()
        
#chunk process
def fileReadChunk():
    if sz > 0:
        inp = sz/10000
        fhand.seek(100, 5000)
        print str(sz)
        print str(inp)
        print(fhand.read(int(inp)))

def main():
    fileLoader()
    fileReadChunk()

if __name__ == '__main__':
    main()
