class cinema:
    director = ""
    producer= ""
    musicDirector = ""
    hero = ""
    heroin = ""
    villain = ""

    def getFullName(self):
        return self.director
        + " " + self.producer


obj1 = cinema()
obj2 = cinema()

obj1.director = "SUBIKSHAN"
obj1.producer = "RKFI"
obj1.musicDirector = "ANIRUDH"
obj1.hero = "ULAGANAYAGAN KAMAL HAASAN"
obj1.heroin = "SREE DEVI"
obj1.villain = "SANJAY DUTT"

obj2.director = "SUBIKYADHAV"
obj2.producer = "7 SCREEN STUDIOS"
obj2.musicDirector = "PRITHIV"
obj2.hero = "THALAPATHY VIJAY"
obj2.heroin = "3sha"
obj2.villain = "RAGHAVA LAWRENCE"

print(obj1)
print("director -", obj1.director)
print("producer -", obj1.producer)
print("musicDirector -", obj1.musicDirector, "\n")
print("hero - ", obj1.hero)
print("heroin -", obj1.heroin)
print("villain - ", obj1.villain)
print("FullName -", obj1.getFullName())
print("---------------------------")


print(obj2)
print("director -", obj2.director)
print("producer -", obj2.producer)
print("musicDirector - ", obj2.musicDirector, "\n")
print("hero - ", obj2.hero)
print("heroin -", obj2.heroin)
print("villain - ", obj2.villain)
print("FullName -", obj2.getFullName())
print("---------------------------")