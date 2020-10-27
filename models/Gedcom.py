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
        iddic = set()
        offset = 0
        for i in range(len(self._data[1]) - 1):  # enumerate individuals
            start_index = self._data[1][i]
            end_index = self._data[1][i + 1]
            # print(self._data[0][start_index:end_index])
            #TODO: check deplicated ids
            id = self._data[0][start_index][2]
            new_indi = Individual(id)
            if id not in iddic:
                iddic.add(id)
            else :
                offset+=1
            self._individuals["@I"+str(int(id[2:-1])+offset)+"@"] = new_indi
            # print(start_index, end_index)
            for j in range(start_index + 1, end_index):
                level, tag, arguments = self._data[0][j]
                if tag == "NAME":
                    new_indi.set_name("".join(arguments))
                elif tag == "SEX":
                    new_indi.set_gender(arguments[0])
                elif tag == "BIRT":
                    j += 1
                    level, tag, arguments = self._data[0][j]
                    new_indi.set_birthDate(arguments)
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
        offset2 = 0
        for i in range(len(self._data[2]) - 1):
            start_index = self._data[2][i]
            end_index = self._data[2][i + 1]
            # print(self._data[0][start_index:end_index])
            id = self._data[0][start_index][2]
            if id not in self._families:
                new_fam = Family("@F"+str(int(id[2:-1])+offset2)+"@")
                self._families["@F"+str(int(id[2:-1])+offset2)+"@"] = new_fam
            else:
                offset2+=1
            fam = self._families["@F"+str(int(id[2:-1])+offset2)+"@"]
            for j in range(start_index + 1, end_index):
                level, tag, arguments = self._data[0][j]
                # print(level, tag, arguments)
                if tag == "HUSB":
                    fam.set_husband(self._individuals[arguments[0]])
                elif tag == "WIFE":
                    fam.set_wife(self._individuals[arguments[0]])
                elif tag == "CHIL":
                    fam.add_child(self._individuals[arguments[0]])
                elif tag == "MARR":
                    j += 1
                    level, tag, arguments = self._data[0][j]
                    # print(level, tag, arguments)
                    try:
                        fam.set_marriedDate(arguments)
                    except:
                        continue
                elif tag == "DIV":
                    j += 1
                    level, tag, arguments = self._data[0][j]
                    # print(level, tag, arguments)
                    try:
                        fam.set_divorcedDate(arguments)
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
                key = indi.get_name().replace("/","")+"a".join(list(map(str,indi.get_birthDate())))
                #print(key)
                if key not in dic:
                    dic.add(indi)
                else:
                    return False
        return True

    
    def unique_families_by_spouses(self):
        """user story 24 No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file """
        if not self._husband or not self._wife: raise AttributeError("no husband or wife")
        if not self._husband.get_marriedDate and not self._wife.get_marriedDate: raise AttributeError("no marriage date")
        for anotherFam in self.get_families():
            if(self.get_husband == anotherFam.get_husband and self.get_wife == anotherFam.get_wife and self.get_marriedDate == anotherFam.get_marriedDate and self.get_id != anotherFam.get_id):
                return False
                raise ValueError("Error unique families by spouses: Marriage date of " + self.get_id() + " have the same marriage date as other family and same spouces." +self.get_husband+ self.get_wife)
        return True

    def unique_first_names_in_families(self):
        """user story 25 No more than one child with the same name and birth date should appear in a family"""
        childName=[]
        childBirthday=[]
        if not self.get_children: raise AttributeError("no children") 
        if not self.get_children.get_birthDate:  raise AttributeError("no chlidren birthday")
        for child in self.get_families().get_children():
            childName.append(child.get_name().split(" ")[0])
            childBirthday.append(child.get_birthDate())
        for x in range(0, len(childName)):
            for y in range(x+1, len(childName)):
                if(childName[x]==childName[y] and childBirthday[x]==childBirthday[y]):
                    return False
                    raise ValueError("Error unique first names in families: No more than one child with the same name in family "+self.get_id)
        return True

    def include_individual_ages(self):
        pass

    def corresponding_entries(self):
        """ user story 26 the information in the individual and family records should be consistent."""
        if not self.get_children: raise AttributeError("no children")
        if not self.get_wife or self.get_husband: raise AttributeError("no wife or husband found for spouse")
        if self._individuals().get_id()==self._families().get_husband().get_id() or self._individuals().get_id()==self._families().get_wife().get_id():
            return True 
        for child in self._families.get_children():
            if self._individuals().get_id()==self._families().get_id() and self._individuals.get_id()==child:
                return True
        return False
        raise ValueError("Error corresponding entries: All family roles (spouse, child) specified in an individual record should have corresponding entries in the corresponding family, the information in the individual and family records should be consistent.")


# if __name__ == "__main__":
#     SUPPORT_TAGS = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
#                     "DIV", "DATE", "HEAD", "TRLR", "NOTE"}
#     g1 = Gedcom("../testing_files/Jiashu_Wang.ged", SUPPORT_TAGS)#testing_files/Jiashu_Wang.ged
#     # for i in range(len(g1.get_data()[0])):
#     #     print(i,g1.get_data()[0][i])
#     # for i in range(len(g1.get_data()[1])):
#     #     print(g1.get_data()[1][i])
#     # print(g1.get_data(),sep='/n')
#     g1.parse()
#     # print(g1.get_individuals(),g1.get_families())
#     # print(len(g1.get_individuals()),g1.get_individuals()["@I2@"].get_birthDate())
#     g1.unique_name_and_birth_date()
#     # print("what")
#     offset = 11
#     id = "@I123@"
#     print("@I"+str(int(id[2:-1])+offset)+"@")
#     print(g1.get_families().values())