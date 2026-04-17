#Longest substring having all same characters after k changes
def solution(s : str, k: int) -> int:
    frequency = dict()
    left = right = 0
    result = 0
    longest=''
    for ch in s:
        frequency[ch] = frequency.get(ch,0) + 1
        window_size = right - left + 1
        if window_size - max(frequency.values()) <= k:
            #window is valid
            if window_size > result:
                longest = s[left:right+1]
                result = max(result, window_size)
        else:
            #first decrement the frequency of left and then update left
            frequency[s[left]] -= 1
            left += 1
        right += 1
    return result, longest

if __name__ == "__main__":
    tests = [
        # (s, k, expected_length)
        ("bfjejwfwjg", 2, 4),   # basic case
        ("ababab", 2, 5),        # alternating, answer spans nearly full string
        ("aababba", 1, 4),       # classic leetcode case
        ("aaaa", 0, 4),          # all same, k=0
        ("abcde", 0, 1),         # all distinct, k=0 → only 1
        ("abcde", 4, 5),         # k covers entire string
        ("aabbcc", 2, 4),        # tie between dominant chars
        ("a", 0, 1),             # single char
        ("aaabbbccc", 3, 6),     # three equal groups, k=3
        ("zzzaaabbb", 2, 5),     # dominant block at start
    ]
    for s, k, expected in tests:
        length, substr = solution(s, k)
        status = "PASS" if length == expected else "FAIL"
        print(f"[{status}] s={s!r} k={k} → len={length} substr={substr!r} (expected {expected})")

