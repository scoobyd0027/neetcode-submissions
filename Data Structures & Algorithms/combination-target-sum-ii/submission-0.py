class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        candidates.sort()

        def backtrack(i, total, cur):
            nonlocal candidates, target, subsets
            if total > target: return 
            if total == target:
                subsets.append(cur.copy())
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue 

                if total + candidates[j] > target:
                    return
                
                cur.append(candidates[j])
                backtrack(j + 1, total + candidates[j], cur)
                cur.pop()

        backtrack(0, 0, [])
        return subsets

