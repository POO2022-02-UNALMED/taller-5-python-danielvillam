from gestion.zona import Zona
from gestion.zoologico import Zoologico 
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from zooAnimales.animal import Animal

if __name__ == "__main__":
    
    ave1 =Ave("paloma", 5, "ciudad", "F", "gris")
    comp = "Mi nombre es paloma, tengo una edad de 5, habito en ciudad y mi genero es F"
    if ave1.toString() ==  comp:
        print("yes")
    else:
        print("Nop")