
# Mini Project 1: Text Analyzer System

# Accept text from the user
text = input("Enter a sentence or paragraph: ")

# Remove extra spaces from the beginning and end
text = text.strip()

# Remove extra spaces between words
clean_text = " ".join(text.split())

# Convert text into lowercase
lower_text = clean_text.lower()

# Convert text into uppercase
upper_text = clean_text.upper()

# Count total characters
total_characters = len(clean_text)

# Count total words
words = clean_text.split()
total_words = len(words)

# Count total sentences
total_sentences = 0

for ch in clean_text:
    if ch in ".!?":
        total_sentences += 1

# Initialize counters
vowels = 0
consonants = 0
digits = 0
special_characters = 0

# Loop through each character in the text
for ch in clean_text:

    # Check vowels
    if ch.lower() in "aeiou":
        vowels += 1

    # Check consonants
    elif ch.isalpha():
        consonants += 1

    # Check digits
    elif ch.isdigit():
        digits += 1

    # Check special characters
    elif not ch.isspace():
        special_characters += 1

# Display text analysis
print("\n----- TEXT ANALYZER REPORT -----")

print("Total Characters:", total_characters)
print("Total Words:", total_words)
print("Total Sentences:", total_sentences)

print("Total Vowels:", vowels)
print("Total Consonants:", consonants)
print("Total Digits:", digits)
print("Total Special Characters:", special_characters)

# Display uppercase and lowercase text
print("\nUppercase Text:", upper_text)
print("Lowercase Text:", lower_text)

# Search for a specific word
search_word = input("\nEnter a word to search: ")

# Check whether the word exists
if search_word.lower() in lower_text.split():
    print(search_word, "exists in the text.")
else:
    print(search_word, "does not exist in the text.")

# Find frequency of each word
print("\n----- WORD FREQUENCY -----")

word_frequency = {}

for word in lower_text.split():

    # Remove basic punctuation from words
    word = word.strip(".,!?;:")

    if word != "":
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

# Display word frequency
for word, frequency in word_frequency.items():
    print(word, ":", frequency)

# Display cleaned text
print("\nText After Removing Extra Spaces:")
print(clean_text)

# End of program
