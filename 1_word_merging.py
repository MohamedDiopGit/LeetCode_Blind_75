class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        

        merged_string = ""

        length_1 = len(word1)
        length_2 = len(word2)

        tail = ""
        
        if len(word1)>len(word2):
            tail = self.get_tail(word=word1,sizeOtherWord=length_2)
        elif len(word1) < len(word2):
            tail = self.get_tail(word=word2,sizeOtherWord=length_1)
        

        #Process for merging here
        maxSizeToRead =  min(length_1,length_2)
        for i in range(0,maxSizeToRead):

            merged_string += word1[i] + word2[i]


        merged_string += tail

        return merged_string
    
    def get_tail(self,word,sizeOtherWord):
        tail = word[sizeOtherWord:] #cut the word just at n=sizeOtherWord index

        return tail


if __name__ == "__main__":
    solution = Solution()
    print(solution.mergeAlternately("abc", "defg")) # Output: "aebfcgd"
    print(solution.mergeAlternately("abcdef", "ghijkl")) # Output: "aebfcgdhijkl"
    print(solution.mergeAlternately("abc", "def")) # Output: "aebfcgd"