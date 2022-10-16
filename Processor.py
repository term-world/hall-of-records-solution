import json
from inventory import FixtureSpec

class Processor(FixtureSpec):

    def __init__(self):
        super().__init__()
        self.filename = "records/data.json"
        self.data = self.__load()

    def __load(self):
        fh = open(self.filename, "r")
        return json.load(fh)

def main():
    obj = Processor()
    data = obj.data

if __name__ == "__main__":
    main()