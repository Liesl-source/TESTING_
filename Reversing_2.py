class WordReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)


# Example usage
sentence = "Hi there good morning!!!"
reverser = WordReverser(sentence)
print(reverser.reverse_words())
