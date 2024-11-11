def decode_message(s: str, p: str) -> bool:
    # Initialize the DP table
    dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
    dp[0][0] = True  # Empty pattern matches empty string

    # Fill in the first row where pattern has '*'
    for i in range(1, len(p) + 1):
        if p[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
    
    # Fill the rest of the DP table
    for i in range(1, len(p) + 1):
        for j in range(1, len(s) + 1):
            if p[i - 1] == '*':
                # Star can match zero or more characters
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                # Match single character or question mark
                dp[i][j] = dp[i - 1][j - 1]

    # Result is in the bottom-right corner of the table
    return dp[len(p)][len(s)]

# Example usage
print(decode_message("aa", "a"))     # Output: False
print(decode_message("aa", "*"))     # Output: True
print(decode_message("cb", "?a"))    # Output: False
print(decode_message("abc", "?b?")) # Output: True
print(decode_message("acdcb", "a*c?b")) # Output: False
