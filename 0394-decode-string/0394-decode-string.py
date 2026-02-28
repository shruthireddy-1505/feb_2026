class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for i in s:
            if i!="]":
                st.append(i)
            else:
                ch=""
                while st[-1]!="[":
                    ch=st.pop()+ch
                st.pop()
                    
                num=""  
                while st and st[-1].isdigit():
                    num=st.pop()+num
                temp=ch*(int(num))
                st.append(temp)
        res="".join(st)
        return res