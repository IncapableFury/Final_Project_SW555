

class report_error:

    def __init__(self):
        self.error_list = []

    def add_error(self, error):
        self.error_list.append(error)

    def clear(self):
        self.error_list = []

    def __str__(self):
        out = ""
        for error in self.error_list:
            print(error)

        return out

    def __iter__(self):
        for error in self.error_list:
            yield error

    def check_func(self, name):
        list_mark = ["id", "Error", "change_date_formate"]
        return not name[0] == "_" and not name[0:3] == "get" and not name[0:3] == "set" and not name[0:3] == "add" and not name in list_mark


    def test_error(self, obj):
        from Error import Error
        try:
            getattr(obj, "test_error")()

        except Error as e:
            self.error_list.append(e)


    def get_error(self, obj):
        from Error import Error
        func_name = [name for name in dir(obj) if self.check_func(name)]

        for each_func in func_name:

            try:
                getattr(obj, each_func)()

            except Error as e:
                self.error_list.append(e)


if __name__ == "__main__":
    from Error import Error
    from Family import Family
    e1 = Error("123",1,2,3,4)
    e2 = Error("234",2,3,4,5)
    e3 = Error("345",3,4,5,6)
    e4 = Error("456",4,5,6,7)
    e5 = Error("567",5,6,7,8)
    all_error = report_error()
    all_error.add_error(e1)
    all_error.add_error(e2)
    all_error.add_error(e3)
    all_error.add_error(e4)
    all_error.add_error(e5)

    re1 = report_error()
    F1 = Family("01")
    re1.get_error(F1)
    print(re1)