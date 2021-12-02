import json, pickle
import sys
import os.path as ospath
from sklearn import datasets
#from FoxDot import *
from tpot import TPOTClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import numpy as np
import argparse


class Dataset :
    data = None
    target = None
    
    def __init__(self, inputdata, targetdata) -> None:
        self.data = np.array(inputdata)
        self.target = np.array(targetdata)
    
def createDataSet(data, inputlength=4, outputlength=1):
    inputdata = []
    targetdata = []

    for compass in data:
        if len(compass)>inputlength:
            print(compass)
            for i in range(0, max(0,len(compass)-(inputlength+1))):
                inputdata.append(compass[i:(i+inputlength-0)])
                targetdata.append(compass[i+inputlength+0])
            dataset = Dataset(inputdata, targetdata)    

    return dataset

def getTpotModel(digits):
    X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target,
                                                        train_size=0.75, test_size=0.25)

    pipeline_optimizer = TPOTClassifier(generations=5, population_size=20, cv=5,
                                        random_state=42, verbosity=2)
    pipeline_optimizer.fit(X_train, y_train)
    print(pipeline_optimizer.score(X_test, y_test))
    
    tpotModelFileName = ospath.join("output",args.model + "_tpot.py")
    pipeline_optimizer.export(tpotModelFileName)

    pickleFile = ospath.join("output",args.model + "_scikit.pickle")
    print("Saving "+pickleFile)
    with open(pickleFile,'wb') as k:
        pickle.dump(pipeline_optimizer.fitted_pipeline_, k)
        

def trainModel(digits):
    import numpy as np
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import BernoulliNB
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.pipeline import make_pipeline, make_union
    from tpot.builtins import StackingEstimator
    from tpot.export_utils import set_param_recursive

    training_features, testing_features, training_target, testing_target = \
    train_test_split(digits.data, digits.target, random_state=42)

    # Average CV score on the training set was: 0.866000484496124
    exported_pipeline = make_pipeline(
        StackingEstimator(estimator=BernoulliNB(alpha=1.0, fit_prior=True)),
        StackingEstimator(estimator=RandomForestClassifier(bootstrap=False, criterion="gini", max_features=0.9000000000000001, min_samples_leaf=5, min_samples_split=6, n_estimators=100)),
        KNeighborsClassifier(n_neighbors=7, p=1, weights="distance")
    )
    # Fix random state for all the steps in exported pipeline
    set_param_recursive(exported_pipeline.steps, 'random_state', 42)

    exported_pipeline.fit(training_features, training_target)
    results = exported_pipeline.predict(testing_features)
    
    results = exported_pipeline.predict([[7,7,10,7], [7,10,7,5]])
    return results


def main(args):
    modelName = args.model
    modelFile = ospath.join('models',modelName+'.pickle')
    pickleFile = args.file
    if(pickleFile == None):
        pickleFile = ospath.join('output',modelName+'.pickle')
    
    print("Loading "+pickleFile)
    with open(pickleFile,'rb') as j:
        data = pickle.load( j)
        #print(data)
        print(len(data["degree"]), "Compasses")
        dataset = createDataSet(data['degree'])
        
        if args.mode == "tpot":
            modelfilename = getTpotModel(dataset)
            print ("modelfilename", modelfilename)

        if args.mode == 'train':
            modelresults = trainModel(dataset)
            print(modelresults)
            
        if args.mode == 'train':
            modelresults = trainModel(dataset)
            print(modelresults)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Learn from data and test whether it works ok?')
    parser.add_argument('--model', help='Model name', default='bad_guy')
    parser.add_argument('--file', help='File to load learning data from')
    parser.add_argument('--mode', help='What action to take', choices=['tpot', 'train', 'test'], default="train")
    
    
    args = parser.parse_args()


    #print("Scale.minor", Scale.minor)

    main(args)