
# Imports
import nltk
import re # Regular expressions
import numpy as np
import pandas as pd
from pprint import pprint

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# spacy for lemmatization
import spacy

# Plotting tools
import pyLDAvis
import pyLDAvis.gensim # Don't skip this
import matplotlib.pyplot as plt
# %matplotlib inline # Uncomment if running in notebook

# Enable logging for gensim - optional
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR) 

# Ignore depreciation warnings 
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

print("Done.")

