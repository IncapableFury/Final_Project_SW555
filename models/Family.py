class Family:
    def __init__(self, id):
        self.id = id
        self._marriedDate = None
        self._divorced = False
        self._husband = None
        self._wife = None
        self._children = []

    def get_husband(self) -> str:
        return self._husband if self._husband else "NA"
