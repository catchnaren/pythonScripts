import os
#from operator import itemgetter

#For the given folder, print all the file name and file size in asc order by file size.
def lsFolder(path):
    #Get the path to the directory and pass it as an argument to the path parameter
    ls = os.listdir(path)
    lis = []
    for i in ls:
        sz = os.path.getsize(i)
        string = 'File name: ' + i + ' ,File size: ' + str(sz)
        #print string
        div = string.split()
        lis.append(div)
    #tup = tuple(lis)
    #print tup
    sor = sorted(lis, key = lambda lis: int(lis[-1]))
    print sor
    count = 1
    for item in sor:
        #print str(count)+ ' : ' + '{}'.format(item)
        count += 1

def main():
    try:
        filePath = raw_input('Enter the Folder path: ')
        formattedPath = filePath.replace('//', '/')
        lsFolder(formattedPath)

    except:
        print 'File path cannot be found: ', filePath

if __name__ == '__main__':
    main()
