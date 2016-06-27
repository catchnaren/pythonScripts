#get the input file
def fileLoader():
    fname = raw_input('Enter the file name: ')
    try:
        global fhand
        fhand = open(fname)
    except:
        print 'File cannot be opened: ', fname
        exit()

#To find integers from a file
def intFromFile():
    inp = [int(i) for i in fhand.read().split() if i.isdigit()]
    #print inp
    for x in inp:
        print str(x) + ' is an integer'

#To reverse strings from a file
def stringRevFromFile():
    inp = [str(s) for s in fhand.read().split() if not s.isdigit()]
    #print inp
    for y in inp:
        print y[::-1]

#if the word in the file is an int, print the word, eg: '1 is an int'
def intFinder():
    for line in fhand:
        string = line
        ls = list(string)
        for i in ls:
            if type(ls[i]) == int:
                print ls[i] + ' is an interger'

#if not an int, print the word in reverse order.
def notIntReverse():
    for line in fhand:
        string = line.split()
        for i in string:
            if type(string[i]) == str:
                print string[i][::-1]

#comment out the functions based on the need, default: Runs the fileLoader() and intFromFile() functions
def main():
    fileLoader()
    intFromFile()
    #stringRevFromFile()
    #intFinder()
    #notIntReverse()

if __name__ == '__main__':
    main()
