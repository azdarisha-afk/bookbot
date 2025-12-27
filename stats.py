def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_counts = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_counts:
            char_counts[lowered] += 1
        else:
            char_counts[lowered] = 1
    return char_counts


def get_sorted_char_count_list(char_counts):
    char_list = []
    for ch, num in char_counts.items():
        char_list.append({"char": ch, "num": num})

    def sort_on(item):
        return item["num"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list
