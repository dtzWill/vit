from formatter.due import Due

class DueRelative(Due):
    def format(self, dt):
        return self.relative(dt)
