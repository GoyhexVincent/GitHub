#File: sentiment_mod.py

import nltk
import random
from nltk.corpus import movie_reviews
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
from unidecode import unidecode


class VoteClassifier(ClassifierI):
    def __init__(self,*classifiers):
        self._classifiers=classifiers
    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    def confidence (self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf

#Load the data.


##short_pos = open("short_reviews/positive.txt","r").read()
##short_neg = open("short_reviews/negative.txt","r").read()
##
##documents = []
##all_words = []

##j is adject, r is adverb, and v is verb
##allowed_word_types = ["J","R","V"]


##allowed_word_types = ["J"]
##
##for p in short_pos.split('\n'):
##    documents.append( (p,"pos") )
##    words = word_tokenize(p)
##    pos = nltk.pos_tag(words)
##    for w in pos:
##        if w[1][0] in allowed_word_types:
##            all_words.append(w[0].lower())
##
##for p in short_neg.split('\n'):
##    documents.append( (p,"neg"))
##    words = word_tokenize(p)
##    pos = nltk.pos_tag(words)
##    for w in pos:
##        if w[1][0] in allowed_word_types:
##            all_words.append(w[0].lower())
##save_documents = open("pickled_algos/documents.pickle","wb")
##pickle.dump(documents,save_documents)
##save_documents.close()
##
##save_all_words = open("pickled_algos/all_words.pickle","wb")
##pickle.dump(all_words,save_all_words)
##save_all_words.close()



with open(r"pickled_algos/documents.pickle", "rb") as pickle_in:
   documents = pickle.load(pickle_in)
   pickle_in.close()
with open(r"pickled_algos/all_words.pickle", "rb") as pickle_in:
   word_features = pickle.load(pickle_in)
   pickle_in.close()

##all_words = nltk.FreqDist(all_words)

##word_features = list(all_words.keys())[:5000]
print('so far so good')

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features
#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(rev), category) for (rev, category) in documents]
random.shuffle(featuresets)



#naive bayes: we are gonna categorize everything has positive or negative.
#we need two sets: one training and one setting set

training_set = featuresets[:10000]
testing_set = featuresets [10000:]
#naive bayes algorithm.

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)
####
save_classifier = open("pickled_algos/originalnaivebayes5k.pickle","wb")
pickle.dump(classifier,save_classifier)
save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)
####
save_classifier = open("pickled_algos/MNB_classifier5k.pickle","wb")
pickle.dump(MNB_classifier,save_classifier)
save_classifier.close()


BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

####
save_classifier = open("pickled_algos/BernoulliNB_classifier5k.pickle","wb")
pickle.dump(BernoulliNB_classifier,save_classifier)
save_classifier.close()


LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

####
save_classifier = open("pickled_algos/LOgisticRegression_classifier5k.pickle","wb")
pickle.dump(LogisticRegression_classifier,save_classifier)
save_classifier.close()


SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

####
save_classifier = open("pickled_algos/SGDClassifier_classifier5k.pickle","wb")
pickle.dump(SGDClassifier_classifier,save_classifier)
save_classifier.close()


LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

####
save_classifier = open("pickled_algos/LinearSVC_classifier5k.pickle","wb")
pickle.dump(LinearSVC_classifier,save_classifier)
save_classifier.close()


NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)
####
save_classifier = open("pickled_algos/NuSVC_classifier5k.pickle","wb")
pickle.dump(NuSVC_classifier,save_classifier)
save_classifier.close()



print("Regular Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

##save_classifier = open("naivebayes.pickle", "wb")
##pickle.dump(classifier, save_classifier)
##save_classifier.close()import nltk

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MultinomialNB accuracy percent:",nltk.classify.accuracy(MNB_classifier, testing_set))

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BernoulliNB accuracy percent:",nltk.classify.accuracy(BNB_classifier, testing_set))



voted_classifier =  VoteClassifier(classifier,
                                   LogisticRegression_classifier,
                                   MNB_classifier,
                                   BernoulliNB_classifier,
                                   #SGDClassifier_classifier,
                                   LinearSVC_classifier,
                                   NuSVC_classifier)
print("Voted_classifier accuracy percent:",nltk.classify.accuracy(voted_classifier, testing_set))
def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats)

#SAVE ME AS SENTIMENT_MOD.py
