class WordSuggestion:
    def __init__(self, keyword, after_words, counts):
        self.keyword = keyword
        self.after_words = after_words
        self.counts = counts

        if len(self.after_words) == 1:
            self.suggestions = [self.after_words[0], 'of', 'the']
        elif len(self.after_words) == 2:
            self.suggestions = [self.after_words[0], 'of']
        else:
            self.suggestions = after_words[0:3]

    def __repr__(self):
        return "Key = {0}. Suggestions: {1}, {2} and {3}".format(self.keyword, self.suggestions[0],
                                               self.suggestions[1], self.suggestions[2])

    def show_suggestions(self):
        return "Press: [1] {} [2] {} [3] {}  [Q]uit".format(self.suggestions[0], self.suggestions[1],
                                             self.suggestions[2])

