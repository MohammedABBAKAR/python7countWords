# Write a function that receives a string value. 
# This function counts the number of words in a text value,
# then returns the number of words of type integer.


def countWords(txt: str) -> int:
    # Split the text by whitespace to get words
    words = txt.split()
    
    # Count the number of words
    word_count = len(words)
    
    return word_count

# Examples of using the function
print(countWords("Hello, world! This is a test."))  # Output: 6
print(countWords("Another example with more words in it."))  # Output: 7
