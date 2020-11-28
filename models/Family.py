#TODO: import error class
from Gedcom import Gedcom
class Family(Gedcom):
    '''
    This is the class for Family.
    id is the only variable that is required. If other variable does not exist, it would return None
    If children does not exist, it would return an empty list
    all date value are passed in as str, and saved as tuple with formate (year, month, day)
    '''
    from Error import Error 
    def __init__(self, id: str):
        from report_error import report_error
        self.id = id
        self._husband = None
        self._wife = None
        self._marriedDate = None
        self._divorced = None
        self._children = []
        self._lineNum = {}

    def get_lineNum(self) -> {}:
        return self._lineNum

    def get_id(self) -> str:
        return self.id

    def get_husband(self):
        return self._husband

    def get_wife(self):
        return self._wife

    def get_marriedDate(self) -> tuple:
        return self._marriedDate

    def get_divorcedDate(self) -> tuple:
        return self._divorced

    def get_children(self) -> list:
        return self._children

    def set_lineNum(self, lineNumberDict)->None:
         self._lineNum = lineNumberDict

    def set_husband(self, husband) -> None:
        ##if not isinstance(husband, Individual): raise TypeError("input has to be a Individual type")
        self._husband = husband

    def set_wife(self, wife) -> None:

        ##if not isinstance(wife, Individual): raise TypeError("input has to be a Individual type")
        self._wife = wife

    def set_marriedDate(self, married_date: tuple) -> None:

        ##if not isinstance(married_date, str): raise TypeError("input has to be a str type")
        if all(isinstance(v, int) for v in married_date):
            self._marriedDate = married_date
            return
        self._marriedDate = self.change_date_formate(married_date)

    def set_divorcedDate(self, divorced_date: tuple) -> None:

        ##if not isinstance(divorced_date, str): raise TypeError("input has to be a str type")
        if all(isinstance(v, int) for v in divorced_date):
            self._divorcedDate = divorced_date
            return
        self._divorced = self.change_date_formate(divorced_date)

    def set_children(self, children_list: list) -> None:
        ##if not isinstance(children_list, list): raise TypeError("input has to be a list type")
        self._children = children_list

    def add_child(self, child) -> None:
        '''
        this function would add one kid into the children list
        '''
        ##if not isinstance(child, Individual): raise TypeError("input has to be a Individual type")
        self._children.append(child)

    def change_date_formate(self, date: list) -> tuple:
        '''
        Would take the string input and convert it into a int tuple:(year, month, day)
        '''
        monthList = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9,
                     "OCT": 10, "NOV": 11, "DEC": 12}
        return int(date[2]), monthList[date[1]], int(date[0])

    def multiple_births_lessOrEqual_than_5(self):  # cannot catch multi multiples; not sure if need to
        from datetime import date
        today = date.today()
        try:
            births = sorted(
                list(map(lambda i: abs((date(*i) - today).days), [x.get_birthDate() for x in self.get_children()])))
        except AttributeError:
            err = Error("ERROR", "FAMILY", "US14", "Missing birthdate for children", self._lineNum)
            Gedcom.error_report.add_error(err)

        if len(births) <= 5: return True
        multi, sameDay, pre = 0, 0, births[0]
        for i in range(len(births)):
            if pre == births[i]:
                multi += 1
                sameDay += 1
            elif births[i] - pre == 1:
                multi, sameDay = sameDay + 1, 1
            else:
                multi, sameDay = 1, 1
            pre = births[i]
            if multi >= 5:
                err = Error("ANOMALY", "FAMILY", "US14", f'{multi} births where maxium is 5', self._lineNum)
                Gedcom.error_report.add_error(err)
        return True

    def parents_not_too_old(self):
        if not self._husband or not self._wife: raise AttributeError("Error: missing husband or wife")

        if not self._husband.get_age() or not self._wife.get_age(): raise AttributeError(
            "Error: missing age for husband or wife")

        if not self._husband.get_age() or not self._wife.get_age(): raise AttributeError("Error: missing age for husband or wife")

        wife_age = self._wife.get_age()
        husband_age = self._husband.get_age()
        for child in self._children:
            if not child.get_age(): raise AttributeError("Error: missing child age")
            wife_diff = wife_age - child.get_age()
            husband_diff = husband_age - child.get_age()
            if wife_diff >= 60 or husband_diff >= 80: return False
        return True

    def marriage_before_divorce(self):
        from datetime import date
        marriage = self.get_marriedDate()
        divorce = self.get_divorcedDate()
        if not marriage: raise AttributeError("Missing marriage date")
        if not divorce: return True
        timedelta = date(*marriage) - date(*divorce)
        return timedelta.days < 0

    def marriage_after_14(self) -> bool:
        from datetime import date

        if not self._husband or not self._wife or not self._marriedDate: raise AttributeError(
            "Missing husband/wife/marriedDate")
        if not self._husband.get_birthDate() or not self._wife.get_birthDate(): raise AttributeError(
            "Missing birthdate for husband/wife")

        if not self._husband or not self._wife or not self._marriedDate: raise AttributeError("Missing husband/wife/marriedDate")
        if not self._husband.get_birthDate() or not self._wife.get_birthDate(): raise AttributeError("Missing birthdate for husband/wife")
        husbandMarryAge = (date(*self._marriedDate) - date(*self._husband.get_birthDate())).days // 365
        wifeMarryAge = (date(*self._marriedDate) - date(*self._wife.get_birthDate())).days // 365
        return husbandMarryAge > 14 and wifeMarryAge > 14

    def marriage_before_death(self):
        from datetime import date

        if not self._husband or not self._wife or not self.get_marriedDate(): raise AttributeError(
            "Missing husband/wife/marriedDate")
        if not self._husband.get_deathDate() and not self._wife.get_deathDate(): return True

        death = None
        if not self._husband.get_deathDate():
            death = self._wife.get_deathDate()
        elif not self._wife.get_deathDate():
            death = self._husband.get_deathDate()

        if not self._husband or not self._wife or not self.get_marriedDate(): raise AttributeError("Missing husband/wife/marriedDate")
        if not self._husband.get_deathDate() and not self._wife.get_deathDate(): return True

        death = None
        if not self._husband.get_deathDate(): death = self._wife.get_deathDate()
        elif not self._wife.get_deathDate(): death = self._husband.get_deathDate()

        else:
            if self._husband.get_deathDate() > self._wife.get_deathDate():
                death = self._wife.get_deathDate()
            else:
                death = self._husband.get_deathDate()
        marriage = self._marriedDate
        timedelta = date(*marriage) - date(*death)
        return timedelta.days <= 0

    def divorce_before_death(self) -> bool:
        from datetime import date
        if not self._husband or not self._wife: raise AttributeError("Missing husband/wife")
        if not self._husband.get_deathDate() and not self._wife.get_deathDate(): return True
        if not self._divorced: return True

        deathdays = None
        if not self._husband.get_deathDate():
            deathdays = (date(*self._divorced) - date(*self._husband.get_deathDate())).days
        elif not self._wife.get_deathDate():
            deathdays = (date(*self._divorced) - date(*self._wife.get_deathDate())).days
        else:
            deathdays = (date(*self._divorced) - date(*self._husband.get_deathDate())).days
            if deathdays > (date(*self._divorced) - date(*self._wife.get_deathDate())).days:
                deathdays = (date(*self._divorced) - date(*self._wife.get_deathDate())).days

        return deathdays < 0


    def birth_before_marriage_of_parents(self):
        if not self._husband or not self._wife: raise AttributeError("Missing husband/wife")
        if not self.get_marriedDate():raise AttributeError("Missing marrageDate")

        for c in self._children:
            if not c.get_birthDate(): raise AttributeError("Missing child birthDate")
            if c.get_birthDate() <= self.get_marriedDate(): return False
        return True

    def birth_before_death_of_parents(self):
        if not self._husband or not self._wife: raise AttributeError("Missing husband/wife")
        if not self._husband.get_deathDate() and not self._wife.get_deathDate(): return True
        if len(self._children) == 0: return True
        death = self._wife.get_deathDate()
        hDeath = self._husband.get_deathDate()


        if not hDeath:
            for c in self._children:
                if c.get_birthDate() > death: return False
            return True

        hDeath = hDeath + (0, 9, 0)
        if hDeath[1] > 12:
            hDeath[1] = hDeath[1] % 12
            hDeath[0] = hDeath[0] + 1
        if not death:
            for c in self._children:
                if c.get_birthDate() > hDeath: return False
            return True

        if hDeath < death:

            if not death and not hDeath:
                return True
        if hDeath:
            hDeath = tuple(map(sum, zip(hDeath, (0,9,0))))
            if hDeath[1] > 12:
                hDeath[1] = hDeath[1] % 12
                hDeath[0] = hDeath[0] + 1
        if death is None or hDeath < death:

            death = hDeath

        for c in self._children:
            if c.get_birthDate() > death: return False
        return True

    def siblings_spacing(self):
        from datetime import date
        threshold = [1, 240]  # 8 month is ambiguous, let's just assume 8*30=240 days
        n = len(self.get_children())
        if n < 2: return True
        sumOfDifference = 0
        for i in range(n - 1):
            timedelta = date(*self.get_children()[i].get_birthDate()) - date(*self.get_children()[i + 1].get_birthDate())
            sumOfDifference += abs(timedelta.days)
        return not (threshold[0] < sumOfDifference // (n - 1) < threshold[1])

    def fewer_than_15_siblings(self):
        """
        if self._children is empty, it is a empty list which the length is 0
        :return: boolean if the length of self._children is less then 15
        """
        return len(self._children) < 15

    def correct_gender_for_role(self):
        """
        throw error when missing husband/wife or missing gender of husband/wife
        :return: boolean from compare the string of husband and wife gender
        """
        if (not self._husband or not self._wife): raise AttributeError("missing husband or wife")
        if (not self._husband.get_gender() or not self._wife.get_gender()): raise AttributeError(
            "missing gender of husband or wife")
        return self._husband.get_gender() == "M" and self._wife.get_gender() == "F"

    def male_last_names(self):
        if not self._husband: raise AttributeError("Missing Father")
        if not self._husband.get_name(): raise AttributeError("Missing Father's name")

        check_last_name = self._husband.get_name().split(' ')[1]
        def dfs(family, last_name):
            flag = True
            for child in family.get_children():
                if child.get_gender() == None: raise AttributeError("child's gender is not set yet")
                
                if child.get_gender() == "F": continue
                if not child.get_name(): raise AttributeError("Child's name is missing")
                if child.get_name().split(' ')[1] != last_name: return False
                for fam in child.get_family():
                    flag = dfs(fam) and flag
            return flag

        return dfs(self, check_last_name)


    def siblings_should_not_marry(self):
        if not self._husband or not self._wife: raise AttributeError("Missing husband or wife")
        if not self._husband.get_parent_family() and not self._wife.get_parent_family(): raise AttributeError("Missing husband and wife parent")
        return not self._husband.get_parent_family().get_id() == self._wife.get_parent_family().get_id()

    def order_siblings_by_age(self):
        """
        Need one extra step which filters out the Nones. Not sure if necessary.
        :return: list of references in the order of descending age
        """
        res = sorted(self.get_children(), key=lambda x: x.get_age(days=True), reverse=True)
        return list(filter(lambda x: x.get_birthDate() != None, res))

    def list_all_husbands(self):
        """US 52 lists all husbands"""
        husbandslist=[]
        if not self.get_husband: raise AttributeError("no husband found")
        for family in self._families():
            if self.get_husband==self.get_id:
                husbandslist.append(self.get_husband)
        return husbandslist 

    def list_all_wives(self):
        """US 53 lists all wives"""
        wiveslist=[]
        if not self.get_wife: raise AttributeError("no wives found")
        for family in self._families():
            if self.get_wife==self.get_id:
                wiveslist.append(self.get_wife)
        return wiveslist



if __name__ == "__main__":
    pass

    # from models.Individual import Individual

    #from models.Individual import Individual
    # ---------------------------testing cases below---------------------------