import PyPDF2
import sys

#####
#This script combine PDFs
#Usage: run the script with pdf names as argument
#####

NEW_PDF_NAME = 'combined.pdf'
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(NEW_PDF_NAME)

pdf_combiner(inputs)