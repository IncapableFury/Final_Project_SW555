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
        for i in range(len(self._data[1]) - 1):  # enumerate individuals
            start_index = self._data[1][i]
            end_index = self._data[1][i + 1]
            # print(self._data[0][start_index:end_index])
            id = self._data[0][start_index][2]
            new_indi = Individual(id)
            self._individuals[id] = new_indi
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
        for i in range(len(self._data[2]) - 1):
            start_index = self._data[2][i]
            end_index = self._data[2][i + 1]
            # print(self._data[0][start_index:end_index])
            id = self._data[0][start_index][2]
            if id not in self._families:
                new_fam = Individual(id)
                self._families[id] = new_fam
            fam = self._families[id]
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


    def Unique_IDs(self):
        pass 

    def unique_name_and_birth_date(self):
        pass

    def unique_families_by_spouses(self):
        pass

    def unique_first_names_in_families(self):
        pass

    def include_individual_ages(self):
        pass

    def corresponding_entries(self):
        pass



# if __name__ == "__main__":
    # SUPPORT_TAGS = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
    #                 "DIV", "DATE", "HEAD", "TRLR", "NOTE"}
    # g1 = Gedcom("../testing_files/Jiashu_Wang.ged", SUPPORT_TAGS)
    # for i in range(len(g1.get_data()[0])):
    #     print(i,g1.get_data()[0][i])
    # for i in range(len(g1.get_data()[1])):
    #     print(g1.get_data()[1][i])
    # print(g1.get_data(),sep='/n')
    # g1.parse()
    # print(len(g1.get_individuals()),g1.get_individuals()["@I2@"].get_birthDate())
