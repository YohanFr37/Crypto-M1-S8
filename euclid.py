# CONSTANTES
import random
import sys
sys.setrecursionlimit(2048)
sys.set_int_max_str_digits(80000)
fichier = open("test.txt", "w")
# HexaNumber = 2^894 * PI
HexaNumber = 0XFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF
p = (2 ** 1024) - (2 ** 960) - 1 + (2 ** 64) * (HexaNumber + 129093)
g = 2
#p = 3526784
def Bezout(a, p,i):
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
        #print("Q ",Q, " R ", R, " U ", U, " V ", V, " U0 ", U0, " U1 ", U1, " V0 ", V0, " V1 ", V1)
    print("i",i," R0 ",R0 ," aa ", a)
    if (i<=20):
        fichier.write("i : "+ str(i) +"\n")
        fichier.write("a : "+ str(a) +"\n")
        fichier.write("u : "+ str(U0) +"\n")
        fichier.write("p : "+ str(R1) +"\n")
        fichier.write("v : "+ str(V0) +"\n")
        fichier.write("Reste : "+ str(R0)+"\n")
        #fichier.write("\n")

# Question 4 : calcul de g^a mod p
def ExpMod(g,a,i):
    if(a>1):
        if(a%2==0):
            #print("2 g ",g," a ", a)
            #fichier.write("g : "+ str(g)+"\n""\n")
            #fichier.write("a : "+ str(a)+"\n""\n")
            g=g%p
            #fichier.write("A : "+ str(g)+"\n")
            return ExpMod(g*g,a//2,i)%p
        else:
            #print("3 g ",g," a ", a)
            #fichier.write("g : "+ str(g)+"\n""\n")
            #fichier.write("a : "+ str(a)+"\n""\n")
            g=g%p
            #fichier.write("A : "+ str(g)+"\n")
            return ExpMod(g*g,a//2,i)*g%p
    fichier.write("A : "+ str(g)+"\n""\n")
    return g

def main ():  
    for i in range(20):
        c = random.getrandbits(27)
        Bezout(c,p,i+1)
        print("Test :     ",(g**c)%p)
        print("Fonction : ",ExpMod(g,c,i))
main()