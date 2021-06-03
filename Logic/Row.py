class Row:
    def __init__(self, contents):
        self.contents = contents

    def check_casts(self, row_types):
        for ind, type_ in enumerate(row_types):
            if self.try_cast(type_, self.contents[ind]) is False:
                return False
            self.contents[ind] = type_(self.contents[ind])
        return True

    @staticmethod
    def try_cast(type_, content):
        try:
            type_(content)
            return True
        except ValueError:
            return False
