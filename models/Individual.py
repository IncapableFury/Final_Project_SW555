import datetime
class Individual:
    '''
    This is the class for individual. 
    id is the only variable that is required. If other variable does not exist, it would return None
    If children/spouse does not exist, it would return an empty list
    
    all date value are passed in as str, and saved as tuple with formate (year, month, day)
    '''

    def __init__(self, id: str, name: str = None, gender: str = None, birth_date: str = None, death_date: str = None, family = [], parent_family = None):
        from Family import Family
        self.set_id(id)
        self.set_name(name)
        self.set_gender(gender)
        self.set_birthDate(birth_date)
        self.set_deathDate(death_date)
        self.set_familyList(family) 
        self.set_parentFamily(parent_family)
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

    def get_familyList(self) -> list:
        return self._familyList

    def get_parent_family(self):
        return self._parentFamily

    def set_id(self, id) -> str:
        ##if not isinstance(id, str): raise TypeError("input has to be a str type")
        self.id = id

    def set_name(self, name: str) -> None:
        if name is None: 
            self._name = None
            return
        ##if not isinstance(name, str): raise TypeError("input has to be a str type")
        self._name = name

    def set_gender(self, gender: str) -> None:
        if gender is None: 
            self._gender = None
            return
        ##if not isinstance(gender, str): raise TypeError("input has to be a str type")
        self._gender = gender

    def set_birthDate(self, birth_date: str) -> None:
        if birth_date is None: 
            self._birthDate = None
            return
        ##if not isinstance(birth_date, str): raise TypeError("input has to be a str type")
        self._birthDate = self.change_date_formate(birth_date)

    def set_deathDate(self, death_date: str) -> None:
        if death_date is None:
            self._deathDate = None
            return
        ##if not isinstance(death_date, str): raise TypeError("input has to be a str type")
        self._deathDate = self.change_date_formate(death_date)

    def set_familyList(self, family) -> None:
        ##if not isinstance(family, list): raise TypeError("input has to be a list type")
        self._familyList = family

    def set_parentFamily(self, parent_family) -> None:
        ##if not isinstance(parent_family, family): raise TypeError("input has to be a family type")
        self._parentFamily = parent_family

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


    def dates_before_current_date(self):
        pass

    def birth_before_marriage(self):
        pass

    def birth_before_death(self):
        pass

    def less_then_150_years_old(self):
        pass

    def no_bigamy(self):
        pass

    def siblings_spacing(self):
        pass

    def parents_not_too_old(self):
        pass

# ---------------------shit testing below---------------------


if __name__ == "__main__":
    # name = None, gender = None, birth_date = None, death_date = None, children = [], spouse = []
    '''
    test run the class
    '''
    from Family import Family
    fam_test = Family ("1")
    test_list = ["01", "Jason", "M", "09 APR 1997", "25 DEC 2078", [fam_test], fam_test]
    test = Individual(test_list[0])
    test.set_name(test_list[1])
    test.set_gender(test_list[2])
    test.set_birthDate(test_list[3])
    test.set_deathDate(test_list[4])
    test.set_familyList(test_list[5])
    test.set_parentFamily(test_list[6])

    print("id:", test.get_id())
    print("Name:", test.get_name())
    print("gender:", test.get_gender())
    print("birthday:", test.get_birthDate())
    print("age:", test.get_age())
    print("deathdate:", test.get_deathDate())
    print("family:", test.get_familyList())
    print("parent family:", test.get_parent_family())
