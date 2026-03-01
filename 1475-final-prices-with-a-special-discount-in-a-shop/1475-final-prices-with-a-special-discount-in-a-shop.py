class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st=[]
        res=[]
        for i in range(len(prices)-1,-1,-1):
            while st and st[-1]>prices[i]:
                st.pop()
            if len(st)==0:
                st.append(prices[i])
                res.append(prices[i])
            else:
                res.append(prices[i]-st[-1])
                st.append(prices[i])
        return res[::-1] 