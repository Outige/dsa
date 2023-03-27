"""
    Simple hash table implementation. Using an array and linear probing
"""

WORD_BANK = [
    "locate","recent","environment","tonight","level","folks",
    "break","second","shop","gulf","hidden","term","inside",
    "fierce","factory","rest","perfectly","discuss","fear",
    "slipped","everything","replied","breakfast","ready",
    "finest","blind","mainly","onlinetools","rice","egg",
    "track","facing","between","grown","flame","forty","bend",
    "fought","class","adjective","magnet","according","eaten",
    "fellow","apart","night","gravity","dug","gone","believed",
    "yesterday","exact","instrument","soldier","quickly",
    "popular","still","choice","thread","indicate","ask",
    "himself","likely","due","size","serve","none","cup","it",
    "more","near","neighbor","gate","usual","nervous","merely",
    "however","whole","connected","feature","friendly","garden",
    "government","baby","gently","small","seen","hurried",
    "substance","monkey","terrible","broad","control","longer",
    "moment","produce","additional","sure","year","mountain",
    "zoo","were","distant","position","fifteen","various",
    "certain","student","border","dance","firm","human","window",
    "feel","higher","real","belt","been","fell","cream","advice",
    "under","rapidly","needed","chain","halfway","rhythm",
    "stepped","easily","particularly","swimming","dark","tears",
    "cattle","down","primitive","sort","burst","clock","lovely",
    "hundred","equipment","open","your","immediately","back",
    "region","eleven","introduced","women","main","ever",
    "fairly","teeth","chosen","sad","as","return","gift",
    "freedom","damage","purpose","edge","guess","lay","mark","most",
    "let","wrapped","daily","melted","hold","highest","prize","guard",
    "with","sign","buried","coast","tired","riding","wheel","page",
    "trick","negative","office","thumb","calm","he","hungry","split",
    "skill","selection","quick","adventure","although","spread"
]

class HT:
    """
        Hash table class
    """
    def __init__(self, size):
        self.table = [None]*size
        self.colisions = 0

    def __getitem__(self, key):
        index = self.hash_function(key)
        if index is None or self.table[index] != key:
            return False
        return True

    def linear_probe(self, start):
        """
            Linear probling method
        """
        if self.table[start] is None:
            return start
        self.colisions += 1

        for i in range(start+1, len(self.table)):
            if self.table[i] is None:
                return i
        for i in range(0, start):
            if self.table[i] is None:
                return i
        return None

    def hash_function(self, key):
        """
            Simple hash function
        """
        total = 0
        for x in key:
            total += ord(x)
        return self.linear_probe(total % len(self.table))

    def insert(self, key):
        """
            Insert function
        """
        index = self.hash_function(key)
        if index is None:
            raise IndexError('HT max size')
        self.table[index] = key

if __name__ == '__main__':
    ht = HT(size=20)
    for i in range(0, 20):
        ht.insert(WORD_BANK[i])
    print(ht.table, ht.colisions)
