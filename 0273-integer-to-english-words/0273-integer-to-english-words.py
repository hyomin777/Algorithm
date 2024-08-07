class Solution:
    converter = {
        1: ["One", "Ten"],
        2: ["Two", "Twenty"],
        3: ["Three", "Thirty"],
        4: ["Four", "Forty"],
        5: ["Five", "Fifty"],
        6: ["Six", "Sixty"],
        7: ["Seven", "Seventy"],
        8: ["Eight", "Eighty"],
        9: ["Nine", "Ninety"],
        10: ["Ten", "Ten"],
        11: ["Eleven", "Eleven"],
        12: ["Twelve", "Twelve"],
        13: ["Thirteen", "Thirteen"],
        14: ["Fourteen", "Fourteen"],
        15: ["Fifteen", "Fifteen"],
        16: ["Sixteen", "Sixteen"],
        17: ["Seventeen", "Seventeen"],
        18: ["Eighteen", "Eighteen"],
        19: ["Nineteen", "Nineteen"]
    }

    unit_num = {
        1: "Thousand",
        2: "Million",
        3: "Billion",
        4: "Trillion"
    }

    def group_num_by_three_digits(self, num: int) -> List[str]:
        groupped_nums = []
        num_str = str(num)

        for i in range(len(num_str), 0, -3):
            start = max(i - 3, 0)
            groupped_num = num_str[start:i]
            if groupped_num:
                groupped_nums.append(groupped_num)

        return groupped_nums

    def three_digits_to_words(self, num_str: str) -> str:
        num = int(num_str)
        if num == 0:
            return ""

        words = []
        if num >= 100:
            words.append(self.converter[num // 100][0])
            words.append("Hundred")
            num %= 100

        if num >= 20:
            words.append(self.converter[num // 10][1])
            num %= 10

        if 0 < num < 20:
            words.append(self.converter[num][0])

        return " ".join(words)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        groupped_nums = self.group_num_by_three_digits(num)
        output = []

        for i in range(len(groupped_nums)):
            group_words = self.three_digits_to_words(groupped_nums[i])
            if group_words:
                if i > 0:
                    group_words += " " + self.unit_num[i]
                output.append(group_words)

        return " ".join(reversed(output))