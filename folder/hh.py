import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

def extract_text_from_txt_file(txt_path):
    text = ""
    with open(txt_path, 'r') as txt_file:
        data = txt_file.readlines()
        for txt in data :
            text += txt
             
    return text

def process_text(text):
    """Tokenize, stem, and lemmatize the extracted text."""
    # Tokenization
    tokens = word_tokenize(text)
    
    # Stemming and Lemmatization
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    
    stemmed_words = [stemmer.stem(word) for word in tokens]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
    
    return stemmed_words, lemmatized_words

# Specify the path to your PDF file
txt_file_path = "C:\\Users\\Danny\\.vscode-oss\\Scripts\\.Comp\\Scripts\\kalenjin.txt"  # Change this to your PDF file path


extracted_text = extract_text_from_txt_file(txt_file_path)


stemmed_words, lemmatized_words = process_text(extracted_text)


print("Stemmed Words:", stemmed_words)
print("Lemmatized Words:", lemmatized_words)
