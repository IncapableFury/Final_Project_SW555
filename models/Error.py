class Error(Exception):
    idCounter = 0
    def __init__(self,severity,className,instance,lineNum,message):
        """
        :param severity: Severity of the error. Could be either error or anomaly.
        :param className: From which class
        :param instance: From whom
        :param lineNum: From which line
        :param message: blablabla
        """
        Error.idCounter+=1
        self.id = "E"+str(Error.idCounter)
        self.severity = severity
        self.className = className
        self.instance = instance
        self.message = message
        self.lineNum = lineNum
    def test1(self):
        print("1")
    def test2(self):
        print("2")
    def call(self):
        for fun in [self.test1,self.test2]:
            fun()
        return

    
    def __str__(self):
        message = f'{self.severity}: {self.className}: {self.instance}: {self.lineNum}: {self.message}'
        return message



if __name__ == "__main__":
    e1 = Error("123",1,1,1,1)
    e1.call()
    print(e1)
#     e2 = Error("456")
#     print(e1.id,e1.message)
#     print(e2.id,e2.message)


