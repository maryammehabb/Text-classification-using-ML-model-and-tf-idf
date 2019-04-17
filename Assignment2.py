import os
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

path = r'D:\Mariam\4th year\2nd term\NLP\Assignments\New folder\txt_sentoken\neg'
path2 = r'D:\Mariam\4th year\2nd term\NLP\Assignments\New folder\txt_sentoken\pos'
files=os.listdir(path)
files2 = os.listdir(path2)
corpuspos = []
corpusneg = []
neg = []
pos = []
labels = []
posandneg = []


for name in files:
        filename = os.path.join(path, name)
        f = open(filename,"r").read()
        corpusneg.append(f)
        neg.append(0)

for name in files2:
        filename = os.path.join(path2, name)
        f = open(filename,"r").read()
        corpuspos.append(f)
        pos.append(1)


for t in range(len(neg)):
    labels.append((neg[t]))
for t in range(len(pos)):
    labels.append((pos[t]))

for t in range(len(corpusneg)):
    posandneg.append((corpusneg[t]))
    #print(corpuspos[t])
for t in range(len(corpuspos)):
    posandneg.append((corpuspos[t]))


vectorizer = TfidfVectorizer(stop_words='english', analyzer='char')
X_train, X_test, y_train, y_test = train_test_split(posandneg, labels, test_size=0.33, random_state=42)
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)
yPrediction = model.predict(X_test)
print(yPrediction)
x =accuracy_score(y_test, yPrediction)
print(x)
a = x * 100
print(a)


def predictt(v, m, text):
    arroftext=[]
    arroftext.append(text)
    X_train = v.transform(arroftext)
    result = m.predict(X_train)
    print(result)


predictt(vectorizer, model, "two teen couples go to a church party")
