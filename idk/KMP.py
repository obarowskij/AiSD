def compute_lps_array(pattern):
    lps = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1

        lps[i] = j

    return lps


def kmp(pattern, text):
    if not pattern or not text:
        return []

    lps = compute_lps_array(pattern)
    indices = []
    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == len(pattern):
            indices.append(i - j + 1)
            j = lps[j - 1]

    return indices

pattern = "abra"
text = "abrakadabra"
print(kmp(pattern, text))
