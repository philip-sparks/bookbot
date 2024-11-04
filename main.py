def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        
        word_count = count_words(file_contents)
        print(f"Word count: {word_count}")
        
        character_counts = count_characters(file_contents)
        print("Character counts:", character_counts)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    # Dictionary to store character counts
    char_count = {}
    for char in text.lower():
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

if __name__ == "__main__":
    main()
