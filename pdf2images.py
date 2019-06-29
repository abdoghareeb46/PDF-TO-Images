# Import libraries
from pdf2image import convert_from_path
from os import listdir
from os.path import isfile, join

#list out PDF files in the directory
mypath='/home/abdo/Desktop/input/'
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
        page.save("/home/abdo/Desktop/output/"+str(join(mypath,onlyfiles[n]).split("/")[-1])+image_name, 'JPEG')
        image_counter = image_counter + 1
# After conversion print Done
print("Done")
