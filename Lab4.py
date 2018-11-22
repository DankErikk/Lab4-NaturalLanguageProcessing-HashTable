# Erik Rivera
# Lab3A
# CS2302 TR @ 10:30-11:50 
# Professor Aguirre, Diego
# TA Saha, Manoj
# Date of last modification 11/9/2018
# Purpose of this lab assigment is to improve running time of previous lab by using a hashmap
# This lab uses word embeddings to get the similarity between to words

from HashMap import HashMap
from HashMap import HashNode

import math
import string

    
def create_hash_array(file_name , size):
    # Initiate the class
    hash_array = HashMap(size)
    # Try to open the file, in the case that an error occurs, inform the user and exit program
    try:
        with open(file_name, encoding = "utf8") as file:
            alphabet = list(string.ascii_letters)
            # Scan each line
            for line in file:
                # Split line into array
                array = line.split(" ")
                # First element holds the word
                word = array[0]
                # If the first letter of the word is in the alphabet then add to HashMap
                if alphabet.__contains__(word[0]):
                    embedding = []
                    for num in array[1:]:
                        embedding.append(float(num))
                    node = HashNode(word, embedding)
                    #print("Inserting: " + str(node.key))
                    hash_array.__insert__(node)

    except FileNotFoundError:
        print("Error, file was not found...")
        print("Exiting...")
        exit()
    return hash_array
def compare_from_word_file(array, file_name):
    with open(file_name, encoding="utf8") as file:
        for line in file:
            words = line.split(" ")
            first_node = array.__find__(words[0])
            second_node = array.__find__(words[1])
            similarity = compare_nodes(first_node, second_node)
            print("Similarity between " + str(first_node.key) + " and " + str(second_node.key) + " is " + str(similarity))

def compare_nodes(first_node, second_node):
    # Check that both nodes contain embeddings
    if first_node.embedding is not None and second_node.embedding is not None:
        # Variable used for the top part of the fraction
        top = 0
        # Bottom variable used for bottom part of fraction
        bottomA = 0
        bottomB = 0
        
        for i in range(len(first_node.embedding)):
            top = top + (first_node.embedding[i] * second_node.embedding[i])

            bottomA = bottomA + first_node.embedding[i]**2
            bottomB = bottomB + second_node.embedding[i]**2
        return (top/(math.sqrt(bottomA) * math.sqrt(bottomB)))

def display_options():
    print("Select an option...")
    print("[1]: Compute the number of nodes in the tree.")
    print("[2]: Compute the height of the tree.")
    print("[3]: Generate file that contains words in the tree.")
    print("[4]: Given depth 'd', generate file with that depth.")
    print("[5]: Exit")

    while True:
        try:
            user_ans = int(input("Please enter 1 through 5...\n"))
        except TypeError:
            print("Sorry that is not a number...\n")
            continue
        if user_ans<1 and user_ans>5:
            continue
        else:
            break
    
    return user_ans

def perform_operation(user_ans, HashMap):
    if user_ans == 1:
            amount = compute_amount_nodes(HashMap)
            print("There are " + str(amount) + " nodes")
    if user_ans == 2:
        # height = compute_tree_height(temp.root)
        print("This method uses a hashmap.")
    if user_ans == 3:
        file_name_word = "word_file.txt"
        word_file = open(file_name_word,"w+",encoding =  "utf8")
        generate_text_file_from_hashtable(HashMap.array, word_file)
        print("Word file generated: word_file.txt")
    if user_ans == 4:
        # file_name_word_depth = "word_file_depth.txt"
        # word_file_depth = open(file_name_word_depth, "w+",  encoding =  "utf8")
        # while True:
        #     try:
        #         depth = int(input("Enter desired depth.\n"))
        #         if depth > compute_tree_height(temp.root):
        #             print("Depth too low.")
        #             continue
        #         else:
        #             generate_text_file_from_tree_depth(temp.root, depth, word_file_depth)
        #             print("Word file generate: word_file_depth.txt")
        #             break
        #     except ValueError:
        #         print("Please enter a number.")
        #         continue
        #     except TypeError:
        #         print("Please enter a number.")
        #         continue
        print("This method uses a hashmap.")
    if user_ans == 5:
        print("Thank You!")
        exit()
    
def compute_amount_nodes(array):
    return array.count
def generate_text_file_from_hashtable(array, word_file):
    for node in array:
        while node != None:
            word_file.write(node.key+"\n")
            node = node.next

def main():
    print("RUNNING MAIN")
    # First read the file provided and save it into an array composed of HashNodes
    while(True):    
        try:
            size = int(input("Enter size of hash array\n"))
            break
        except ValueError:
            print("Please enter a valid integer...")
        
    # Create the hash array by reading the file
    hash_array = create_hash_array(file_name , size)
    compare_from_word_file(hash_array, word_pairs_file_name)

    # After comparing the words in the file, prompt the user choose from the following options
    while True:
        array = hash_array
        # Display options
        # Method that returns a valid user input
        user_ans = display_options()
        # perform the operation
        perform_operation(user_ans, array)
file_name = "glove.6B.50d.txt"
word_pairs_file_name = "word_pairs.txt"
main()