def decode_message(s: str, p: str) -> bool:
    memo = {}

    def match(i, j):
        # Check if result is already computed
        if (i, j) in memo:
            return memo[(i, j)]

        # If we've reached the end of both the message and pattern, it's a match
        if i == len(s) and j == len(p):
            return True
        # If we've reached the end of the pattern but not the message, it's not a match
        if j == len(p):
            return False

        # Handle '*' in the pattern
        if p[j] == '*':
            # '*' can either match no characters in s or at least one character
            match_result = match(i, j + 1) or (i < len(s) and match(i + 1, j))
        else:
            # Match single character or ?
            match_result = i < len(s) and (p[j] == s[i] or p[j] == '?') and match(i + 1, j + 1)

        # Memoize and return the result
        memo[(i, j)] = match_result
        return match_result

    # Start matching from the beginning of both the message and pattern
    return match(0, 0)

# Take user input in a single line and split it into message and pattern
input_line = input(" ")
message, pattern = input_line.split()

# Check if the pattern matches the message and print the result
if decode_message(message, pattern):
    print("True")
else:
        print("False")