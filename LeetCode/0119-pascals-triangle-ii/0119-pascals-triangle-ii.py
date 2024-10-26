class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[1]]

        if rowIndex == 0:
            return rows[0]

        for i in range(1, rowIndex+1):
            prev_row = rows[i-1]
            current_row = [1]

            for j in range(1, i):
                current_row.append(prev_row[j-1] + prev_row[j])
            
            current_row.append(1)
            rows.append(current_row)
        
        return rows[rowIndex]