from lib import dictionary



class WordFinder:
    dic = dictionary.Dictionary()
    #print(dic.get_dic())

    chars = "aaabcdefg"
    min = 0
    max = 0
    length = 0



    def find_words(self):
        words = self.dic.get_dic()
        relevant_words = []
        matches = 0
        #for i in range(len(words)):
        for i in range(10):
            if(self.word_is_yay(words[i])):
                matches += 1
                relevant_words.append(words[i])
        print(matches)


    def word_is_yay(self, word):
        match = False
        if self.consists_of(word):
            print("A match")
            match = True

        print("Not a match")
        print()
        return match


    def consists_of(self, word):
        #word = "abcd"
        characters = self.chars

        print(word)
        print(characters)

        runs = 0


        ##### REWRITE THIS SHITTY SHIT!
        x = -1
        while(x < len(word) -2):
            remove_pair = False
            x += 1
            y = -1
            while(y < len(characters) -2):
                y += 1
                print("Runs: " + str(runs))
                runs += 1
                #word_ind = word[x]
                #characters_ind = characters[y]
                if(len(word) == 0):
                    #print("len word 0")
                    return True
                elif(len(word) > 0 and len(characters) == 0):
                    #print("len chars 0")
                    return False
                elif(word[x] == characters[y]):
                    remove_pair = True
                    continue

            if(remove_pair):
                word = word[:x] + word[x + 1:]
                characters = characters[:y] + characters[y + 1:]
                x -= 1
                y -= 1




        #print("other")
        if(len(word) == 0):
            return True
        return False




findr = WordFinder()
findr.find_words()
