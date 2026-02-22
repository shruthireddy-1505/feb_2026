class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        if len(st)==1:
            return False

        for i in s:
            if (len(st)!=0) and ((i==")" and st[-1]=="(") or (i=="]" and st[-1]=="[") or (i=="}" and st[-1]=="{")):
                st.pop()
            else:
                st.append(i)
        if len(st)==0:
            return True
        else:
            return False