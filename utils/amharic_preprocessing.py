# utils/amharic_preprocessing.py

import re
import nltk
from nltk.tokenize import word_tokenize

def normalize_amharic_text(text):
    """Normalize Amharic text by removing punctuation, extra spaces, and normalizing orthographic variations."""
    
    punctuation = ['።', '፣', '፤', '፥', '፦', '፧', '፨', '!', '?', '.', ',', ':', ';', '"', '“', '”']
    for p in punctuation:
        text = text.replace(p, '')
    
    # Keep only Amharic characters and spaces
    text = re.sub(r'[^ሀ-ፐ\s]', '', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def tokenize_amharic(text):
    """Tokenize Amharic text into words."""
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if len(token) > 1 and re.match(r'[ሀ-ፐ]', token)]
    
    return tokens

def preprocess_amharic_text(text):
    """Preprocess the Amharic text by tokenizing, normalizing, and handling linguistic features."""
    
    normalized_text = normalize_amharic_text(text)
    tokens = tokenize_amharic(normalized_text)
    
    return tokens
