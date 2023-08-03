class cinema:
    def __init__(self,fname, lname, dname ):
        self.DIRECTOR = fname
        self.HERO = lname
        self.MOVIENAME = dname

obj1=cinema("logaram"," adhi","pink veeran ")     
obj2 =cinema("jishnu", "adhi", "saathan")
        
print(obj1)
print("DIRECTOR-", obj1.DIRECTOR)
print("HERO-", obj1.HERO)
print("MOVIENAME-", obj1.MOVIENAME)
           


