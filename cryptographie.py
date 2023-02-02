# CONSTANTES
import random
import sys
sys.setrecursionlimit(2048)
sys.set_int_max_str_digits(8192)
fichier = open("test.txt", "w")
fichierEuclid = open("Euclid.txt", "w")
fichierExpMod = open("ExpMod.txt", "w")
fichierKeyGen = open("KeyGen.txt", "w")
fichierEncrypt = open("Encrypt.txt", "w")
fichierDecrypt = open("Decrypt.txt", "w")

# HexaNumber = 2^894 * PI
HexaNumber = 0XFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF
p = (2 ** 1024) - (2 ** 960) - 1 + (2 ** 64) * (HexaNumber + 129093)

g = 2
Kp = []
Ks = 0

# Qestion 3 : Théorème de Bezout (Euclide Etendue)
def Euclid(a, p, ecriture):
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
    if(ecriture):
        fichierEuclid.write("a : "+ str(a) +"\n")
        fichierEuclid.write("u : "+ str(U0) +"\n")
        fichierEuclid.write("p : "+ str(R1) +"\n")
        fichierEuclid.write("v : "+ str(V0) +"\n")
        fichierEuclid.write("Reste : "+ str(R0)+"\n\n")
    return U0


# Question 4 : calcul de A = g^a mod p

def ExpMod(g,a,ecriture):
    if(a>1):
        if(a%2==0):
            g=g%p
            return ExpMod(g*g,a//2,ecriture)%p   #puissance(g^2,a/2)
        else:
            g=g%p
            return ExpMod(g*g,a//2,ecriture)*g%p #g * puissance(g^2,(a −1)/2)
    if(ecriture):
        fichierExpMod.write("A : "+ str(g) +"\n")
        fichierExpMod.write("a : "+ str(a) +"\n")
        fichierExpMod.write("p : "+ str(p) +"\n\n")
    return g


# Question 5

def Keygen(g,p,x,public):                           # X ≡ g^x mod p
    if(public):
        ecriture = False
        fichierKeyGen.write("g : "+ str(g) +"\n")
        fichierKeyGen.write("X : "+ str(ExpMod(g,x,ecriture)) +"\n")
        return [g,p,ExpMod(g,x,ecriture)]           # Données public dans la génération de clef g, p et X
    else :
        fichierKeyGen.write("x : "+ str(x) +"\n\n")
        return x                                    # Donnée gardé secrète : x

def Encrypt(X,g,p,i):
    ecriture = False
    r = random.randint(2, p-2)
    m = random.randint(i*1000000000, (i+1)*(1000000000-1))
    y = ExpMod(X,r,ecriture)                        # y ≡ X^r mod p
    fichierEncrypt.write("m : "+ str(m) +"\n")
    fichierEncrypt.write("r : "+ str(r) +"\n")
    fichierEncrypt.write("y : "+ str(y) +"\n")
    fichierEncrypt.write("B : "+ str(m*y%p) +"\n")    
    fichierEncrypt.write("C : "+ str(ExpMod(g,r,ecriture)) +"\n\n")
    fichierDecrypt.write("m : "+ str(m) +"\n")
    return [m*y%p,ExpMod(g,r,ecriture)]             # Retourne les valeurs de B et de C

def Decrypt(B,C,x):
    ecriture = False
    D = ExpMod(B,x,ecriture)                        # D ≡ B^x mod p
    DInv = Euclid(D,p,ecriture)                     # Calcule l'inverse de D
    m2 = C*DInv%p                                   # C * D^-1 mod p
    fichierDecrypt.write("m' : "+ str(m2) +"\n\n")
    return m2

#Question 6

def Homomorphique():
    j=37
    public = True                   #Definie si les données sont rendues public
    a = random.randint(2, p-2)
    Kp = Keygen(g,p,a,public)       #Kp = (p,g,X)
    public = False              
    Ks = Keygen(g,p,a,public)       #Ks = x
    BC1 = Encrypt(Kp[2],g,p,j) 
    B1 = BC1[1]                       #Prend le résultat m*y%p de la fonction Encrypt()
    C1 = BC1[0]                       #Prend le résultat ExpMod(g,r) de la fonction Encrypt()
    j=54
    BC2 = Encrypt(Kp[2],g,p,j) 
    B2 = BC2[1]                       #Prend le résultat m*y%p de la fonction Encrypt()
    C2 = BC2[0]  
    C = C1*C2%p
    B = B1*B2%p 
    m1 = Decrypt(B1,C1,Ks)              #Prend le résultat ExpMod(g,r) de la fonction Encrypt()
    print("m1 " ,m1)
    m2 = Decrypt(B2,C2,Ks)
    print("m2 " ,m2)
    m3 = m1*m2%p
    print("m3 ",m3)
    m4 = Decrypt(B,C,Ks)
    print("m4 ",m4)                     

def main ():
    for i in range(100):
        ecriture = True
        a = random.randint(2, p-2)
        Euclid(a,p,ecriture)
        ExpMod(g,a,ecriture)
    for i in range(100):
        a = random.randint(2, p-2)
        public = True                   #Definie si les données sont rendues public
        Kp = Keygen(g,p,a,public)       #Kp = (p,g,X)
        public = False              
        Ks = Keygen(g,p,a,public)       #Ks = x
        BC = Encrypt(Kp[2],g,p,i) 

        B = BC[1]                       #Prend le résultat m*y%p de la fonction Encrypt()
        C = BC[0]                       #Prend le résultat ExpMod(g,r) de la fonction Encrypt()
        m2 = Decrypt(B,C,Ks)
        #print(m2)                       #Nous retrouvons bien le message m
    Homomorphique()
    #fichier.write("A : "+ str(ExpMod(g,a))+"\n""\n")
main()