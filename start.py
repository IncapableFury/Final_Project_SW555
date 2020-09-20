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
            print("Something wrong.")


if __name__ == "__main__":
    project = Main()
    g1 = Gedcom("testing_files/Jiashu_Wang.ged", SUPPORT_TAGS)
    project.add_file_to_cache("g1", g1)
    project.peek_file("g1")
    # project3.pretty_print()
    # --------------------testing--------------------
    i1 = Individual("@I1@")
    i1.set_name("test")
    print(i1.get_name())
