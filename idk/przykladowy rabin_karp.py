def rabin_karp(pattern, text):
    if not pattern or not text:
        return []

    prime = 101
    pat_len = len(pattern)
    text_len = len(text)
    pat_hash = 0
    text_hash = 0

    for i in range(pat_len):
        pat_hash += ord(pattern[i]) * (prime ** i)
        text_hash += ord(text[i]) * (prime ** i)

    indices = []

    for i in range(text_len - pat_len + 1):
        if pat_hash == text_hash:
            if text[i:i + pat_len] == pattern:
                indices.append(i)

        if i < text_len - pat_len:
            text_hash = (text_hash - ord(text[i])) / prime
            text_hash += ord(text[i + pat_len]) * (prime ** (pat_len - 1))

    return indices

pattern = "SZOSA"
text = "W CZASIE SUSZY SZOSA SUCHA SZOSA"
print("Indices where pattern occurs:", rabin_karp(pattern, text))
