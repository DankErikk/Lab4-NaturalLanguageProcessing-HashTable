class HashMap:
    def __init__(self, size):
        self.array = [None]*size
    def __insert__(self, node):
        loc = node.value % self.size
        if self.array[loc] == None:
            self.array[loc] = node
            return
        node.next = self.array[loc]
        self.array[loc] = node
        return
    def __insert_word_embedding__(self, word, embedding):
        node = HashNode(word,embedding)
        self.__insert__(node)

    def __find__(self, )

class HashNode:
    def __init__(self, key, embedding, next=None):
        # Key will be the actual word
        self.key = key
        # Embedding will hold the embedding for the node
        self.embedding = embedding
        # Next node
        self.next = next
        
    