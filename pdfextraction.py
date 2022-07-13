# importing required modules
import PyPDF2
import glob
import re


def pdfextraction():
    """
    Program creates text files for each PDF in a folder CourseMaterials (not included)
    in another folder called Materials (not included)
    
    Modifyed excerpt for use of PyPDF2 from https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
    and StackOverflow for use of Glob https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder
    and Introduction to Computer Science using Python, page 294
    and this https://programminghistorian.org/lessons/working-with-text-files
    and this https://github.com/jalan/pdftotext
    and this https://stackoverflow.com/questions/41668092/return-the-content-of-a-wildcard-match-in-python
    updated 7/13/2022 using https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/
    """
    
    for filename in glob.iglob('**/*.pdf'):
        print(filename)
        
        # creating a pdf file object
        with open(filename, 'rb') as pdfFileObj:
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
        # number of pages in pdf file
        numPages = pdfReader.numPages
    
        for page in pdfReader:
            file = open(str(filename) + '.txt','a')
    
            for line in page:
                file.write(line)
            
            file.close()
    return

#I am a cool

#Main

pdfextraction()


