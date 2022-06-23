def countWordsFromFile():
    fileName = input("Enter the FILE NAME:")
    file = open(fileName, 'r')
    count = 0
    for i in file:
        words = i.split()
        print(words)
        count = count + len(words)
       
    print("No. of words are :") 
    print(count)      


countWordsFromFile()