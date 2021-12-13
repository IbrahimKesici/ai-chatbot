from typing import List

import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np


class NLPEngine():
    
    def __init__(self, stemmer: object = None) -> None:
        self._stemmer = stemmer or PorterStemmer()
    
    def vectorize_sentence(self, sentence: str, words_map:List[str]) -> List[int]:
        tokens = self.tokenize(sentence)
        words = [self.get_stem(token.lower()) for token in tokens if token.isalnum()]

        cleaned_words_map = [self.get_stem(word_map.lower()) for word_map in words_map if word_map.isalnum()]
        vector = self.map_words(words, cleaned_words_map)
        
        return vector

    def tokenize(self, sentence: str) -> List[str]:
        return nltk.word_tokenize(sentence)
    
    def get_stem(self, word: str) -> str:
        return self._stemmer.stem(word)
    
    def map_words(self, words: List[str], words_map: List[str]) -> List[int]:
        vector = np.zeros(len(words_map), dtype=int)
        for idx, word in enumerate(words_map):
            if word in words:
                vector[idx] = 1
        
        return vector
        
        
        
    
     