def countWordFrequency(file_path):
    hashCount = {}

    with open(file_path, 'r') as file:
        # Read the entire content of the file
        content = file.read()

        # Split the content into words (assuming words are separated by whitespace)
        words = content.split()

        # Count the occurrences of each word
        for w in words:
            w = w.strip(".,!?\"':;()[]{}")  # Remove common punctuation marks
            w = w.lower()  # Convert to lowercase for case-insensitive count
            hashCount[w] = 1 + hashCount.get(w, 0)

    return hashCount


file_path = "sample.txt"  # Replace with the path to your text file
result = countWordFrequency(file_path)

print("Word occurrences in the file:")

for word, count in result.items():
    print(f"{word}: {count}")
