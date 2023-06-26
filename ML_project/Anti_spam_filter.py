import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split, cross_val_score,cross_val_predict, StratifiedKFold

data = pd.read_csv('spam.csv', encoding='latin-1')
data = data[['v1', 'v2']]
train_data,test_data =  train_test_split(data, test_size=0.2, random_state=59,)
x_train = train_data['v2'].tolist()
y_train = train_data['v1']
x_test = test_data['v2'].tolist()
y_test = test_data['v1']
pipeline = Pipeline([
    ('count_vectorizer', CountVectorizer()),
    ('naive_bayes', MultinomialNB())
])

# Walidacja krzyżowa wraz z stratyfikacja
cv_strat = StratifiedKFold(n_splits=5, shuffle=True, random_state=53)
cv_scores = cross_val_score(pipeline, x_train, y_train, cv=cv_strat)

for i, score in enumerate(cv_scores):
    print("Cross-Validation Iteration", i+1)
    print("Accuracy:", score)

y_pred = cross_val_predict(pipeline, x_train, y_train, cv=10)

precision = precision_score(y_train, y_pred, pos_label='spam')
recall = recall_score(y_train, y_pred, pos_label='spam')

print("Precision:", precision)
print("Recall:", recall)

pipeline.fit(x_train,y_train)
print(y_train.info())
# Ocena modelu na danych treningowych
train_predictions = pipeline.predict(x_train)
train_accuracy = accuracy_score(y_train, train_predictions)
train_precision = precision_score(y_train, train_predictions, pos_label='spam')
train_recall = recall_score(y_train, train_predictions, pos_label='spam')


test_predictions = pipeline.predict(x_test)
test_accuracy = accuracy_score(y_test, test_predictions)
test_precision = precision_score(y_test, test_predictions, pos_label='spam')
test_recall = recall_score(y_test, test_predictions, pos_label='spam')

print("Train Accuracy:", train_accuracy)
print("Train Precision:", train_precision)
print("Train Recall:", train_recall)
print("Test Accuracy:", test_accuracy)
print("Test Precision:", test_precision)
print("Test Recall:", test_recall)
example = [ "erotic date with hot woman"]
example2 = [ "hot moms in your area."]
example3 = [ "hi honey i love you so much"]
example4 = [ "Multi level marketing"]
example5 = [ "Lottery, you can win a prize, 1000$"]
# Prognozowanie etykiety przykładu
prediction = pipeline.predict(example)
print("Prediction:", prediction)
prediction2 = pipeline.predict(example2)
print("Prediction2:", prediction2)
prediction3 = pipeline.predict(example3)
print("Prediction3:", prediction3)
prediction4 = pipeline.predict(example4)
print("Prediction4:", prediction4)
prediction5 = pipeline.predict(example5)
print("Predictio5n:", prediction5)
import pickle

with open('model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

