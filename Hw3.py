import re

def preprocess_text(text):
    """Preprocess text by removing punctuation, converting to lowercase, and splitting into words."""
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    words = text.split()  # Split into words
    return set(words)  # Return a set of unique words

def count_unique_words(file_path):
    """Load text from a file and count the unique words."""
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    unique_words = preprocess_text(text)
    return len(unique_words)

# File paths (Replace with the actual file names)
crime_and_punishment_file = "crime.txt"  # Change this to your actual file path
moby_dick_file = "moby.txt"  # Change this to your actual file path

# Count unique words in both books
crime_unique_count = count_unique_words(crime_and_punishment_file)
moby_unique_count = count_unique_words(moby_dick_file)

# Output the results
print(f"'Crime and Punishment' has {crime_unique_count} unique words.")
print(f"'Moby Dick' has {moby_unique_count} unique words.")

# Compare the two
if crime_unique_count > moby_unique_count:
    print("Fyodor Dostoevsky used more unique words in 'Crime and Punishment'.")
elif crime_unique_count < moby_unique_count:
    print("Herman Melville used more unique words in 'Moby Dick'.")
else:
    print("Both authors used the same number of unique words.")