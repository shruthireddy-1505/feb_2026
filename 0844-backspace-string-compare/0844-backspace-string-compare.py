class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(val):
            st=[]
            for i in val:
                if i=="#":
                    if st:
                        st.pop()
                else:
                    st.append(i)
            
            return "".join(st)
        return backspace(s)==backspace(t)
    
