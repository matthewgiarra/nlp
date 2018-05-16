#!/bin/bash

# Activate the virtual environment
source activate nlp

# Download NLTK data
echo "Downloading NLTK data..."
python3 -c "import nltk; nltk.download('stopwords')"

# Download spacy data
echo "Downloading spacy data..."
python3 -m spacy download en

