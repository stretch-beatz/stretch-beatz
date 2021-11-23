import json, pickle
import sys
import os.path as ospath
from sklearn import datasets
#from FoxDot import *
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import numpy as np
import argparse

class MusicLearning:
    dataset = None
    _data = []
    _target = []
    _pipeline = None
    model = ""
    filename = ""
    inputlength=4
    tpot_max_len = 10000

    def __init__(self, model) -> None:
        self.model = model

    def set_data(self, data):
        self.dataset = data
        self._data = []
        self._target = []
        
    @property
    def data(self):
        if len(self._data) == 0 :
            self.createDataSet()    
        return self._data

    @property
    def target(self):
        if len(self._target) == 0 :
            self.createDataSet()    
        return self._target

    def createDataSet(self):
        inputdata = []
        targetdata = []

        for compass in self.dataset:
            if len(compass) > self.inputlength:
                for i in range(0, max(0,len(compass)-(self.inputlength+1))):
                    inputdata.append(compass[i:(i+self.inputlength-0)])
                    targetdata.append(compass[i+self.inputlength+0])
        
        self._data = np.array(inputdata)
        self._target = np.array(targetdata)
        print ("Data Set Contains "+ str(len(self._data))+" items")

    @property
    def model_file(self):
        return ospath.join('models',self.model+'.pickle')
    
    @property
    def tpot_file(self):
        return ospath.join("output", self.model + "_tpot.py")

    @property
    def pipeline_file(self):
        return ospath.join("output", self.model + "_scikit.pickle")

    '''
    @property
    def data_file(self):
        return ospath.join("output", self.model + ".pickle")
    '''


    @property
    def data_json_file(self):
        return ospath.join("output", self.model + ".json")

    @property
    def pipeline(self):
        if self._pipeline == None :
            if(ospath.isfile(self.pipeline_file)):
                with open(self.pipeline_file,'rb') as j:
                    self._pipeline = pickle.load( j)
            else :
                self.getTpotModel()

        return self._pipeline

    def getTpotModel(self):
        from tpot import TPOTClassifier
        prop = 1
        data_len = len(self.data)
        print("data_len", data_len, "self.tpot_max_len", self.tpot_max_len) 
        if (data_len> self.tpot_max_len):
            prop = self.tpot_max_len / data_len
            print("Proportion of data used for TPot", prop)

        X_train, X_test, y_train, y_test = train_test_split(self.data, self.target,
                                                            train_size=(0.75*prop), test_size=(0.25*prop))

        pipeline_optimizer = TPOTClassifier(generations=5, population_size=20, cv=5,
                                            #random_state=42,
                                             verbosity=2)
        pipeline_optimizer.fit(X_train, y_train)
        print(pipeline_optimizer.score(X_test, y_test))
        
        pipeline_optimizer.export(self.tpot_file)

        self._pipeline = pipeline_optimizer.fitted_pipeline_

        self.save_pipeline()

    def trainModel(self):
        X_train, X_test, y_train, y_test = train_test_split(self.data, self.target,
                                                            train_size=0.75, test_size=0.25)

        self.pipeline.fit(X_train, y_train)
        #results = self.pipeline.predict(X_test)
        print(self.pipeline.score(X_test, y_test))
        #results = self.pipeline.predict([[7,7,10,7], [7,10,7,5]])
        #return results
        self.save_pipeline()

    def save_pipeline(self):
        pickleFile = self.pipeline_file
        print("Saving "+pickleFile)
        with open(pickleFile,'wb') as k:
            pickle.dump(self.pipeline, k)


    def expand(self, input, length = 4):
        output = []
        output.extend(input)
        #print("input", input)
        #print("output", output)
        for i in range(length):
            
            next_bar = output[-self.inputlength:]
            #print("next_bar", next_bar)
            prediction = self.pipeline.predict([next_bar])
            #print("prediction", prediction)
            output.append(prediction[0])

        #print("output", output)
        return output


def main(args):
    modelName = args.model

    ml = MusicLearning(modelName)

    pickleFile = args.file
    if(pickleFile == None):
        pickleFile = ospath.join('output',modelName+'.pickle')
    
    if args.mode == "tpot":
        print("Loading "+pickleFile)
        with open(pickleFile,'rb') as j:
            data = pickle.load(j)
            ml.set_data(data['degree'])
            ml.getTpotModel()

    if args.mode == 'train':
        print("Loading "+pickleFile)
        with open(pickleFile,'rb') as j:
            data = pickle.load(j)
            ml.set_data(data['degree'])
            ml.trainModel()
        
    if args.mode == 'test':
        expanded = ml.expand([0,2,1,3,4,6,2,3,5],20) 
        print(expanded)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Learn from data and test whether it works ok?')
    parser.add_argument('--model', help='Model name', default='bach')
    parser.add_argument('--file', help='File to load learning data from')
    parser.add_argument('--mode', help='What action to take', choices=['tpot', 'train', 'test'], default="test")
    
    args = parser.parse_args()
    #print (args)
    
    main(args)