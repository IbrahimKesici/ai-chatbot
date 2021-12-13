from nlp_engine import NLPEngine

def main():
    sentence = "Hi, how are you doing?"
    words_map = ['Hi', 'there', 'doing']

    nlp_engine = NLPEngine()
    sentence_vector = nlp_engine.vectorize_sentence(sentence, words_map)

if __name__ == '__main__':
    main()