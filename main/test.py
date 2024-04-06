from model.classifier import KNN_DIGIT_CLASSIFIER

classifier = KNN_DIGIT_CLASSIFIER('./Dataset/Train.csv')
x_train, y_train = classifier.process_data()
classifier.train(x_train,y_train,5)
