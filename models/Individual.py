class Individual:
    def __init__(self, id):
        self.id = id
        self._name = None
        self._gender = None
        self._birthDate = None
        self._deathDate = None
        self._children = []
        self._spouse = None

    def set_name(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name if self._name else "NA"

    # ---------------------shit testing below---------------------

    def dates_before_current_date(self):
        pass

    def birth_before_marriage(self):
        pass

    def birth_before_death(self):
        pass

    def marriage_before_divorce(self):
        pass

    def marriage_before_death(self):
        pass

    def divorce_before_death(self):
        pass

    def less_then_150_years_old(self):
        pass

    def birth_before_marriage_of_parents(self):
        pass

    def birth_before_death_of_parents(self):
        pass

    def marriage_after_14(self):
        pass

    def no_bigamy(self):
        pass

    def parents_not_too_old(self):
        pass
