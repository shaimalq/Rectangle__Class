class rectangle () :
    def __init__(self , largeur , longueur): 
        self.largeur  = largeur
        self.longueur = longueur 


    def iscarre (self):
       if  (self.largeur == self.longueur) :
           return "il s'agit d'un carre"
       else:
           return "il  ne s'agit pas d'un carre"
       
       
    def air (self):
        return  self.largeur * self.longueur



    def perimetre(self):
        return 2 * (self.largeur * self.longueur)
    
    def info (self):
        print(f"largeur:{self.largeur}\nlongueur:{self.longueur}\nperimetre:{2 * (self.largeur * self.longueur)}\nair: {self.largeur * self.longueur}\nIscarre:{self.largeur == self.longueur}")
rectangle =rectangle(2,2)

rectangle.info()