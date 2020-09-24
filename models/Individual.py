import datetime

class Individual:
    '''
    This is the class for individual. 
    id is the only variable that is required. If other variable does not exist, it would return None
    If children/spouse does not exist, it would return an empty list
    
    all date value are passed in as str, and saved as tuple with formate (year, month, day)
    '''
    def __init__(self, id: str, name: str = None, gender: str = None, birth_date: str = None, death_date: str = None, children: list = [], spouse: list = []):
        self.id = id
        self._name = name
        self._gender = gender
        if birth_date is not None: self._birthDate = self.change_date_formate(birth_date)
        else: self._birthDate = birth_date
        if death_date is not None: self._deathDate = self.change_date_formate(death_date)
        else: self._deathDate = death_date
        self._children = children
        self._spouse = spouse
        self._monthList = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]


    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self._name 

    def get_gender(self) -> str:
        return self._gender

    def get_birthDate(self) -> tuple:
        return self._birthDate

    def get_age(self) -> int:
        '''
        calculate age base on the birthdate. If birthdate is None, this would return None

        require datetime module
        '''
        if self._birthDate is None: return None
        now_time = datetime.datetime.now()
        Age = now_time.year - int(self._birthDate[0])
        if(now_time.month - int(self._birthDate[1]) < 0): Age -= 1
        if(now_time.month - int(self._birthDate[1]) == 0 and now_time.day - int(self._birthDate[2]) < 0): Age -= 1
        return Age

    def get_deathDate(self) -> tuple:
        return self._deathDate

    def get_children(self) -> list:
        return self._children

    def get_spouse(self) -> list:
        return self._spouse


    def set_name(self, name: str) -> None:
        if not isinstance(name, str): raise TypeError("input has to be a str type")
        self._name = name

    def set_gender(self, gender: str) -> None:
        if not isinstance(gender, str): raise TypeError("input has to be a str type")
        self._gender = gender

    def set_birthDate(self, birth_date: str) -> None:
        if not isinstance(birth_date, str): raise TypeError("input has to be a str type")
        self._birthDate = self.change_date_formate(birth_date)

    def set_deathDate(self, death_date: str) -> None:
        if not isinstance(death_date, str): raise TypeError("input has to be a str type")
        self._deathDate = self.change_date_formate(death_date)

    def set_children(self, children: list) -> None:
        if not isinstance(children, list): raise TypeError("input has to be a list type")
        self._children = children

    def add_child(self, child: str) -> None:
        '''
        this function would add one kid into the children list
        '''
        if not isinstance(child, str): raise TypeError("input has to be a list type")
        self._children.append(child)

    def set_spouse(self, spouse: list) -> None:
        if not isinstance(spouse, list): raise TypeError("input has to be a list type")
        self._spouse = spouse

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
    # name = None, gender = None, birth_date = None, death_date = None, children = [], spouse = []
    '''
    test run the class
    '''
    test_list = ["01", "Jason", "M", "09 APR 1997", "25 DEC 2078", ["02", "03"], ["10, 13"]]
    test = Individual(test_list[0])
    test.set_name(test_list[1])
    test.set_gender(test_list[2])
    test.set_birthDate(test_list[3])
    test.set_deathDate(test_list[4])
    test.set_children(test_list[5])
    test.add_child("51")
    test.set_spouse(test_list[6])

    print("id:", test.get_id())
    print("Name:", test.get_name())
    print("gender:", test.get_gender())
    print("birthday:", test.get_birthDate())
    print("age:", test.get_age())
    print("deathdate:", test.get_deathDate())
    print("children:", test.get_children())
    print("spouse:", test.get_spouse())