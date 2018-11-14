from HashNode import HashNode
import string
def create_hash_array(file_name):
    hash_array = []
    try:
        with open(file, encoding = "utf8") as file:
            alphabet = list(string.ascii_letters)
            for line in file:
                array = line.split(" ")
                word = array[0]
                if alphabet.__contains__(word[0]):
                    numbers = []
                    for num in array[1:]:
                        numbers.append(float(num))
                    wordNode = HashNode(word, numbers)




    return hash_array
def main():
    # First read the file provided and save it into an array composed of HashNodes
    size = input("Enter size of hash array\n")
    hash_array = [None]*size
    hash_array = create_hash_array(file_name, len(hash_array))
main