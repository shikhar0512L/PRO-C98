def wordscounter():
    filename=input("enter the file name: ")
    numberofwords=0
    file=open(filename, 'r')
    for line in file:
        words=line.split()
        numberofwords=numberofwords+len(words)
    print(numberofwords)

wordscounter()