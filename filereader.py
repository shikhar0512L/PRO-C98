def countWordsFromFile():
    x=input("enter file name: ")
    f=open(x, 'r')
    d=f.read()
    x=d.split("\n")
    ff=0

    for ww in x:
        vv=ww.split()
        ff=ff+len(vv)
    print(ff)
        



countWordsFromFile()