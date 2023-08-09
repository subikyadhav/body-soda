class Name:
    hero = ""
    def value1(self):
        print(self.name)
class pattam:
    pattam = ""
    def value2(self):
        print(self.pattam)
# Multiple level
class stduent(Name, pattam):
    def parents(self):
        print("Name :", self.name)
        print("pattam :", self.pattam)
stdu = stduent()
stdu.name = "kamalhaasan"
stdu.pattam = "ulaganayagan"
