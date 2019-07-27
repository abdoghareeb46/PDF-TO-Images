# Import libraries
from pdf2image import convert_from_path
from os import listdir
from os.path import isfile, join
import sys


if len(sys.argv) <= 2:
  print("Command should be like: python pdf2imags.py input/directory output/directory")
elif len(sys.argv)>=4:
    print("You should eneter Two values INPUT and OUTPUT directory")
    print("Command should be like: python pdf2imags.py input/directory output/directory")
else:
    mypath =sys.argv[1]
    outpath=sys.argv[2]
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f))]
    # GO through PDF files and create images from these files
    print("IF you have many files, it's going to take a while........")

    for n in range(0, len(onlyfiles)):
        # get number of pages in each document
        print("File Name: ",join(mypath,onlyfiles[n]))
        pages = convert_from_path(join(mypath,onlyfiles[n]), 500)
        # set image counter to 1
        image_counter = 1
        for page in pages:
            # Convert each page in the PDF file into .JPEG Image
            image_name = "page_"+str(image_counter)+".JPEG"
            # Save every image with it's number concatenated with PDF File Name
            page.save(outpath+str(join(mypath,onlyfiles[n]).split("/")[-1])+image_name, 'JPEG')
            image_counter = image_counter + 1
    # After conversion print Done
    print("Done")
