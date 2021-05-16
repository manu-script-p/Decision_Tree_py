'''
Assume df is a pandas dataframe object of the dataset given
'''
import numpy as np
import pandas as pd
import random

'''Calculate the entropy of the enitre dataset'''
	#input:pandas_dataframe
	#output:int/float/double/large

def get_entropy_of_dataset(df):
    entropy=0
    v={}
    x=df[df.columns[-1]].count()
    a=df[df.columns[-1]].unique()
    for i in a:
        v[i]=df[df.columns[-1]].str.count(i).sum()
    for j in v:
        if v[j]>0 and x>0:       
            x1=(v[j])/x
            entropy-=x1*np.log2(x1)
    return entropy



'''Return entropy of the attribute provided as parameter'''
	#input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
	#output:int/float/double/large
def get_entropy_of_attribute(df,attribute):
    entropy_of_attribute = 0
    z=dict(tuple(df.groupby(attribute)))
    entropy=0;
    v={}
    x=df[df.columns[-1]].count()
    a=df[df.columns[-1]].unique()
    for i in a:
        v[i]=df[df.columns[-1]].str.count(i).sum()
    for key,value in z.items():
        v={}
        x1=value[value.columns[-1]].count()
        a1=value[value.columns[-1]].unique()
        for i in a1:
            v[i]=value[value.columns[-1]].str.count(i).sum()
        entropy= get_entropy_of_dataset(value)
        entropy_of_attribute= entropy_of_attribute+x1*entropy/x
    return abs(entropy_of_attribute)



'''Return Information Gain of the attribute provided as parameter'''
	#input:int/float/double/large,int/float/double/large
	#output:int/float/double/large
def get_information_gain(df,attribute):
    information_gain = 0
    entropy=get_entropy_of_dataset(df)
    entropya=get_entropy_of_attribute(df, attribute)
    information_gain= entropy-entropya
    return information_gain



''' Returns Attribute with highest info gain'''  
	#input: pandas_dataframe
	#output: ({dict},'str')     
def get_selected_attribute(df):
    information_gains={}
    selected_column=''
    for key in df.keys():
        if key!=df.columns.values[len(df.columns)-1]:
            information_gain=get_information_gain(df, key)
            information_gains[key]=information_gain

    selected_column= max(information_gains,key=information_gains.get)
    return (information_gains,selected_column)



'''
------- TEST CASES --------
How to run sample test cases ?

Simply run the file DT_SampleTestCase.py
Follow convention and do not change any file / function names

'''