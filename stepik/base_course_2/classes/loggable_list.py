import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, a):
        super(LoggableList, self).append(a)
        self.log(a)


x = LoggableList()
x.append('a')

