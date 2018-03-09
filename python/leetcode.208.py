class Node(object):
    def __init__(self, x):
        self.next = [None] * 26
        self.val = x
        self.fail = None
        self.valid = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for x in word:
            x_index = ord(x) - ord('a')
            if cur.next[x_index] == None:
                cur.next[x_index] = Node(x)
            cur = cur.next[x_index]
        cur.valid = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for x in word:
            x_index = ord(x) - ord('a')
            if cur.next[x_index] == None:
                return False
            cur = cur.next[x_index]
        return cur.valid

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for x in prefix:
            x_index = ord(x) - ord('a')
            if cur.next[x_index] == None:
                return False
            cur = cur.next[x_index]
        return True


# Your Trie object will be instantiated and called as such:
if __name__ == '__main__':
    obj = Trie()
    obj.insert("word")
    print obj.search("word")
    print obj.startsWith("wo")
    print obj.startsWith("")
    print obj.startsWith("a")
    print obj.search("wo")