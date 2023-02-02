# CONSTANTES
import random
import sys
sys.setrecursionlimit(2048)
sys.set_int_max_str_digits(8192)
fichier = open("test.txt", "w")

# HexaNumber = 2^894 * PI
HexaNumber = 0XFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF
p = (2 ** 1024) - (2 ** 960) - 1 + (2 ** 64) * (HexaNumber + 129093)

g = 2
Kp = []
Ks = 0

# Qestion 3 : Théorème de Bezout (Euclide Etendue)
def Bezout(a, p):
    U0 = 1
    U1 = 0
    V0 = 0
    V1 = 1
    R0 = a
    R1 = p
    while (R1 > 0):
        Q = R0//R1
        R = R0 % R1
        U = U0 - Q * U1
        V = V0 - Q * V1
        R0 = R1
        R1 = R
        U0 = U1
        V0 = V1
        U1 = U
        V1 = V
        """
        fichier.write("a : "+ str(a) +"\n")
        fichier.write("u : "+ str(U0) +"\n")
        fichier.write("p : "+ str(R1) +"\n")
        fichier.write("v : "+ str(V0) +"\n")
        fichier.write("Reste : "+ str(R0)+"\n")
        #fichier.write("\n")
        """
    return U0

# Question 4 : calcul de g^a mod p
def ExpMod(g,a):
    if(a>1):
        if(a%2==0):
            g=g%p
            return ExpMod(g*g,a//2)%p   #puissance(g^2,a/2)
        else:
            g=g%p
            return ExpMod(g*g,a//2)*g%p #g * puissance(g^2,(a −1)/2)
    #print("\nX2 ", g)
    return g

# Question 5

def Keygen(g,p,x,public):
    if(public):
        return [g,p,ExpMod(g,x)]        #Données public dans la génération de clef g, p et X
    else :
        return x                        #Donnée gardé secrète : x

def Encrypt(X,g,p,j):
    r = random.randint(2, p-2)
    m = j**2
    y = ExpMod(X,r)                     # y = X^r mod p
    print(m)
    return [m*y%p,ExpMod(g,r)]          # Retourne les valeurs de B et de C

def Decrypt(B,C,x):
    D = ExpMod(B,x)                     #B^x mod p
    DInv = Bezout(D,p)                  #Calcule l'inverse de D
    m2 = C*DInv%p                       #C * D^-1 mod p
    print(m2)                           #Nous retrouvons bien le message m
    #return C * (1//D)%p

#Question 6
#def Homomorphique():

def main ():  
    for i in range(100):
        j=i+1
        public = True                   #Definie si les données sont rendues public
        a = random.randint(2, p-2)
        #Bezout(a,p)
        Kp = Keygen(g,p,a,public)       #Kp = (p,g,X)
        public = False              
        Ks = Keygen(g,p,a,public)       #Ks = x

        BC = Encrypt(Kp[2],g,p,j) 
        B = BC[1]                       #Prend le résultat m*y%p de la fonction Encrypt()
        C = BC[0]                       #Prend le résultat ExpMod(g,r) de la fonction Encrypt()
        Decrypt(B,C,a)
        fichier.write("A : "+ str(ExpMod(g,a))+"\n""\n")
main()