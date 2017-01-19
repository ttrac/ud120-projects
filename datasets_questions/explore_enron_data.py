#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
from collections import Counter


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# number of people in the file
print "people:", len(enron_data)

# number of attributes for each person
print "features:", len(enron_data.itervalues().next())

# total number of datapoints
print "values:", sum(len(v) for v in enron_data.itervalues())

# count of 'persons of interest' (POI)
def count_poi(d):
	count = 0
	for k, v in d.iteritems():
		if isinstance(v, dict):
			for l, u in v.iteritems():
				if l == 'poi' and u == True:
					count += 1
	print "poi count:", count

count_poi(enron_data)
