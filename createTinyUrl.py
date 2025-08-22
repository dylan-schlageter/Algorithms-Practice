class Codec:

    def __init__(self):
        self.link_num = {}
        self.num_link = {}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        self.link_num[longUrl] = self.counter
        self.num_link[self.counter] = longUrl
        res = self.counter
        self.counter += 1
        return "http://tinyurl.com/" + str(res)

    def decode(self, shortUrl: str) -> str:
        divided = shortUrl.split("/")        
        return self.num_link[int(divided[-1])]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
