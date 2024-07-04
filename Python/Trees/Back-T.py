class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        arr = []

        return self.hasPathHelper(root, arr, targetSum)
    
    def hasPathHelper(self, root, arr, target) -> bool:
        if not root:
            return False
        
        arr.append(root.val)
        
        if not root.right and not root.left:
            s = sum(arr)
            if s == target:
                return True
            else:
                arr.pop()
                return False

        if self.hasPathHelper(root.right, arr, target):
            return True
        if self.hasPathHelper(root.left, arr, target):
            return True
            
        arr.pop()
        return False
    




    # one for all of the subsets

    class Solution:
        def subsets(self, nums: List[int]) -> List[List[int]]:
            res = []

            subset = []
            def dfs(i):
                if i >= len(nums):
                    res.append(subset[:])
                    return
                
                subset.append(nums[i])
                dfs(i+1)

                subset.pop()
                dfs(i+1)
            
            dfs(0)
            return res
        



    
    """
    Backtracking with digits.

    This has O(n4^n) time complecity and O(n) space complexity (n for the number of stacks and n for the response).
    """


    def letterCombinations(self, digits: str) -> List[str]:

        mapping = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        res = []

        if not digits:
            return res

        lets = []
        def dfs(i):
            if i >= len(digits):
                s = "".join(lets)
                res.append(s)
                return
            
            p = mapping[digits[i]]
            for l in p:
                lets.append(l)
                dfs(i+1)
                lets.pop()

        dfs(0)
        return res