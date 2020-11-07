class Gedcom:
    def __init__(self, path, supportTags):
        self._supportTags = supportTags
        self._individuals = {}
        self._families = {}
        self._data = self.readfile(path)

    def readfile(self, path):
        res = [[], [], []]  # [[level, tag, arguments], [start indices of indi], [start indices of fam]]
        f = open(path, "r")
        index = 0
        for line in f:
            level, tag, arguments = self.parseline(line)
            if tag not in self._supportTags:  # skip unsupported tags
                continue
            res[0].append([level, tag, arguments])
            if tag == "INDI":
                res[1].append(index)
            elif tag == "FAM":
                if not res[2]:
                    res[1].append(index)  # the first start index for family is the last end index for indis
                res[2].append(index)
            index += 1
        res[2].append(index)  # end index for fam
        f.close()
        return res

    def parseline(self, line):
        line = line.split()
        level, tag, arguments = line[0], line[1], line[2:]
        if arguments and arguments[0] in ["INDI", "FAM"]:
            tag, arguments = arguments[0], tag
        return level, tag, arguments

    def peek(self):
        for line in self._data[0]:
            level, tag, arguments = line[0], line[1], line[2:]
            print("    " * int(level), level, tag, arguments)

    def get_data(self):
        return self._data

    def get_individuals(self):
        return self._individuals

    def get_families(self):
        return self._families

    def parse(self):
        from models.Individual import Individual
        from models.Family import Family
        offset = 0
        for i in range(len(self._data[1]) - 1):  # enumerate individuals
            start_index = self._data[1][i]
            end_index = self._data[1][i + 1]
            # print(self._data[0][start_index:end_index])
            # TODO: check deplicated ids
            id = self._data[0][start_index][2]
            if id in self._individuals:
                offset += 1
                id = "@I" + str(int(id[2:-1]) + offset) + "@"
            new_indi = Individual(id)
            self._individuals[id] = new_indi
            # print(start_index, end_index)
            for j in range(start_index + 1, end_index):
                level, tag, arguments = self._data[0][j]
                if tag == "NAME":
                    new_indi.set_name("".join(arguments))
                elif tag == "SEX":
                    new_indi.set_gender(arguments[0])
                elif tag == "BIRT":  # set missing dates to Jan/01
                    j += 1
                    level, tag, arguments = self._data[0][j]
                    try:
                        new_indi.set_birthDate(arguments)
                    except ValueError as e:
                        print(e)  # TODO:how to handle error?
                elif tag == "DEAT":
                    j += 1
                    level, tag, arguments = self._data[0][j]
                    new_indi.set_deathDate(arguments)
                elif tag == "FAMS":
                    if arguments[0] not in self._families:
                        new_fam = Family(arguments[0])
                        self._families[arguments[0]] = new_fam
                    new_indi.add_to_family(self._families[arguments[0]])
                elif tag == "FAMC":
                    if arguments[0] not in self._families:
                        new_fam = Family(arguments[0])
                        self._families[arguments[0]] = new_fam
                    new_indi.set_parentFamily(self._families[arguments[0]])
        offset = 0
        for i in range(len(self._data[2]) - 1):
            start_index = self._data[2][i]
            end_index = self._data[2][i + 1]
            # print(self._data[0][start_index:end_index])
            id = self._data[0][start_index][2]
            # if id in self._families:  #TODO: handle duplicate
            #     offset+=1
            #     id = "@F" + str(int(id[2:-1]) + offset) + "@"
            new_fam = Family(id)
            self._families[id] = new_fam
            for j in range(start_index + 1, end_index):
                level, tag, arguments = self._data[0][j]
                # print(level, tag, arguments)
                if tag == "HUSB":
                    new_fam.set_husband(self._individuals[arguments[0]])
                elif tag == "WIFE":
                    new_fam.set_wife(self._individuals[arguments[0]])
                elif tag == "CHIL":
                    new_fam.add_child(self._individuals[arguments[0]])
                elif tag == "MARR":
                    j += 1
                    level, tag, arguments = self._data[0][j]
                    # print(level, tag, arguments)
                    try:
                        new_fam.set_marriedDate(arguments)
                    except:
                        continue
                elif tag == "DIV":
                    j += 1
                    level, tag, arguments = self._data[0][j]
                    # print(level, tag, arguments)
                    try:
                        new_fam.set_divorcedDate(arguments)
                    except:
                        continue

    '''
    Move this function from individual.py to gedcom.py
    '''

    def dates_before_current_date(self):
        from datetime import date
        today = date.today()
        for _, indi in self._individuals:
            if not indi.get_birthDate(): raise AttributeError("Error: missing birthdate for individual")
            if not (today - date(indi.get_birthDate())).days < 0: return False
            if not indi.get_deathDate() == None:
                if not (today - date(indi.get_deathDate())).days < 0: return False

        for _, fam in self._families:
            if not fam.get_marriedDate(): raise AttributeError("Error: missing marriedDate for family")
            if not (today - date(fam.get_marriedDate())).days < 0: return False
            if not fam.get_divorcedDate() == None:
                if not (today - date(fam.get_divorcedDate())).days < 0: return False

        return True

    def Unique_IDs(self):
        pass

    # Finshed in mainfunction.

    def unique_name_and_birth_date(self):
        dic = set()
        for indi in self._individuals.values():
            if indi.get_birthDate():
                key = indi.get_name().replace("/", "") + "a".join(list(map(str, indi.get_birthDate())))
                # print(key)
                if key not in dic:
                    dic.add(indi)
                else:
                    return False
        return True

    def unique_families_by_spouses(self):
        """user story 24 No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file """
        check_list = []
        for _, family in self._families:
            if not family.get_husband() or not family.get_wife(): raise AttributeError("no husband or wife")
            if not family.get_husband().get_name() or not family.get_wife().get_name(): raise AttributeError(
                "no husband or wife name")
            if not family.get_marriedDate(): raise AttributeError("no marriage date")
            this_fam_info = [family.get_husband().get_name(), family.get_wife.get_name(), family.get_marriedDate()]
            if check in check_list: return False
            check_list.append(this_fam_info)

        return True

    def unique_first_names_in_families(self):
        """user story 25 No more than one child with the same name and birth date should appear in a family"""

        for _, family in self._families:
            check_list = []
            for child in family.get_children():
                if not child.get_name() or not child.get_birthDate(): raise AttributeError(
                    "no name or birthdate for child")
                child_info = [child.get_name(), child.get_birthDate()]
                if child_info in check_list: return False
                check_list.append(child_info)

        return True

    def include_individual_ages(self):
        pass

    def corresponding_entries(self):
        """ user story 26 the information in the individual and family records should be consistent."""
        for key_id, indi in self._individuals:
            if indi.get_parentFamily():
                flag = False
                for child in indi.get_parentFamily().get_children():
                    if child.get_id() == key_id: flag = True
                if not flag: return False

            for fam in indi.get_family():
                if not fam.get_husband() and not fam.get_wife(): return False
                if not (fam.get_husband().get_id() == key_id or fam.get_wife().get_id() == key_id): return False

        for key_id, fam in self._families:
            if fam.get_husband():
                flag = False
                for check_fam in fam.get_husband().get_family():
                    if check_fam.get_id() == key_id: flag = True
                if not flag: return False

            if fam.get_wife():
                flag = False
                for check_fam in fam.get_wife().get_family():
                    if check_fam.get_id == key_id: flag = True
                if not flag: return False

            for child in fam.get_children():
                if not child.get_parentFamily(): return False
                if child.get_parentFamily().get_id() == key_id: return False

        return True

        if not self.get_children: raise AttributeError("no children")
        if not self.get_wife or self.get_husband: raise AttributeError("no wife or husband found for spouse")
        if self._individuals().get_id() == self._families().get_husband().get_id() or self._individuals().get_id() == self._families().get_wife().get_id():
            return True
        for child in self._families.get_children():
            if self._individuals().get_id() == self._families().get_id() and self._individuals.get_id() == child:
                return True
        return False
        raise ValueError(
            "Error corresponding entries: All family roles (spouse, child) specified in an individual record should have corresponding entries in the corresponding family, the information in the individual and family records should be consistent.")


        def list_deceased(self):
            """us 29 list all deceased individuals in a gedcom file"""
            deceasedPeople=[]
            if self._individuals.get_deathDate()==None: raise AttributeError("no one deceased")
            for individual in self._individuals():
                if self.get_deathDate() != None:
                    deceasedPeople.append(self.get_id())
            return deceasedPeople


        def list_living_married(self):
            """list all living married people in a Gedcom file"""
            marriedPeople=[]
            if not self.get_wife or self.get_husband: raise AttributeError("no wife or husband found for spouse")
            for family in self._families():
                if self.get_husband==self.get_id and self.husband.get_deathDate == None:
                    marriedPeople.append(self.get_husband)
                if self.get_wife==self.get_id and self.get_wife.get_deathDate==None:
                    marriedPeople.append(self.get_wife)
            return marriedPeople

    def list_recent_deaths(self):
        from datetime import date
        from datetime import timedelta
        deathPeople = []
        for indi in self._individuals.values():
            if indi.get_deathDate[0]>(date.today() - timedelta(30)).strftime("%Y"):
                deathPeople.append(indi.get_name)
            elif indi.get_deathDate[0]==(date.today() - timedelta(30)).strftime("%Y"):
                if indi.get_deathDate[1]>(date.today() - timedelta(30)).strftime("%m"):
                    deathPeople.append(indi.get_name)
                elif indi.get_deathDate[1]==(date.today() - timedelta(30)).strftime("%m"):
                    if indi.get_deathDate[2]>(date.today() - timedelta(30)).strftime("%d"):
                        deathPeople.append(indi.get_name)

        return deathPeople

    def list_multiple_births(self):
        dic = {}
        multiple_birth = []
        for indi in self._individuals.values():
            key = indi.get_parent_family().get_id()+str(indi.get_birthDate())
            if key in dic:
                dic[key].append(indi.get_id())
            else:
                dic[key] = [indi.get_id()]
        for list1 in dic.values():
            if len(list1)>1 :
                multiple_birth.append(list1)
        return multiple_birth




if __name__ == "__main__":
    # from datetime import datetime, date
    # # from datetime import timedelta
    # # SUPPORT_TAGS = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
    # #                 "DIV", "DATE", "HEAD", "TRLR", "NOTE"}
    # # g1 = Gedcom("../testing_files/test_date_validation.ged", SUPPORT_TAGS)  # testing_files/Jiashu_Wang.ged
    # # g1.peek()
    # # g1.parse()
    # # print(g1.get_individuals().keys(), g1.get_families().keys())
    # # print(str(g1.get_individuals()["@I3@"].get_parent_family().get_id())+str(g1.get_individuals()["@I2@"].get_birthDate()))
    # # g1.unique_name_and_birth_date()

    key = 1
    value = 10
    dic= {}
    dic[key] = value
    value = 20
    list = []
    list.append([1,2])
    print(type([1,2]).__name__ =='list')