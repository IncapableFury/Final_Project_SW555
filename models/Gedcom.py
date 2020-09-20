class Gedcom:
    def __init__(self, path,supportTags):
        self._data = self.readfile(path)
        self._supportTags = supportTags

    def readfile(self, path):
        res = []
        f = open(path, "r")
        for l in f:
            res.append(l)
        f.close()
        return res

    def peek(self):
        def parseline(line):
            level, tag, arguments = line[0], line[1], line[2:]
            if arguments and arguments[0] in ["INDI", "FAM"]:
                tag, arguments = arguments[0], tag
            if tag in self._supportTags:
                print("    " * int(level), level, tag, arguments)

        for line in self._data:
            parseline(line.split())
