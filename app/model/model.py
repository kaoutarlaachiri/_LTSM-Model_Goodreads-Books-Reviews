import tensorflow as tf
from pathlib import Path
import string
from keras_preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import numpy as np


# The maximum number of words to be used. (most frequent)
MAX_NB_WORDS = 10000
# Max number of words in each complaint.
MAX_SEQUENCE_LENGTH = 250



BASE_DIR = Path(__file__).resolve(strict=True).parent

loaded_model = tf.keras.models.load_model(r'app\model\saved_model')

def predict_rating(text):
    #preprocessing
    text = str(text)
    
    noise_removing(text)
    #tokenize text
    tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@^_`{|}~')
    tokenizer.fit_on_texts(text)
    text = tokenizer.texts_to_sequences(text)
    text = pad_sequences(text, maxlen=MAX_SEQUENCE_LENGTH)
    #predict
    ratings = [np.argmax(i) for i in loaded_model.predict(text)]
    ratings =max(set(ratings), key = ratings.count)
    ratings = int(ratings)
    



    return ratings

def noise_removing(text):
    # Lower case the review text
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
  




