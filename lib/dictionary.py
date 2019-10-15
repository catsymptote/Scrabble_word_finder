class Dictionary:
    full_dic = []
    dic = []

    full_dictionary_file = "dictionary\\full_dictionary.txt"
    dictionary_file = "dictionary\\used_dictionary.txt"

    illegal_characters = [
        ' ', '-', '\'', '\"', '.', ',', '&', '/',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    max_word_length = 11



    def __init__(self, fname = None):
        if(fname):
            self.full_dictionary_file = fname


    def load_full_dic(self):
        with open(self.full_dictionary_file) as dic_file:
            self.full_dic = dic_file.readlines()
        #print(self.full_dic)


    def load_dic(self):
        # Add: if file does not exist?
        with open(self.dictionary_file) as dic_file:
            self.dic = dic_file.readlines()

        print(len(self.dic))
        for i in range(len(self.dic)):
            self.dic[i] = self.dic[i].replace('\n', '')
        #print(self.dic)


    ##  Get the full dictionary.
    def get_full_dic(self):
        if not self.full_dic:
            self.load_full_dic()
        return self.full_dic

        ##  Get the using dictionary.
    def get_dic(self):
        if not self.dic:
            self.load_dic()
        return self.dic


    ##  Check if string includes illegal characters.
    def includes_illegal_char(self, word):
        for i in range(len(self.illegal_characters)):
            if self.illegal_characters[i] in word:
                return True
        return False



    ##  Gets words from full dictionary and put them in another list.
    def make_dic(self):
        # If list is empty: create/load list.
        if not self.full_dic:
            self.load_full_dic()

        # Copy full list.
        self.dic = self.full_dic
        dic_size = len(self.dic)
        
        # Exclude words of length > 11 and words including illegal characters.
        index = 0
        while(index < dic_size):
            # Remove '\n'.
            self.dic[index] = self.dic[index].replace('\n', '')

            # Exclude illegal character words.
            if(self.includes_illegal_char(self.dic[index])):
                del self.dic[index]
                dic_size -= 1
            # Exclude too long words.
            elif(   len(self.dic[index]) > self.max_word_length
                    or len(self.dic[index]) < 2):
                del self.dic[index]
                dic_size -= 1
            # Increment index if element not removed.
            else:
                index += 1

        #print(len(self.dic))
        #print(len(self.full_dic))

        # Write file.
        f = open(self.dictionary_file, "w+")
        dic_string = ""
        for i in range(dic_size):
            f.write(self.dic[i].lower())
        f.close()
