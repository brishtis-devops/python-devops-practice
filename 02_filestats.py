# file: count_text_stats.py

def count_file_stats(filename):
    lines = 0
    words = 0
    characters = 0

    with open(filename, "r") as file:
        for line in file:
            lines += 1
            words += len(line.split())
            characters += len(line)

    print("Lines:", lines)
    print("Words:", words)
    print("Characters:", characters)


# change the file name below if needed
count_file_stats("sample.txt")
