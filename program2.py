def decode_message(s: str, p: str) -> bool:
    memo = {}

    def match(i, j):
        # Check if we've already computed the result for this state
        if (i, j) in memo:
            return memo[(i, j)]
        
        # If we reach the end of both the message and pattern, it's a match
        if i == len(s) and j == len(p):
            return True
        # If we reach the end of the pattern but not the message, it's not a match
        if j == len(p):
            return False
        
        # If the pattern contains '*'
        if p[j] == '*':
            # '*' can match zero characters or one/more characters in `s`
            match_result = match(i, j + 1) or (i < len(s) and match(i + 1, j))
        else:
            # Match single character or '?'
            match_result = i < len(s) and (p[j] == s[i] or p[j] == '?') and match(i + 1, j + 1)
        
        # Store result in memoization table
        memo[(i, j)] = match_result
        return match_result

    # Start matching from the beginning of both the message and pattern
    return match(0, 0)

# Example usage
print(decode_message("aa", "a"))     # Output: False
print(decode_message("aa", "*"))     # Output: True
print(decode_message("cb", "?a"))    # Output: False
print(decode_message("adceb", "*a*b")) # Output: True
print(decode_message("acdcb", "a*c?b")) # Output: False
