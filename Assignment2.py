import os

path = r'D:\Mariam\4th year\2nd term\NLP\Assignments\New folder\txt_sentoken\neg'
files=os.listdir(path)
print(files)
words = []
for name in files:
        print(" ",name,"")
        filename = os.path.join(path, name)
        f = open(filename,"r")
        for line in f:
            for word in line.split():
                #print(word)
                words.append(word)
        counter = 0
        print(len(words))