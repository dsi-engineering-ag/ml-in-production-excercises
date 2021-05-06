#!/bin/python

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate, cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from joblib import dump, load


def load_data(csv_file):
    df = pd.read_csv(csv_file, low_memory=False)

    return df


def preprocess(df):
    # specify target. Eligible if not defaulted
    df['TARGET'] = [0 if i=='Default' else 1 for i in df['loan_status']]

    df.drop(df.columns.difference(['loan_amnt', 'annual_inc', 'TARGET']), 1, inplace=True)
    df = df.dropna()
    df = pd.get_dummies(df)

    return df


def split(df):
    X_train, X_test, y_train, y_test = train_test_split(df.drop('TARGET',axis=1),df['TARGET'],test_size=0.15,random_state=101,  stratify=df['TARGET'])
    return X_train, X_test, y_train, y_test


def create_pipeline():

    eligibility_pipeline = make_pipeline(StandardScaler(), LogisticRegression(C = 0.0001,random_state=21))

    return eligibility_pipeline


def store_model(model, file):
    dump(model, file) 


def train_pipeline(pipeline, X, y):

    from imblearn.over_sampling import SMOTE

    sm = SMOTE(random_state=12)
    x_train_r, y_train_r = sm.fit_resample(X, y)

    print("Train pipeline")

    pipeline.fit(x_train_r, y_train_r)


def calculate_score(pipeline, X, y):
    print("Confusion matrix on test set:")
    conf = confusion_matrix(y, pipeline.predict(X))

    print(conf)

if __name__ == '__main__':

    src = 'notebooks/clean-loan-data.csv'

    print("Load data source file:", src)
    df = load_data(src)
    print("Source file loaded")

    df = preprocess(df)

    X_train, X_test, y_train, y_test = split(df)

    pipeline = create_pipeline()

    train_pipeline(pipeline, X_train, y_train)

    calculate_score(pipeline, X_test, y_test)

    store_model(pipeline, 'services/eligibility/eligibility_pipeline.joblib')

