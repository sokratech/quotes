class Quote:
    def __init__(self, row):
        self._id = row[0]
        self._content = row[1]
        self._category = row[2]

    def id(self):
        return self._id

    def content(self):
        return self._content.decode("utf-8")

    def category(self):
        return self._category.decode("utf-8")

    def to_string(self):
        return "<{}> {} - {}".format(self.id(), self.content(), self.category())
