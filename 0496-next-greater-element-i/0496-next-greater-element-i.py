class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        d={}
        for i in range(len(nums2)-1,-1,-1):
            while st and st[-1]<=nums2[i]:
                st.pop()
            if len(st)==0:
                st.append(nums2[i])
                if nums2[i] in nums1:
                    d[nums2[i]]=-1
            else:
                if nums2[i] in nums1:
                    d[nums2[i]]=st[-1]
                st.append(nums2[i])
        ans=[]
        for i in range(len(nums1)):
            ans.append(d[nums1[i]])
        return ans
        