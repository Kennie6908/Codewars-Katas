# This kata requires you to write an object that receives a file path and does operations on it.

# >>> master = FileMaster('/Users/person1/Pictures/house.png')
# >>> master.extension()
# 'png'
# >>> master.filename()
# 'house'
# >>> master.dirpath()
# '/Users/person1/Pictures/'

class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath
    def extension(self):
        periodindex = self.filepath.find(".")
        return self.filepath[periodindex + 1:]
    def filename(self):
        periodindex = self.filepath.find(".")
        lastslash = self.filepath.rfind("/")
        return self.filepath[lastslash + 1 : periodindex]
    def dirpath(self):
        lastslash = self.filepath.rfind("/")
        return self.filepath[:lastslash + 1]
