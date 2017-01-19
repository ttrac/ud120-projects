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

### values for first record in dict
# print enron_data.itervalues().next()


### number of people in the file
print "people:", len(enron_data)


### number of attributes for each person
print "features:", len(enron_data.itervalues().next())


### total number of datapoints
print "values:", sum(len(v) for v in enron_data.itervalues())


### count of 'persons of interest' (POI)
def count_poi(d):
	count = 0
	for k, v in d.iteritems():
		if isinstance(v, dict):
			for l, u in v.iteritems():
				if l == 'poi' and u == True:
					count += 1
	print "poi count:", count
	return count

count_poi(enron_data)
poi_count = count_poi(enron_data)

### stock value for James Prentice 
print "stock value for James Prenctice:", enron_data['PRENTICE JAMES']['total_stock_value']


### emails from Wesley Colwell to persons of interest
print "emails to POI from Wesley Colwell:", enron_data['COLWELL WESLEY']['from_this_person_to_poi']


### stock options exercised by Jeffrey K Skilling
print "exercised stock from Jeff Skilling:", enron_data['SKILLING JEFFREY K']['exercised_stock_options']


### total payments comparison
print "total payments Jeff Skilling:", enron_data['SKILLING JEFFREY K']['total_payments']
print "total payments Kenneth Lay:", enron_data['LAY KENNETH L']['total_payments']
print "total payments Andrew Fastow:", enron_data['FASTOW ANDREW S']['total_payments']


### people with a quantified salary
def count_salary(d):
	count = 0
	for k, v in d.iteritems():
		if isinstance(v, dict):
			for l, u in v.iteritems():
				if l == 'salary' and u != 'NaN':
					count += 1
	print "salary count:", count

count_salary(enron_data)


### people with a known email address
def count_email_address(d):
	count = 0
	for k, v in d.iteritems():
		if isinstance(v, dict):
			for l, u in v.iteritems():
				if l == 'email_address' and u != 'NaN':
					count += 1
	print "email_address count:", count

count_email_address(enron_data)


### How many people in the dataset (as it currently exists) do not have a value for
### total payments? What percentage of people in the dataset as a whole is this?

def count_payments_null(d):
	count = 0
	for k, v in d.iteritems():
		if isinstance(v, dict):
			for l, u in v.iteritems():
				if l == 'total_payments' and u == 'NaN':
					count += 1
	print "null total_payments count:", count
	print "percentage:", count/float(len(enron_data))

count_payments_null(enron_data)


### POIs in the dataset with null total_payments? What percentage of POI as a whole is this?

def count_poi_payments_null(d):
	count = 0
	for k, v in d.iteritems():
		if isinstance(v, dict):
			for l, u in v.iteritems():
				if l == 'poi' and u == True:
					if l == 'total_payments' and u == 'NaN':
						count += 1
	print "POI with null total_payments:", count
	print "percentage:", count/float(poi_count)

count_poi_payments_null(enron_data)
