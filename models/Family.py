from Individual import Individual

class Family:
    '''
    This is the class for Family. 
    id is the only variable that is required. If other variable does not exist, it would return None
    If children does not exist, it would return an empty list
    
    all date value are passed in as str, and saved as tuple with formate (year, month, day)
    '''
    def __init__(self, id: str, husband: Individual = None, wife: Individual = None, married: str = None, divorced: str = None, children_list: list = []):
        self.id = id
        self._husband = husband
        self._wife = wife
        if married is not None: self._marriedDate = self.change_date_formate(married)
        else: self._marriedDate = married
        if divorced is not None: self._divorced = self.change_date_formate(divorced)
        else: self._divorced = divorced
        self._children = children_list
        self._monthList = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

    def get_id(self) -> str:
        return self.id

    def get_husband(self) -> Individual:
        return self._husband.get_id()

    def get_wife(self) -> Individual:
        return self._wife.get_id()

    def get_marriedDate(self) -> tuple:
        return self._marriedDate
    
    def get_divorced(self) -> tuple:
        return self._divorced

    def get_children(self) -> list:
        return self._children

    def set_husband(self, husband: Individual) -> None:
        if not isinstance(husband, Individual): raise TypeError("input has to be a Individual type")
        self._husband = husband
    
    def set_wife(self, wife: Individual) -> None:
        if not isinstance(wife, Individual): raise TypeError("input has to be a Individual type")
        self._wife = wife
    
    def set_marriedDate(self, married_date: str) -> None:
        if not isinstance(married_date, str): raise TypeError("input has to be a str type")
        self._marriedDate = self.change_date_formate(married_date)
    
    def set_divorced(self, divorced_date: str) -> None:
        if not isinstance(divorced_date, str): raise TypeError("input has to be a str type")
        self._divorced = self.change_date_formate(divorced_date)

    def set_children(self, children_list: list) -> None:
        if not isinstance(children_list, list): raise TypeError("input has to be a list type")
        self._children = children_list

    def add_children(self, child: str) -> None:
        '''
        this function would add one kid into the children list
        '''
        if not isinstance(child, str): raise TypeError("input has to be a Individual type")
        self._children.append(child)


    def change_date_formate(self, str_input_date: str) -> tuple:
        '''
        Would take the string input and convert it into a int tuple:(year, month, day)
        '''
        date_list = str_input_date.split(" ")
        date_list[1] = str(self._monthList.index(date_list[1])+1)
        temp = date_list[0]
        date_list[0] = date_list[2]
        date_list[2] = temp
        tuple_out = tuple(date_list)
        return tuple_out
        

if __name__ == "__main__":
    #id, husband = None, wife = None, married = None, divorced = None, children_list = [])
    '''
    test run the class
    '''
    husband = Individual("10")
    wife = Individual("20")
    test_list = ["01", husband, wife, "04 MAR 1999", "7 MAY 2011", ["03", "11"]]

    test = Family(test_list[0])
    test.set_husband(test_list[1])
    test.set_wife(test_list[2])
    test.set_marriedDate(test_list[3])
    test.set_divorced(test_list[4])
    test.set_children(test_list[5])
    test.add_children("51")

    print("id:", test.get_id())
    print("husband:", test.get_husband())
    print("wife:", test.get_wife())
    print("married:", test.get_marriedDate())
    print("divorced:", test.get_divorced())
    print("children:", test.get_children())
