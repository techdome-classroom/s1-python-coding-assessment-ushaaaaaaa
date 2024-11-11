def decode_message(s: str, p: str) -> bool:
    memo = {}

    def match(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(s) and j == len(p):
            return True
        if j == len(p):
            return False

        if p[j] == '*':
            match_result = match(i, j + 1) or (i < len(s) and match(i + 1, j))
        else:
            match_result = i < len(s) and (p[j] == s[i] or p[j] == '?') and match(i + 1, j + 1)

        memo[(i, j)] = match_result
        return match_result

    return match(0, 0)

input_line = input(" ")
message, pattern = input_line.split()

if decode_message(message, pattern):
    print("True")
else:
    print("False")
