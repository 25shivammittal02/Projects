import pandas as pd
import numpy as np
import time 
import re
import nltk
from nltk.corpus import stopwords
#nltk.download('stopwords')

train_set = pd.read_csv('final.csv')
train_min = train_set

def pre_process(lis):
    for i in range(len(lis)):
        review = re.sub(r'\W', ' ', str(lis[i]))
        review = review.lower()
        review = re.sub(r'^br$', ' ', review)
        review = re.sub(r'\s+br\s+',' ',review)
        review = re.sub(r'\s+[a-z]\s+', ' ',review)
        review = re.sub(r'^b\s+', '', review)
        review = re.sub(r'\s+', ' ', review)
        lis[i] = review
        
for x in range(20702):
        d = int(train_min.iloc[x,1])
        if d in range(1,4):
            train_min.iloc[x,1] = 0
        else:
            train_min.iloc[x,1] = 1
        review = re.sub(r'\W', ' ', str(train_min.iloc[x,2]))
        review = review.lower()
        review = re.sub(r'^br$', ' ', review)
        review = re.sub(r'\s+br\s+',' ',review)
        review = re.sub(r'\s+[a-z]\s+', ' ',review)
        review = re.sub(r'^b\s+', '', review)
        review = re.sub(r'\s+', ' ', review)
        train_min.iloc[x,2] = review

# Creating the Tf-Idf model directly

# Training the classifier

train_min.to_csv('./final1.csv')

print ("Welcome to Amazon Customer Review Analysis..")
time.sleep(1)
product_list = []
for i in range(train_min.shape[0]):
    if train_min.iloc[i,0] in product_list:
        continue
    else:
       product_list.append(train_min.iloc[i,0])     
