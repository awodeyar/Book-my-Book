import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
 
def word_feats(words):
    return dict([(word, True) for word in words])
 
f = open("rev.txt","r")
lines = f.read()
line = lines.split()
f.close()

line = (word_feats(line),'pos')
lines1 = []
lines1.append(line)

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

negcutoff = len(negfeats)
poscutoff = len(posfeats)
 
trainfeats = negfeats+ posfeats
testfeats = lines1
#print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 
print line[0]
classifier = NaiveBayesClassifier.train(trainfeats)
#print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
#classifier.show_most_informative_features()
#classifier.batch_classify
#classifier.batch_prob_classify()
#classifier.batch_probdist()
print classifier.classify(line[0])
#classifier.labels
#classifier.most_informative_features(lines1)
#classifier.prob_classify
#classifier.probdist()
