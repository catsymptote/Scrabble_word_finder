class Dictionary:
    word_list = []
    word_list_all = []

    illegal_characters = [
        ' ', '-', '\'', '\"',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]

    dictionary_file = "dictionary\\words.txt"


    def __init__(self, fname = None):
        if(fname):
            self.dictionary_file = fname

        self.load_words()


    def load_words(self):
        with open(self.dictionary_file) as dic:
            self.word_list = dic.readlines()
        print(self.word_list)


    def purge_words(self):
        pass
