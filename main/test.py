from model.classifier import DIGIT_CLASSIFIER

# Path: main/test.py
classifier = DIGIT_CLASSIFIER('data/train.csv')
x_train,y_train = classifier.process_data()
classifier.train(x_train,y_train)


