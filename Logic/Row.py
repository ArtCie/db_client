class Row:
    """Class represents row object, contain list of row content"""
    def __init__(self, contents):
        """Constructor takes one row - list of content"""
        self.contents = contents

    def check_casts(self, row_types):
        """Method checks whether all types and contents are valid"""
        for ind, type_ in enumerate(row_types):
            if self.try_cast(type_, self.contents[ind]) is False:
                return [type_, self.contents[ind]]
            self.contents[ind] = type_(self.contents[ind])
        return True

    @staticmethod
    def try_cast(type_, content):
        """Method tries to cast specifies value into given type"""
        try:
            type_(content)
            return True
        except ValueError:
            return False
