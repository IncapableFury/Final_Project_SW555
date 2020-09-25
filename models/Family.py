class Family:
    '''
    This is the class for Family. 
    id is the only variable that is required. If other variable does not exist, it would return None
    If children does not exist, it would return an empty list
    
    all date value are passed in as str, and saved as tuple with formate (year, month, day)
    '''
    def __init__(self, id: str, husband = None, wife = None, married: str = None, divorced: str = None, children_list: list = []):
        from Individual import Individual
        self.set_id(id)
        self.set_husband(husband)
        self.set_wife(wife)
        self.set_marriedDate(married)
        self.set_divorced(divorced)
        self.set_children(children_list)
        self._monthList = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

    def get_id(self) -> str:
        return self.id

    def get_husband(self):
        return self._husband.get_id()

    def get_wife(self):
        return self._wife.get_id()

    def get_marriedDate(self) -> tuple:
        return self._marriedDate
    
    def get_divorced(self) -> tuple:
        return self._divorced

    def get_children(self) -> list:
        return self._children

    def set_id(self, id) -> str:
        ##if not isinstance(id, str): raise TypeError("input has to be a str type")
        self.id = id

    def set_husband(self, husband) -> None:
        if husband is None: 
            self._husband = None
            return
        ##if not isinstance(husband, Individual): raise TypeError("input has to be a Individual type")
        self._husband = husband
    
    def set_wife(self, wife) -> None:
        if wife is None:
            self._wife = None
            return
        ##if not isinstance(wife, Individual): raise TypeError("input has to be a Individual type")
        self._wife = wife
    
    def set_marriedDate(self, married_date: str) -> None:
        if married_date is None: 
            self._marriedDate = None
            return
        ##if not isinstance(married_date, str): raise TypeError("input has to be a str type")
        self._marriedDate = self.change_date_formate(married_date)
    
    def set_divorced(self, divorced_date: str) -> None:
        if divorced_date is None:
            self._divorced = None
            return
        ##if not isinstance(divorced_date, str): raise TypeError("input has to be a str type")
        self._divorced = self.change_date_formate(divorced_date)

    def set_children(self, children_list: list) -> None:
        ##if not isinstance(children_list, list): raise TypeError("input has to be a list type")
        self._children = children_list

    def add_children(self, child) -> None:
        '''
        this function would add one kid into the children list
        '''
        ##if not isinstance(child, Individual): raise TypeError("input has to be a Individual type")
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

    


    def multiple_births_lessOrEqual_than_5(self):
        pass

    def marriage_before_divorce(self):
        pass

    def dates_before_current_date(self):
        pass
        
    def marriage_after_14(self):
        pass

    def marriage_before_death(self):
        pass

    def divorce_before_death(self):
        pass

    def birth_before_marriage_of_parents(self):
        pass

    def birth_before_death_of_parents(self):
        pass


    # ---------------------shit testing below---------------------


if __name__ == "__main__":
    #id, husband = None, wife = None, married = None, divorced = None, children_list = [])
    '''
    test run the class
    '''
    from Individual import Individual
    husband = Individual("10")
    wife = Individual("20")
    child = Individual("55")
    test_list = ["01", husband, wife, "04 MAR 1999", "7 MAY 2011", [Individual("03"), Individual("11")]]

    test = Family(test_list[0])
    test.set_husband(test_list[1])
    test.set_wife(test_list[2])
    test.set_marriedDate(test_list[3])
    test.set_divorced(test_list[4])
    test.set_children(test_list[5])
    test.add_children(child)

    print("id:", test.get_id())
    print("husband:", test.get_husband())
    print("wife:", test.get_wife())
    print("married:", test.get_marriedDate())
    print("divorced:", test.get_divorced())
    print("children:", test.get_children())



