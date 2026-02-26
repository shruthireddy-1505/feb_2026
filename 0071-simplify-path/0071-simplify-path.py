class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path=path.split("/")
        st=[]

        for i in new_path:
            if i=="" or i==".":
                continue
            elif i=="..":
                if len(st)==0:
                    continue
                else:
                    st.pop()
            else:
                st.append(i)
        res="/".join(st)

        return "/"+res