# # your_project/your_code_files/data_preprocessing.py

# from datasets import Dataset
# import os

# def load_text_data(directory):
#     data = []
#     for filename in os.listdir(directory):
#         with open(os.path.join(directory, filename), 'r') as file:
#             data.append(file.read())
#     return data

# # Load articles
# articles = load_text_data('../cybersecurity_data/articles')

# # Convert to Hugging Face Dataset
# dataset = Dataset.from_dict({'text': articles})

# # Save the processed dataset
# dataset.save_to_disk('../cybersecurity_data/processed_dataset')

import fitz  # PyMuPDF
from langchain_community.document_loaders import BaseLoader

class PDFLoader(BaseLoader):
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        # Open the PDF file
        doc = fitz.open(self.file_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        return text

# Example usage:
loader = PDFLoader('D:/FYP/fyp/Project/cybersecurity_data/articles/article_1.pdf')
text = loader.load()
print(text)  # To see the extracted text
