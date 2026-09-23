import string

def word_frequency_analyser(text):
    text = text.lower()

    # Remove punctuation
    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    words = text.split()

    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    # Sort by frequency in descending order
    sorted_freq = sorted(
        freq.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_freq


# Main program
text = input("Enter a paragraph / text: ")

result = word_frequency_analyser(text)

print("\nWord Frequency:")

for word, count in result:
    print(f"{word} : {count}")