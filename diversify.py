import pandas as pd
import csv
from itertools import combinations
import os

name_of_file = input('please provide the name of the file: ')
issue_gender= int(input('how big of an importance does gender have on your life (out of 5): '))
issue_race= int(input('how big of an importance does race have on your life (out of 5): '))

data = pd.read_csv(name_of_file, dtype= {'Gender' :'category', 'Race' : 'category'} )
groups_q = int(input("group size: "))
best_diversity= 100 #arbitrary value
best_diversity_index= 0
for i in list(combinations(data.index,groups_q)):
    comb=data.loc[i,:] # one by one comb
    genderval= comb.Gender.value_counts()
    raceval= comb.Race.value_counts()
    diversity_score= issue_gender* genderval.std(ddof=0)+ issue_race* raceval.std(ddof=0) # can change the diversity_score
    if diversity_score < best_diversity:
        best_diversity = diversity_score
        best_diversity_index = i

comb=data.loc[best_diversity_index,:]
print("the most diverse group within the given csv file is, ")
print(comb)

os.system("pause")