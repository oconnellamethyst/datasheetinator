from glob import glob
from fnmatch import fnmatch

def superfluouslineremover():
    """
    Program that removes superfluous lines from the output text files
    from the pdf extraction module from pdfs taken from the Saint Paul College
    bookstore
    """
    finalfile = open('alltextbooks.txt','a')
    
    filenamelist = []
    for file in glob('Materials/*.txt'):
        filenamelist.append(file)

    filenamelist = sorted(filenamelist)
        
    for filename in filenamelist:
        with open(filename, 'r') as textFile:
            for line in textFile:
                if fnmatch(line,'*/*/*Course Materials*')\
                   or fnmatch(line,' Course Materials List*')\
                   or fnmatch(line,'http://www.saintpaulcollegebookstore.com/CourseMaterialsPrint.aspx*')\
                   or fnmatch(line,' Pricing Disclaimer*')\
                   or fnmatch(line,' Pricing is subject to change without notice.*')\
                   or fnmatch(line,' books. Pricing changes*')\
                   or fnmatch(line,' We make every effort to*'):
                    pass
                else:
                    finalfile.write(line)
    finalfile.close()
    return

# Main
superfluouslineremover()
