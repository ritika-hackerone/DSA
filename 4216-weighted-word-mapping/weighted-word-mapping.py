class Solution(object):
    def mapWordWeights(self, words, weights):
        d={25:'a',24:'b',23:'c',22:'d',21:'e',20:'f',19:'g',18:'h',17:'i',16:'j',15:'k',14:'l',13:'m',12:'n',11:'o',10:'p',9:'q',8:'r',7:'s',6:'t',5:'u',4:'v',3:'w',2:'x',1:'y',0:'z'};
        temp=[];
        for i in words:
            t=0;
            for c in i:
                t+=weights[ord(c)-ord('a')];
            t%=26;
            temp.append(d[t]);
        return "".join(temp)
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        