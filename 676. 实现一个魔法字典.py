class MagicDictionary:

    def __init__(self):
        self.l = []

    def buildDict(self, dictionary ) -> None:
        self.l = dictionary


    def search(self, searchWord: str) -> bool:
        result = False
        for word in self.l:
            if len(searchWord) == len(word):
                cnt = 0
                for i,c in enumerate(word):
                    if searchWord[i] !=word[i]:
                        cnt +=1
                        if cnt > 1:
                            break
                if cnt == 1:
                    # result = (result or True)  #能返回true的时候， 后面的判断就不用执行了
                    return True

        return result





if __name__ == '__main__':
    m = MagicDictionary()
    m.buildDict(['hello','leetcode'])
    print(m.search('hello'))
    print(m.search('hell2'))
    print(m.search('hell'))