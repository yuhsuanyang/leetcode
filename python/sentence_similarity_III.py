#no. 1813
class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        sentence1 = sentence1.split(' ')
        sentence2 = sentence2.split(' ')
        if len(sentence1) == 1 or len(sentence2) == 1:
            if sentence1[0] == sentence2[0] or sentence1[-1] == sentence2[-1]: 
                return True
            else:
                return False

        while len(sentence1) and len(sentence2):
            if sentence1[0] != sentence2[0] and sentence1[-1] != sentence2[-1]:
                # 頭尾都不一樣
                return False
            elif sentence1[0] == sentence2[0]: 
                # 頭一樣
                sentence1 = sentence1[1:]
                sentence2 = sentence2[1:]

            elif sentence1[-1] == sentence2[-1]:
                sentence1 = sentence1[:-1]
                sentence2 = sentence2[:-1]
        return True

solution = Solution()
print(solution.areSentencesSimilar("My name is Haley", "My Haley"))
print(solution.areSentencesSimilar("of", "A lot of words"))
print(solution.areSentencesSimilar("Eating right now", "Eating"))
