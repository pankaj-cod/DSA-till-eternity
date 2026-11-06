class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashi = {}
        alphas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in sentence:
            if i in hashi:
                hashi[i]+=1
            else:
                hashi[i]= 1
        
        for let in alphas:
            if let not in hashi:
                return False
        
        return True
