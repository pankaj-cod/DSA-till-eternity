class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        Sum = int(a,2)+int(b,2)
        return bin(Sum)[2:]
