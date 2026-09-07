words = open("words.txt", encoding="utf-8").read().split()
seen = set()

for word in words:
    if word not in seen:
        seen.add(word)

print("count=", len(seen))