#menu starts here
while True:
    for i in range(len(product_list)):
        p = i + 1
        print (str(p)+". "+(product_list[i]))
        time.sleep(0.5)
    choice = input('Choose the product(6 to exit) : ')
    choice = int(choice)
    if choice==1:
        input3 = open('final1.csv' , 'r')
        output = open('New1.csv' , 'w')
        row = input3.readline()
        output.write(row)
        while row:
            # print(row)
            row = input3.readline()
            if row and product_list[0].strip() in row:
                output.write(row)
            #output.write('\n')
        input3.close()
        output.close()
        camera = []
        c = []
        bat = []
        b = []
        ds = pd.read_csv('New1.csv')#picking up revs
        for i in range(ds.shape[0]):
            sent = ds.iloc[i,3]
            sent = str(sent)
            sent = sent.lower()
            if 'camera' in sent or 'picture' in sent or 'image' in sent:
                camera.append(sent)
                c.append(ds.iloc[i,2])
            if 'battery' in sent or 'power' in sent:
                bat.append(sent)
                b.append(ds.iloc[i,2])
        pre_process(camera)
        pre_process(bat)
        att = str(input('enter feature(camera,battery) : '))
        if att=='camera':
            y = c
            from sklearn.feature_extraction.text import TfidfVectorizer
            vectorizer = TfidfVectorizer(max_features = 200, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
            X = vectorizer.fit_transform(camera).toarray()
            from sklearn.model_selection import train_test_split
            text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
            from sklearn.linear_model import LogisticRegression
            classifier = LogisticRegression()
            classifier.fit(text_train,sent_train)
            sent_pred = classifier.predict(text_test)
            from sklearn.metrics import confusion_matrix
            cm = confusion_matrix(sent_test, sent_pred)
        elif att=='battery':
            y = b
            from sklearn.feature_extraction.text import TfidfVectorizer
            vectorizer = TfidfVectorizer(max_features = 200, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
            X = vectorizer.fit_transform(bat).toarray()
            from sklearn.model_selection import train_test_split
            text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
            from sklearn.linear_model import LogisticRegression
            classifier = LogisticRegression()
            classifier.fit(text_train,sent_train)
            sent_pred = classifier.predict(text_test)
            from sklearn.metrics import confusion_matrix
            cm = confusion_matrix(sent_test, sent_pred)
        else:
            print('invalid !')
            time.sleep(0.5)
        break
    elif choice==2:
        input3 = open('final1.csv' , 'r')
        output = open('New2.csv' , 'w')
        row = input3.readline()
        output.write(row)
        while row:
            # print(row)
            row = input3.readline()
            if row and product_list[1].strip() in row:
                output.write(row)
            #output.write('\n')
        input3.close()
        output.close()
        camera = []
        c = []
        bat = []
        b = []
        ds = pd.read_csv('New2.csv')#picking up revs
        for i in range(ds.shape[0]):
            sent = ds.iloc[i,3]
            sent = str(sent)
            sent = sent.lower()
            if 'camera' in sent or 'picture' in sent or 'image' in sent:
                camera.append(sent)
                c.append(ds.iloc[i,2])
            if 'battery' in sent or 'power' in sent:
                bat.append(sent)
                b.append(ds.iloc[i,2])
        pre_process(camera)
        pre_process(bat)
        att = str(input('enter feature(camera,battery) : '))
        if att=='camera':
            y = c
            from sklearn.feature_extraction.text import TfidfVectorizer
            vectorizer = TfidfVectorizer(max_features = 200, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
            X = vectorizer.fit_transform(camera).toarray()
            from sklearn.model_selection import train_test_split
            text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
            from sklearn.linear_model import LogisticRegression
            classifier = LogisticRegression()
            classifier.fit(text_train,sent_train)
            sent_pred = classifier.predict(text_test)
            from sklearn.metrics import confusion_matrix
            cm = confusion_matrix(sent_test, sent_pred)
        elif att=='battery':
            y = b
            from sklearn.feature_extraction.text import TfidfVectorizer
            vectorizer = TfidfVectorizer(max_features = 200, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
            X = vectorizer.fit_transform(bat).toarray()
            from sklearn.model_selection import train_test_split
            text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
            from sklearn.linear_model import LogisticRegression
            classifier = LogisticRegression()
            classifier.fit(text_train,sent_train)
            sent_pred = classifier.predict(text_test)
            from sklearn.metrics import confusion_matrix
            cm = confusion_matrix(sent_test, sent_pred)
        else:
            print('invalid !')
            time.sleep(0.5)
        break
    elif choice==3:
        input3 = open('final1.csv' , 'r')
        output = open('New3.csv' , 'w')
        row = input3.readline()
        output.write(row)
        while row:
            # print(row)
            row = input3.readline()
            if row and product_list[2].strip() in row:
                output.write(row)
            #output.write('\n')
        input3.close()
        output.close()
        camera = []
        c = []
        bat = []
        b = []
        ds = pd.read_csv('New3.csv')#picking up revs
        for i in range(ds.shape[0]):
            sent = ds.iloc[i,3]
            sent = str(sent)
            sent = sent.lower()
            if 'camera' in sent or 'picture' in sent or 'image' in sent:
                camera.append(sent)
                c.append(ds.iloc[i,2])
            if 'battery' in sent or 'power' in sent:
                bat.append(sent)
                b.append(ds.iloc[i,2])
        pre_process(camera)
        pre_process(bat)
        att = str(input('enter feature(camera,battery) : '))
        if att=='camera':
            y = c
            from sklearn.feature_extraction.text import TfidfVectorizer
            vectorizer = TfidfVectorizer(max_features = 200, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
            X = vectorizer.fit_transform(camera).toarray()
            from sklearn.model_selection import train_test_split
            text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
            from sklearn.linear_model import LogisticRegression
            classifier = LogisticRegression()
            classifier.fit(text_train,sent_train)
            sent_pred = classifier.predict(text_test)
            from sklearn.metrics import confusion_matrix
            cm = confusion_matrix(sent_test, sent_pred)
        elif att=='battery':
            y = b
            from sklearn.feature_extraction.text import TfidfVectorizer
            vectorizer = TfidfVectorizer(max_features = 200, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
            X = vectorizer.fit_transform(bat).toarray()
            from sklearn.model_selection import train_test_split
            text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
            from sklearn.linear_model import LogisticRegression
            classifier = LogisticRegression()
            classifier.fit(text_train,sent_train)
            sent_pred = classifier.predict(text_test)
            from sklearn.metrics import confusion_matrix
            cm = confusion_matrix(sent_test, sent_pred)
        else:
            print('invalid !')
            time.sleep(0.5)
        break
    elif choice==4:
        input3 = open('final1.csv' , 'r')
        output = open('New4.csv' , 'w')
        row = input3.readline()
        output.write(row)
        while row:
            # print(row)
            row = input3.readline()
            if row and product_list[3].strip() in row:
                output.write(row)
            #output.write('\n')
        input3.close()
        output.close()
        camera = []
        c = []
        bat = []
        b = []
        ds = pd.read_csv('New4.csv')#picking up revs
        for i in range(ds.shape[0]):
            sent = ds.iloc[i,3]
            sent = str(sent)
            sent = sent.lower()
            if 'camera' in sent or 'picture' in sent or 'image' in sent:
                camera.append(sent)
                c.append(ds.iloc[i,2])
            if 'battery' in sent or 'power' in sent:
                bat.append(sent)
                b.append(ds.iloc[i,2])
        pre_process(camera)
        pre_process(bat)
        att = str(input('enter feature(camera,battery) : '))
        if att=='camera':
            y = c
            from sklearn.feature_extraction.text import TfidfVectorizer
            vectorizer = TfidfVectorizer(max_features = 200, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
            X = vectorizer.fit_transform(camera).toarray()
            from sklearn.model_selection import train_test_split
            text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
            from sklearn.linear_model import LogisticRegression
            classifier = LogisticRegression()
            classifier.fit(text_train,sent_train)
            sent_pred = classifier.predict(text_test)
            from sklearn.metrics import confusion_matrix
            cm = confusion_matrix(sent_test, sent_pred)
        elif att=='battery':
            y = b
            from sklearn.feature_extraction.text import TfidfVectorizer
            vectorizer = TfidfVectorizer(max_features = 200, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
            X = vectorizer.fit_transform(bat).toarray()
            from sklearn.model_selection import train_test_split
            text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
            from sklearn.linear_model import LogisticRegression
            classifier = LogisticRegression()
            classifier.fit(text_train,sent_train)
            sent_pred = classifier.predict(text_test)
            from sklearn.metrics import confusion_matrix
            cm = confusion_matrix(sent_test, sent_pred)
        else:
            print('invalid !')
            time.sleep(0.5)
        break
    elif choice==5:
        input3 = open('final1.csv' , 'r')
        output = open('New5.csv' , 'w')
        row = input3.readline()
        output.write(row)
        while row:
            # print(row)
            row = input3.readline()
            if row and product_list[4].strip() in row:
                output.write(row)
            #output.write('\n')
        input3.close()
        output.close()
        storage = []
        s = []
        bat = []
        b = []
        ds = pd.read_csv('New5.csv')#picking up revs
        for i in range(ds.shape[0]):
            sent = ds.iloc[i,3]
            sent = str(sent)
            sent = sent.lower()
            if 'storage' in sent or 'space' in sent or 'memory' in sent:
                storage.append(sent)
                s.append(ds.iloc[i,2])
            if 'battery' in sent or 'power' in sent:
                bat.append(sent)
                b.append(ds.iloc[i,2])
        camera = storage
        c = s
        pre_process(camera)
        pre_process(bat)
        att = str(input('enter feature(storage,battery) : '))
        if att=='storage':
            y = c
            from sklearn.feature_extraction.text import TfidfVectorizer
            vectorizer = TfidfVectorizer(max_features = 200, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
            X = vectorizer.fit_transform(camera).toarray()
            from sklearn.model_selection import train_test_split
            text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
            from sklearn.linear_model import LogisticRegression
            classifier = LogisticRegression()
            classifier.fit(text_train,sent_train)
            sent_pred = classifier.predict(text_test)
            from sklearn.metrics import confusion_matrix
            cm = confusion_matrix(sent_test, sent_pred)
        elif att=='battery':
            y = b
            from sklearn.feature_extraction.text import TfidfVectorizer
            vectorizer = TfidfVectorizer(max_features = 200, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
            X = vectorizer.fit_transform(bat).toarray()
            from sklearn.model_selection import train_test_split
            text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
            from sklearn.linear_model import LogisticRegression
            classifier = LogisticRegression()
            classifier.fit(text_train,sent_train)
            sent_pred = classifier.predict(text_test)
            from sklearn.metrics import confusion_matrix
            cm = confusion_matrix(sent_test, sent_pred)
        else:
            print('invalid !')
            time.sleep(0.5)
        break
    elif choice==6:
        print ('Thank You for Visiting !')
        time.sleep(2)
        break
    else:
        print('Please choose from the correct options : ')
        time.sleep(1)
    