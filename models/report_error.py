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


if __name__ == "__main__":
    from Error import Error
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