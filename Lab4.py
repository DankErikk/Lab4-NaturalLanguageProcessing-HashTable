from HashMap import HashMap
from HashMap import HashNode

import string
def create_hash_array(file_name , size):
    
    hash_array = HashMap(size)
    # Try to open the file, in the case that an error occurs, inform the user and exit program
    try:
        with open(file, encoding = "utf8") as file:
            alphabet = list(string.ascii_letters)
            # Scan each line
            for line in file:
                # Split line into array
                array = line.split(" ")
                # First element holds the word
                word = array[0]
                # If the first letter of the word is in the alphabet then add to HashMap
                if alphabet.__contains__(word[0]):
                    embedding = array[1:]
                    node = HashNode(word, embedding)
                    hash_array.__insert__(node)

    except FileNotFoundError:
        print("Error, file was not found...")
        exit()
    return hash_array
def main():
    # First read the file provided and save it into an array composed of HashNodes
    size = input("Enter size of hash array\n")
    hash_array = [None]*size
    hash_array = create_hash_array(file_name , size)
main