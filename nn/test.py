import pickle
from tensorflow.keras import layers, optimizers, models
import numpy as np

vectorizer = pickle.load(open("vectorizer.pickle", "rb"))

test = \
"""
super.viewWillAppear(animated)
    
    var resourceFileDictionary: NSDictionary?
    
    //Load content of Info.plist into resourceFileDictionary dictionary
    if let path = Bundle.main.path(forResource: "Info", ofType: "plist") {
        resourceFileDictionary = NSDictionary(contentsOfFile: path)
    }
    
    if let resourceFileDictionaryContent = resourceFileDictionary {
        
        // Get something from our Info.plist like MinimumOSVersion
        print("MinimumOSVersion = \(resourceFileDictionaryContent.object(forKey: "MinimumOSVersion")!)")
        
        //Or we can print out entire Info.plist dictionary to preview its content
        print(resourceFileDictionaryContent)
        

"""

X = vectorizer.transform([test])

label_encoder = pickle.load(open("label_encoder.pickle", "rb"))

model = models.load_model("model")
predict = model.predict(X)
print(predict)
print(label_encoder.inverse_transform(range(6)))


predicted_classes = []
for prediction in predict:
    predicted_classes.append(np.argmax(prediction))

class_labels = label_encoder.inverse_transform(predicted_classes)
print(class_labels)
