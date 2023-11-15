class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence
        self.tokens = self.sentence.split()
        self.word_count = 0

    def count_words(self):
        self.word_count = len(self.tokens)

    def get_word_count(self):
        return self.word_count
    
    def get_shortest_word(self):
        min = len(self.tokens[0])
        for token in self.tokens:
            if(len(token) < min):
                min = len(token)
        return min

    def get_longest_word(self):
        max = len(self.tokens[0])
        for token in self.tokens:
            if(len(token) > max):
                max = len(token)
        return max
