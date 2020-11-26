from models.Error import Error

class Individual:
    '''
    This is the class for individual.
    id is the only variable that is required. If other variable does not exist, it would return None
    If children/spouse does not exist, it would return an empty list

    all date value are passed in as str, and saved as tuple with formate (year, month, day)
    '''

    def __init__(self, id: str):
        self.id = id
        self._name = None
        self._gender = None
        self._birthDate = None
        self._deathDate = None
        self._family = []
        self._parentFamily = None
        self._lineNum = {}

    def get_lineNum(self)-> {}:
        return self._lineNum

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self._name

    def get_gender(self) -> str:
        return self._gender

    def get_birthDate(self) -> tuple:
        return self._birthDate

    def get_age(self, days=False) -> int:
        """
        :param days: a flag indicates whether you want the years or the days
        :return: Return age in base of years or days. Would return -1 if no birthday info

        """
        import datetime
        if not self._birthDate: raise AttributeError("Error: missing birthdate for age")
        today = datetime.date.today()
        lived_days = (today - datetime.date(*self._birthDate)).days
        return lived_days // 365 if not days else lived_days

    def get_deathDate(self) -> tuple:
        return self._deathDate

    def get_family(self):
        return self._family

    def get_parent_family(self):
        return self._parentFamily

    def set_lineNum(self, lineNumberDict) -> None:
        self._lineNum = lineNumberDict

    def set_name(self, name: str) -> None:
        # if not isinstance(name, str): raise TypeError("input has to be a str type")
        self._name = name

    def set_gender(self, gender: str) -> None:
        # if not isinstance(gender, str): raise TypeError("input has to be a str type")
        self._gender = gender

    def set_birthDate(self, birth_date: list) -> None:  # set missing dates to Jan/01
        # if not isinstance(birth_date, str): raise TypeError("input has to be a str type")
        from datetime import datetime
        if not birth_date:  # ignore empty input
            pass
        elif len(birth_date) == 1:  # assume only year is provided
            birth_date = (int(birth_date[0]), 1, 1)
        elif len(birth_date) == 2:  # assume only year & month are provided
            birth_date = (int(birth_date[1]), birth_date[0], 1)
        # now we know at least all the fields are supplied
        if not all(isinstance(v, int) for v in birth_date):  # convert to desired format
            birth_date = self.change_date_formate(birth_date)
        try:  # check date validity
            datetime(*birth_date)  # raise error if failed
            self._birthDate = birth_date
        except ValueError:
            raise ValueError("Birthday provided for " + self.get_id() + " is not valid.")

    def set_deathDate(self, death_date: list) -> None:
        # if not isinstance(death_date, str): raise TypeError("input has to be a str type")
        self._deathDate = self.change_date_formate(death_date)

    def add_to_family(self, family) -> None:
        # if not isinstance(family, Family): raise TypeError("input has to be a Family type")
        self._family.append(family)

    def set_parentFamily(self, parent_family) -> None:
        # if not isinstance(parent_family, family): raise TypeError("input has to be a family type")
        self._parentFamily = parent_family

    def change_date_formate(self, date: list) -> tuple:
        '''
        Would take the string input and convert it into a int tuple:(year, month, day)
        '''

        monthList = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9,
                     "OCT": 10, "NOV": 11, "DEC": 12}
        return int(date[2]), monthList[date[1]] if date[1] in monthList else 13, int(
            date[0])  # handle invalid month input

    # US02 Birth should occur before marriage of an individual
    def birth_before_marriage(self):
        from datetime import date
        if not self._birthDate or not self._family: raise AttributeError("Error: Missing self birthday or family marriage date")
        # if not self._parentFamily.get_marriedDate(): raise AttributeError("Error: Missing attribute")
        for family in self.get_family():
            if not family.get_marriedDate(): raise AttributeError("Error: Missing attribute")
            timedelta = date(*family.get_marriedDate()) - date(*self._birthDate)
            if (timedelta.days <= 0):
                #return False
                raise Error('ERROR', 'INDIVIDUAL', 'US02', self.get_lineNum()['BIRT'], f" Individual's Birthday {self.get_birthDate()} is after marriage date of Family {family.get_marriedDate()}")
        return True

    #US03 Birth should occur before death of an individual
    def birth_before_death(self):
        from datetime import date
        if not self._birthDate or not self._deathDate: raise AttributeError("Error: Missing attribute")

        if (date(*self._deathDate) - date(*self._birthDate)).days > 0:
            return True
        else: raise Error('ERROR', 'INDIVIDUAL', 'US03', self.get_lineNum()['BIRT'], f" Individual's Birthday {self.get_birthDate()} is after individual's death date {self.get_deathDate()}")

    #US07 Death should be less than 150 years after birth for dead people, and current date should be less than 150 years after birth for all living people
    def less_then_150_years_old(self):
        if self.get_age() < 150: return True
        else: raise Error('ANOMALY', 'INDIVIDUAL', 'US07', self.get_lineNum()['DEAT'], f" Individual's Age {self.get_age()} is greater than 150")

    #US11 Marriage should not occur during marriage to another spouse //EXPLAIN CASE
    def no_bigamy(self):
        if (len(self._family) <= 1): return True
        marrageAgeList = []
        birthDate = self._birthDate
        if not self._family: raise AttributeError("Error: Missing attribute")
        for each_marrage in self._family:
            if not each_marrage.get_marriedDate(): raise AttributeError("Error: Missing attribute")
            marrageAge = each_marrage.get_marriedDate()[0] - birthDate[0] + (
                    each_marrage.get_marriedDate()[1] - birthDate[1]) / 12 + (
                                 each_marrage.get_marriedDate()[2] - birthDate[2]) / 365
            devorceAge = None
            if (each_marrage.get_divorcedDate() is not None): devorceAge = each_marrage.get_divorcedDate()[0] - \
                                                                           birthDate[
                                                                               0] + (each_marrage.get_divorcedDate()[
                                                                                         1] - birthDate[1]) / 12 + (
                                                                                   each_marrage.get_divorcedDate()[
                                                                                       2] -
                                                                                   birthDate[2]) / 365
            for Age_range in marrageAgeList:
                if (Age_range[1] == devorceAge and devorceAge == None):
                    #return False
                    raise Error('ERROR', 'INDIVIDUAL', 'US11', self.get_lineNum()['INDI ID'],
                                      f" Individual has committed bigamy")

                elif ((not Age_range[1] == devorceAge) and devorceAge == None):
                    if (not (Age_range[0] < marrageAge and Age_range[1] < marrageAge)):
                        #return False
                        raise Error('ERROR', 'INDIVIDUAL', 'US11', self.get_lineNum()['INDI ID'],
                                    f" Individual has committed bigamy")
                elif ((not Age_range[1] == devorceAge) and Age_range[1] == None):
                    if (not (marrageAge < Age_range[0] and devorceAge < Age_range[0])):
                        #return False
                        raise Error('ERROR', 'INDIVIDUAL', 'US11', self.get_lineNum()['INDI ID'],
                                    f" Individual has committed bigamy")
                else:
                    if (marrageAge > Age_range[0] and marrageAge < Age_range[1]):
                        #return False
                        raise Error('ERROR', 'INDIVIDUAL', 'US11', self.get_lineNum()['INDI ID'],
                                    f" Individual has committed bigamy")
                    elif (devorceAge > Age_range[0] and devorceAge < Age_range[1]):
                        #return False
                        raise Error('ERROR', 'INDIVIDUAL', 'US11', self.get_lineNum()['INDI ID'],
                                    f" Individual has committed bigamy")
            marrageAgeList.append((marrageAge, devorceAge))
        return True

    #US20 Aunts and uncles should not marry their nieces or nephews //NOT REMOVING OWN FATHER/MOTHER?
    def aunts_and_uncles(self):
        if (not self._parentFamily): raise AttributeError("Error: missing value")
        if (not self._parentFamily.get_husband() or not self._parentFamily.get_wife()): raise AttributeError(
            "Error: missing value")
        if (
                not self._parentFamily.get_husband().get_parent_family() or not self._parentFamily.get_wife().get_parent_family()): raise AttributeError(
            "Error: missing value")

        dad_grand_family = self._parentFamily.get_husband().get_parent_family()
        mom_grand_family = self._parentFamily.get_wife().get_parent_family()

        for dad_side_aunt_uncle in dad_grand_family.get_children():
            check_id = dad_side_aunt_uncle.get_id()
            for dad_side_family in dad_side_aunt_uncle.get_family():
                if (not dad_side_family.get_husband() or not dad_side_family.get_wife()): raise AttributeError(
                    "Error: missing value")
                uncle_id = dad_side_family.get_husband().get_id()
                aunt_id = dad_side_family.get_wife().get_id()
                if (uncle_id == aunt_id):
                    #return False
                    raise Error('ERROR', 'INDIVIDUAL', 'US20', dad_side_family.get_husband().get_lineNum()['INDI ID'],
                                    f" Individual's Aunt{aunt_id} and Uncle{uncle_id} has the same ID")
                for each_child in dad_side_family.get_children():
                    if (uncle_id == each_child.get_id() or aunt_id == each_child.get_id()):
                        #return False
                        raise Error('ERROR', 'INDIVIDUAL', 'US20',
                                    dad_side_family.get_husband().get_lineNum()['INDI ID'],
                                    f" Individual's Aunt{aunt_id} or Uncle{uncle_id} is married to their child {each_child.get_id()}")
        for mom_side_aunt_uncle in mom_grand_family.get_children():
            for mom_side_family in mom_side_aunt_uncle.get_family():
                if (not mom_side_family.get_husband() or not mom_side_family.get_wife()): raise AttributeError(
                    "Error: missing value")
                uncle_id = mom_side_family.get_husband().get_id()
                aunt_id = mom_side_family.get_wife().get_id()
                if (uncle_id == aunt_id):
                    #return False
                    raise Error('ERROR', 'INDIVIDUAL', 'US20', mom_side_family.get_husband().get_lineNum()['INDI ID'],
                                f" Individual's Aunt{aunt_id} and Uncle{uncle_id} has the same ID")
                for each_child in mom_side_family.get_children():
                    if (uncle_id == each_child.get_id() or aunt_id == each_child.get_id()):
                        #return False
                        raise Error('ERROR', 'INDIVIDUAL', 'US20',
                                    mom_side_family.get_husband().get_lineNum()['INDI ID'],
                                    f" Individual's Aunt{aunt_id} or Uncle{uncle_id} is married to their child {each_child.get_id()}")

        return True

    #US19 First cousins should not marry one another //PROBLEM HERE
    def first_cousins_should_not_marry(self):
        if not self.get_parent_family(): raise AttributeError("Error: missing parent family")
        if not self.get_parent_family().get_husband() or not self.get_parent_family().get_wife(): raise AttributeError("Error: missing husband or wife")
        if not self.get_parent_family().get_husband().get_parent_family() or not self.get_parent_family().get_wife().get_parent_family(): raise AttributeError("Error: missing husband/wife's parent family")

        daddy = self.get_parent_family().get_husband()
        daddy_siblings = self.get_parent_family().get_husband().get_parent_family().get_children()[:]
        daddy_siblings.remove(daddy)  # if singleton, this loop does nothing
        for daddy_sibling in daddy_siblings:
            daddy_sibling_families = daddy_sibling.get_family()  # consider past families
            for child_fam in daddy_sibling_families:
                for first_cousin in child_fam.get_children():
                    if first_cousin == self:
                        #return False
                        raise Error('ANOMALY', 'INDIVIDUAL', 'US19',
                                    first_cousin.get_lineNum()['INDI ID'],
                                    f"first_cousin {first_cousin.get_id()} is married to each other")

        mummy = self.get_parent_family().get_wife()
        mummy_siblings = self.get_parent_family().get_wife().get_parent_family().get_children()[:]
        mummy_siblings.remove(mummy)  # if singleton, this loop does nothing
        for mummy_sibling in mummy_siblings:
            mummy_sibling_families = mummy_sibling.get_family()  # consider past families
            for mummy_sibling_fam in mummy_sibling_families:
                for first_cousin in mummy_sibling_fam.get_children():
                    if first_cousin == self:
                        #return False
                        raise Error('ANOMALY', 'INDIVIDUAL', 'US19',
                                    first_cousin.get_lineNum()['INDI ID'],
                                    f"first_cousin {first_cousin.get_id()} is married to each other")
        return True

    #US17 Parents should not marry any of their descendants
    def no_marriages_to_descendants(self):
        if len(self.get_family()) == 0:
            return True
        spouse = []
        if not self.get_gender(): raise AttributeError("Gender of Individual not set")
        if self.get_gender() == "M":
            for past_family in self.get_family():
                spouse.append(past_family.get_wife())
        else:
            for past_family in self.get_family():
                spouse.append(past_family.get_husband())

        def dfs(indi):
            # print(indi.get_id())
            result = True
            for family in indi.get_family():
                for child in family.get_children():
                    if child in spouse:
                        #return False
                        raise Error('ERROR', 'INDIVIDUAL', 'US17',
                                    child.get_lineNum()['INDI ID'],
                                    f"Parent is married to a descendant{child.get_id()}")
                    result = dfs(child) and result
            return result

        return dfs(self)


if __name__ == "__main__":
    i1 = Individual("i1")
    date = [2018, 123, 1]
    try:
        i1.set_birthDate(date)
    except ValueError as e:
        print(e)
    print(i1.get_birthDate())
