"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    
    def __init__(selt, path):
        dict_file = open(path)
        self.words = set.parse(dict_file)

    def parse(self, dict_file):
        return[w.strip (for w in dict_file)]

    def random(self):
        return random.choice(self.words)

class SWF(WordFinder):
    def parse(self, dict_file):
        
        return [w.strip(for w in dict_file)
            if w.strip() and not w.startswith("#")]

