class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(current_sum, path, start):
            if current_sum == target:
                # current_sum이 target과 같으면 유효한 조합이므로 결과에 추가
                result.append(list(path))
                return
            elif current_sum > target:
                # current_sum이 target을 초과하면 더 이상 진행할 필요 없음
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])  # 현재 숫자를 조합에 추가
                backtrack(current_sum + candidates[i], path, i)  # 재귀 호출
                path.pop()  # 백트래킹: 마지막에 추가한 숫자를 제거
                
        backtrack(0, [], 0)  # 초기 current_sum을 0으로 시작
        return result
