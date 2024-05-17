import sys

def pattern_count(text: str, pattern: str) -> int:
    count = 0
    string_length = len(text)
    pattern_length = len(pattern)
    for i in range(string_length-pattern_length+1):
        if text[i:i+pattern_length] == pattern:
            count += 1
    return count
