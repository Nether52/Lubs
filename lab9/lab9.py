# lab9.py

from collections import Counter

FILENAME = "text100.txt"   # ← ТВОЯ НАЗВА ФАЙЛУ


def get_pairs_from_word(word: str):
    """Повертає всі пари букв усередині ОДНОГО слова."""
    word = word.lower()
    for i in range(len(word) - 1):
        yield word[i:i+2]


def count_pairs_in_line(line: str) -> Counter:
    """
    Рахує пари букв тільки всередині слів.
    НЕ переходить між словами — повністю відповідає вимозі.
    """
    counter = Counter()

    words = line.split()

    for w in words:
        for pair in get_pairs_from_word(w):
            counter[pair] += 1

    return counter


def generator(filename: str):
    """
    Генератор, який пострічково повертає
    3 найчастіші пари для кожного рядка.
    """
    with open(filename, "r", encoding="utf-8") as f:
        for num, line in enumerate(f, start=1):
            line = line.strip()

            counter = count_pairs_in_line(line)

            # 3 найпопулярніші пари букв у цьому рядку
            top3 = counter.most_common(3)

            yield num, top3


def main():
    for line_num, pairs in generator(FILENAME):
        print(f"Рядок {line_num}:")
        if not pairs:
            print("  Немає пар")
        else:
            for pair, count in pairs:
                print(f"  '{pair}' — {count} раз(ів)")
        print("-" * 40)


if __name__ == "__main__":
    main()
