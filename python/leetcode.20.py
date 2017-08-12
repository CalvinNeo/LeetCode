class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for x in s:
            try:
                if x == '}':
                    if st.pop() != '{':
                        return False
                elif x == ']':
                    if st.pop() != '[':
                        return False
                elif x == ')':
                    if st.pop() != '(':
                        return False
                else:
                    st.append(x)
            except:
                return False
        if len(st) == 0:
            return True
        else:
            return False
sln = Solution()
print sln.isValid("[][()][]")
print sln.isValid("")
print sln.isValid("]")
print sln.isValid("([)")
    