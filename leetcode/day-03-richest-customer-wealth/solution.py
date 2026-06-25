class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        # for문을 돌며 각 리스트 안의 리스트 자료를 모두 합해서 최대값을 저장, 최종 출력?
        maxWealth = 0
        for account in accounts:
            total = 0
            for m in account:
                total += m
            
            if total > maxWealth:
                maxWealth = total
        
        return maxWealth