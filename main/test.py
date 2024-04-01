from Model.classifier import KNN_DIGIT_CLASSIFIER

model = KNN_DIGIT_CLASSIFIER([
    './Dataset/Train.csv',
    './Dataset/Test.csv'
])
x_train, x_test, y_train, y_test,test_data = model.process_data()
model.train(x_train, y_train)
y_pred = model.predict(x_test)
print(y_pred)
print(model.decode_labels(y_pred))

