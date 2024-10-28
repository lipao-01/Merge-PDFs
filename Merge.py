import PyPDF2 # tool for manipulate pdfs
import os # manipulate pc files, read files from a folder

merger = PyPDF2.PdfMerger() # merger files

list_files = os.listdir("Files") # show files in a folder
list_files.sort() # sort files in a folder
print(list_files)

for file in list_files: # explore file in list
    if ".pdf" in file: # check if the file is PDF
        merger.append(f"Files/{file}") # add the file you are reading to the merge


merger.write("PDF FINAL.pdf") # creat pdf end
