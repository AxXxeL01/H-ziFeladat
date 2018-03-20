import codecs
def feladat1(fajl_nev):
    fajl=codecs.open(fajl_nev,encoding='utf8', mode="r")
    max=0
    max_sor=""
    for sor in fajl:
        sor=sor.strip()
        if (sor[0].isupper() and len(sor)>max):
            max=len(sor)
            max_sor=sor
    print (max,max_sor)
    fajl.close()

def feladat2():
    fajl=open("be1.txt", mode ="r")
    for sor in fajl:
        if ("   " in sor):
            fajl=open("ki1.txt", mode ="w")
            fajl.write(sor)
            fajl.close()
            break

def fel7(lista,betu):
    li=[]
    fajl=open("ki2.txt", mode = "w")
    for i in lista:
        if i[0]==betu:
            li.append(i)
    fajl.write(str(li))
    fajl.close()

def main():
    feladat1("be1.txt")
    feladat2()
    fel7(["alma", "ananász", "narancs"],"a")
main()