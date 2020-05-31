class Dictionary(List):
    def __init__(self):
        self.reload_list()


    def reload_list(self):
        # Clear list.
        while len(self) > 0:
            del self[0]
        
        # Load list.
        words = 3 #load file here
        for word in words:
            self.append(word)


    def blank_search(self, search):
        """Assuming search is a string of blank letters only."""
        results = []
        for word in self:
            if len(word) == len(search):
                results.append(word)
        return results


    def is_partial_match(self, search):
        """Should match "ab**t" to "about" (and maybe more)."""
        for word in self:
            if len(word) == len(search):
                for i in range(len(word)):
                    if search[i] != "*":
                        if search[i] != word[i]:
                            return False

            if len(word) >= len(search):
                pass

    
    def is_match(self, search):
        if search in self:
            # Is perfect match.
            return True
        elif self.is_partial_match(search):
            # Imperfect match.
            return True
        else:
            # Not a match.
            return False


    def search(self, search_phrase):
        """Find all words fitting. Reduce based on length. Sort by score."""


    def check_word(self, word):
        if self.is_match(word):
            return True
        return False
