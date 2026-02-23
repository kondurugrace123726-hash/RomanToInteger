"""Problem: Roman to Integer
Given a Roman numeral string, convert it to an integer.
Rules:
- If a smaller value appears before a larger value, subtract it.
- Otherwise, add it.
Time Complexity: O(n)
Space Complexity: O(1)"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 
            'V': 5,
            'X': 10, 
            'L': 50,
            'C': 100, 
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):
            current_value = roman_map[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        return total
        
if __name__ == "__main__":
    sol = Solution()
    examples = ["III", "IV", "IX", "LVIII", "MCMXCIV"]

    for roman in examples:
        print(f"{roman} -> {sol.romanToInt(roman)}")

    user_input = input("\nEnter a Roman numeral to convert: ").upper()
    if user_input:
        print(f"{user_input} -> {sol.romanToInt(user_input)}")
        
