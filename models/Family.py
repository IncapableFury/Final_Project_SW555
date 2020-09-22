##from individual import individual

class Family:
    def __init__(self, id, husband, wife, married = None, divorced = None, children_list = []):
        self.id = id
        self._marriedDate = married
        self._divorced = divorced
        self._husband = husband
        self._wife = wife
        self._children = children_list

    def get_husband(self) -> individual:
        return self._husband

    def get_wife(self) -> individual:
        return self._wife

    def get_marriedDate(self) -> str:
        return self._marriedDate
    
    def get_divorced(self) -> str:
        return self._divorced

    def get_children(self) -> list:
        return self._children

    def set_husband(self, husband):
        if not isinstance(husband, type(individual)): raise TypeError("input has to be a individual type")
        self._husband = husband
    
    def set_wife(self, wife):
        if not isinstance(wife, type(individual)): raise TypeError("input has to be a individual type")
        self._wife = wife
    
    def set_marriedDate(self, married_date):
        if not isinstance(married_date, str): raise TypeError("input has to be a str type")
        self._marriedDate = married_date
    
    def set_divorced(self, divorced_date):
        if not isinstance(divorced_date, str): raise TypeError("input has to be a str type")
        self._divorced = divorced_date

    def set_children(self, children_list):
        if not isinstance(children_list, list) raise TypeError("input has to be a list type")
        self._children = children_list

    def add_children(self, child):
        if not isinstance(child, individual) raise TypeError("input has to be a individual type")
        self._children.append(child)