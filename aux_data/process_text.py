# Process the text and save it

import pandas as pd
import numpy as np
import os
import spacy
from spacy import displacy
import networkx as nx
import pdfplumber

def ner(file_name, start_page):
    """
    Function to process text from a pdf file (.pdf) using Spacy.
    
    Params:
    file_name -- name of a pdf file as string
    
    Returns:
    a processed doc file using Spacy English language model
    
    """
    nlp = spacy.load("en_core_web_sm")

    # Open the PDF file
    with pdfplumber.open(file_name.path) as pdf:
        # Extract the text content starting from the specified page
        book_text = ""
        for page in pdf.pages[start_page - 1:]:  # Adjust the page index to start from 0
            book_text += page.extract_text()

    # Perform NER on the text content
    book_doc = nlp(book_text)

    # Save the processed text to a file
    # output_file = file_name + "_processed.txt"  # Create a new file name
    # with open(output_file, "w", encoding="utf-8") as f:
    #     f.write(book_doc.text)
        
    return book_doc

# Load books
# Get all book files in the data directory
all_books = [b for b in os.scandir('books') if '.pdf' in b.name]
# Sort dir entries by name
all_books.sort(key=lambda x: x.name)
