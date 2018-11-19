def string_to_num(word):
        # This will convert a string to a positive integer
        word = word.lower()

        # Check if the word is empty
        if word == "" or len(word)==0:
            return 0
        # Base case
        if len(word) == 1:
            # Return the unicode point value
            return ord(word)-96
        # return the value of the first character to the power of the length of the string times the value of the character
        return string_to_num(word[1:]) +(26**(len(word)-1))*(ord(word[0])-96)
class HashMap:
    def __init__(self, size):
        self.size = size
        self.array = [None]*size
        self.count = 0
    def __insert__(self, node):
        loc = node.value % self.size
        self.array[loc] = HashNode(node.key, node.embedding, self.array[loc])
        self.count+=1
        return
    def __insert_word_embedding__(self, word, embedding):
        node = HashNode(word,embedding)
        self.__insert__(node)
        return
    def __find__(self, word):
        # find the value of the string and start iterating through the position
        location = string_to_num(word)%self.size
        temp_node = self.array[location]
        while temp_node.key != None:
            if temp_node.key == word:
                return temp_node
        print("Word: " + str(word) + " is not in the array...")
        return None

        

class HashNode:
    def __init__(self, key, embedding, next=None):
        # Key will be the actual word
        self.key = key
        # Value will be converted from a base 26 to a base 10
        self.value = string_to_num(self.key)
        # Embedding will hold the embedding for the node
        self.embedding = embedding
        # Next node
        self.next = next
        
    