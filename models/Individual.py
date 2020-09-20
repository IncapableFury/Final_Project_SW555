class Individual:
    def __init__(self, id):
        self.id = id
        self._name = None
        self._gender = None
        self._birthDate = None
        self._deathDate = None
        self._children = []
        self._spouse = None

    def set_name(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name if self._name else "NA"
