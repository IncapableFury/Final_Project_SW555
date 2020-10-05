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

    def validate(self, gedcom):  # just a demo
        errors = []  # str
        tests_for_family = [Family.siblings_spacing, Family.multiple_births_lessOrEqual_than_5,
                            Family.marriage_before_death,
                            Family.birth_before_death_of_parents, Family.marriage_before_divorce,
                            Family.marriage_after_14, Family.divorce_before_death,
                            Family.birth_before_marriage_of_parents]  # , Family.marriage_before_divorce
        tests_for_individuals = [Individual.dates_before_current_date, Individual.birth_before_marriage,
                                 Individual.birth_before_death, Individual.less_then_150_years_old,
                                 Individual.no_bigamy, Individual.parents_not_too_old]
        for fam_id in gedcom.get_families():
            fam = gedcom.get_families()[fam_id]
            for test in tests_for_family:
                try:
                    test(fam)
                except Exception as e:
                    errors.append(e)
        for indi_id in gedcom.get_individuals():
            indi = gedcom.get_individuals()[indi_id]
            for test in tests_for_individuals:
                try:
                    test(indi)
                except Exception as e:
                    errors.append(e)
        print(len(errors))
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
