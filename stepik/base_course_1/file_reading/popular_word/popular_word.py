s = []
with open('in.txt', 'r', encoding='utf-8') as file_reader:
    for line in file_reader:
        for i in line.strip().lower().split():
            s.append(i)
d = {}
pop_words = []
max_word_count = 1
for key in s:
    if d.get(key) is None:
        d[key] = 1
    else:
        d[key] += 1
        if d[key] > max_word_count:
            max_word_count = d[key]
for key, value in d.items():
    if value == max_word_count:
        pop_words.append(key)
pop_words.sort()

with open('out.txt', 'w') as file_writer:
    file_writer.write(pop_words[0] + " " + str(max_word_count))
