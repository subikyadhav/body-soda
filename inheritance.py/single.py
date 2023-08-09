class films:
    company = " cinema"
    production = "RKFI"
 
    def personal_details(self):
        print("subikshan is one of the best director in tamil cinema industry 🎬🎬🎥🎬🎬")
 
 
class RKFI(films):
    def __init__(self):
        self.name = "films"
        self.year = 1998
 
    def product_details(self):
        print("Name     : ", self.name)                                                                                                        
        print("Year     : ", self.year)
        print("Company  : ", self.company)
        print("production  : ", self.production)
         