class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, a):
        if a > 0:
            super(PositiveList, self).append(a)
        else:
            raise NonPositiveError()