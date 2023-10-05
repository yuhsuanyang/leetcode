# no. 676
class MagicDictionary(object):
    def __init__(self):
        return
                    

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        self.word_len = {i: [] for i in range(1, 101)}
        for word in dictionary:
            self.word_len[len(word)].append(word)
                                                            

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        candidates = self.word_len[len(searchWord)]
        if candidates == []:
            return False
        else:
            for word in candidates:
                if self.similarity(searchWord, word):
                    return True
            return False

    def similarity(self, word1, word2):
        assert len(word1) == len(word2), 'word1 and word2 must have same length' 
        diff = 0
        word_length = len(word1)
        for i in range(word_length):
            if word1[i] != word2[i]:
                diff += 1
            if diff >= 2:
                return False
        return diff 
    


dict_words = ['hello', 'hallo', 'leetcode']
search_words = ['hello', 'hhllo', 'hell', 'leetcoded']
solution = MagicDictionary()
solution.buildDict(dict_words)
for word in search_words:
    print(solution.search(word))
