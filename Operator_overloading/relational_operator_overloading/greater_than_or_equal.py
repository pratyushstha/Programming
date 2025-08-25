class SoftwareVersion : 
    def __init__(self, Version) : 
        self.Version = int(Version.replace(".", ""))
    def __ge__(self, other) : 
        return self.Version>=other.Version
v1 = SoftwareVersion("1.2.7")
v2 = SoftwareVersion("2.2.6")
print(v1>=v2)