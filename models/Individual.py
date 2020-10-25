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

    def set_name(self, name: str) -> None:
        # if not isinstance(name, str): raise TypeError("input has to be a str type")
        self._name = name

    def set_gender(self, gender: str) -> None:
        # if not isinstance(gender, str): raise TypeError("input has to be a str type")
        self._gender = gender

    def set_birthDate(self, birth_date: list) -> None:
        # if not isinstance(birth_date, str): raise TypeError("input has to be a str type")
        if all(isinstance(v, int) for v in birth_date):
            self._birthDate = birth_date
            return
        self._birthDate = self.change_date_formate(birth_date)

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
        return int(date[2]), monthList[date[1]], int(date[0])




    def birth_before_marriage(self):
        from datetime import date
        if not self._birthDate or not self._family: raise AttributeError("Error: Missing attribute")
        #if not self._parentFamily.get_marriedDate(): raise AttributeError("Error: Missing attribute")
        for family in self.get_family():
            if not family.get_marriedDate(): raise AttributeError("Error: Missing attribute")
            timedelta = date(*family.get_marriedDate()) - date(*self._birthDate)
            if(timedelta.days <= 0): return False
        return True

    def birth_before_death(self):
        from datetime import date
        if not self._birthDate or not self._deathDate: raise AttributeError("Error: Missing attribute")

        return (date(*self._deathDate) - date(*self._birthDate)).days > 0

    def less_then_150_years_old(self):
        return self.get_age() < 150

    def no_bigamy(self) -> bool:
        if (len(self._family) <= 1): return True
        marrageAgeList = []
        birthDate = self._birthDate
        if not self._family: raise AttributeError("Erro: Missing attribute")
        for each_marrage in self._family:
            if not each_marrage.get_marriedDate(): raise AttributeError("Erro: Missing attribute")
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
                    return False
                elif ((not Age_range[1] == devorceAge) and devorceAge == None):
                    if (not (Age_range[0] < marrageAge and Age_range[1] < marrageAge)):
                        return False
                elif ((not Age_range[1] == devorceAge) and Age_range[1] == None):
                    if (not (marrageAge < Age_range[0] and devorceAge < Age_range[0])): return False
                else:
                    if (marrageAge > Age_range[0] and marrageAge < Age_range[1]):
                        return False
                    elif (devorceAge > Age_range[0] and devorceAge < Age_range[1]):
                        return False

            marrageAgeList.append((marrageAge, devorceAge))
        return True



    def aunts_and_uncles(self):
        if(not self._parentFamily): raise AttributeError("Error: missing value")
        if(not self._parentFamily.get_husband() or not self._parentFamily.get_wife()): raise AttributeError("Error: missing value")
        if(not self._parentFamily.get_husband().get_parent_family() or not self._parentFamily.get_wife().get_parent_family()): raise AttributeError("Error: missing value")
        
        dad_grand_family = self._parentFamily.get_husband().get_parent_family()
        mom_grand_family = self._parentFamily.get_wife().get_parent_family()

        for dad_side_aunt_uncle in dad_grand_family.get_children():
            for dad_side_family in dad_side_aunt_uncle.get_family():
                if(not dad_side_family.get_husband() or not dad_side_family.get_wife()): raise AttributeError("Error: missing value")
                uncle_id = dad_side_family.get_husband().get_id()
                aunt_id = dad_side_family.get_wife().get_id()
                if(uncle_id === aunt_id): return False
                for each_child in dad_side_family.get_children():
                    if(uncle_id === each_child.get_id() or aunt_id === each_child.get_id()): return False

        for mom_side_aunt_uncle in mom_grand_family.get_children():
            for mom_side_family in mom_side_aunt_uncle.get_family():
                if(not mom_side_family.get_husband() or not mom_side_family.get_wife()): raise AttributeError("Error: missing value")
                uncle_id = mom_side_family.get_husband().get_id()
                aunt_id = mom_side_family.get_wife().get_id()
                if(uncle_id === aunt_id): return False
                for each_child in mom_side_family.get_children():
                    if(uncle_id === each_child.get_id() or aunt_id === each_child.get_id()): return False
        
        return True



    def first_cousins_should_not_marry(self):
        if self.get_parent_family() and self.get_parent_family().get_husband() and \
                self.get_parent_family().get_husband().get_parent_family():
            daddy = self.get_parent_family().get_husband()
            daddy_siblings = self.get_parent_family().get_husband().get_parent_family().get_children()[:]
            daddy_siblings.remove(daddy)  # if singleton, this loop does nothing
            for daddy_sibling in daddy_siblings:
                daddy_sibling_families = daddy_sibling.get_family()  # consider past families
                for child_fam in daddy_sibling_families:
                    for first_cousin in child_fam.get_children():
                        if first_cousin == self: return False
        if self.get_parent_family() and self.get_parent_family().get_wife() and \
                self.get_parent_family().get_wife().get_parent_family():
            mummy = self.get_parent_family().get_wife()
            mummy_siblings = self.get_parent_family().get_wife().get_parent_family().get_children()[:]
            mummy_siblings.remove(mummy)  # if singleton, this loop does nothing
            for mummy_sibling in mummy_siblings:
                mummy_sibling_families = mummy_sibling.get_family()  # consider past families
                for mummy_sibling_fam in mummy_sibling_families:
                    for first_cousin in mummy_sibling_fam.get_children():
                        if first_cousin == self: return False
        return True

    def no_marriages_to_descendants(self):  # dfs in dfs
        if not self.get_family():
            return True
        spouse = []
        if self.get_gender() == "M":
            for past_family in self.get_family():
                spouse.append(past_family.get_wife())
        else:
            for past_family in self.get_family():
                spouse.append(past_family.get_husband())
        print(list(map(lambda x: x.get_id(), spouse)))

        def dfs(next_member):
            print(next_member.get_id())
            if not next_member.get_family():
                return True
            result = True
            for family in next_member.get_family():
                for child in family.get_children():
                    if child in spouse:
                        return False
                    result = dfs(child) and result
            return result

        return dfs(self)
