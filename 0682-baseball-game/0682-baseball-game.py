class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st=[]
        for i in ops:
            if len(st)>=2 and i=='+':
                temp=st[-1]+st[-2]
                st.append(temp)
            elif st and i=='D':
                temp=st[-1]*2
                st.append(temp)
            elif st and i=='C':
                st.pop()
            else:
                st.append(int(i))
        return sum(st)
