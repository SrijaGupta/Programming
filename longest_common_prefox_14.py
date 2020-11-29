#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".
class Solution(object):
    def Twostrings(self,s1,s2):
            a = ""  
            c=min(s1,s2)
            for i in range(len(c)):
                if(s1[i]==s2[i]):
                    a=a+s1[i]
                else:
                    break
            return a
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if (len(strs)==1):
            return strs[0]
        prefix= self.Twostrings(strs[0],strs[1])
        strs = strs[2:]
        strs.insert(0,prefix)      
        return self.longestCommonPrefix(strs)
        
