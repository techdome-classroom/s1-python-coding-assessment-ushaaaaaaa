def decode_message(s: str, p: str) -> bool:
    memo = {}

    def match(i, j):
        # Check if the result for this state is already computed
        if (i, j) in memo:
            return memo[(i, j)]
        
        # If both pattern and message are fully matched
        if i == len(s) and j == len(p):
            return True
        # If only pattern is exhausted but message is not
        if j == len(p):
            return False
        
        # If the pattern has '*'
        if p[j] == '*':
            # '*' can either match no characters or one/more characters in `s`
            match_result = match(i, j + 1) or (i < len(s) and match(i + 1, j))
        else:
            # Match single character with '?' or exact character match
            match_result = i < len(s) and (p[j] == s[i] or p[j] == '?') and match(i + 1, j + 1)
        
        # Save the result in the memoization table
        memo[(i, j)] = match_result
        return match_result

    # Start matching from the beginning of both the message and pattern
    return match(0, 0)

# Example usage
print(decode_message("aa", "a"))     # Expected: False
print(decode_message("aa", "*"))     # Expected: True
print(decode_message("cb", "?a"))    # Expected: False
print(decode_message("adceb", "*a*b")) # Expected: True
print(decode_message("acdcb", "a*c?b")) # Expected: False
