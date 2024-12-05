def all_subsequences(text):
    length = len(text)
    for i in range(1 << length):  # 2^length
        subseq = []
        for j in range(length):
            # Проверяем, установлен ли j-й бит
            if (i & (1 << j)):
                subseq.append(text[j])
        yield ''.join(subseq)

a = all_subsequences("abc")
for i in a:
    print(i)
