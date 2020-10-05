from models.Individual import Individual
from models.Family import Family
from models.Gedcom import Gedcom

SUPPORT_TAGS = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
                "DIV", "DATE", "HEAD", "TRLR", "NOTE"}


class Main:
    def __init__(self):
        self.cache = dict()

    def add_file_to_cache(self, filename, gedcom) -> bool:
        self.cache[filename] = gedcom

    def peek_file(self, filename):
        try:
            self.cache[filename].peek()
        except KeyError:
            print("File not found.")
        else:
            print("File read successfully.")
        return

    def parse(self, gedcom):
        gedcom.parse()

    def validate(self, gedcom): # just a demo
        errors = []  # str
        tests = [Family.siblings_spacing, Family.multiple_births_lessOrEqual_than_5, Family.marriage_before_death] #, Family.marriage_before_divorce
        for fam_id in gedcom.get_families():
            fam = gedcom.get_families()[fam_id]
            for test in tests:
                try:
                    test(fam)
                except Exception as e:
                    errors.append(e)
        return errors


if __name__ == "__main__":
    project = Main()
    g1 = Gedcom("testing_files/Jiashu_Wang.ged", SUPPORT_TAGS)
    project.add_file_to_cache("g1", g1)
    # project.peek_file("g1")
    project.parse(g1)
    # print here
    errors = project.validate(g1)
    print(errors)
    # print(g1.get_families())
    # print(g1.get_individuals())
    # --------------------testing--------------------
