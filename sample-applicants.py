# sample-applicants.py
# Description: Randomly generates a CSV list of participants, based on various criteria for distribution
# By: Stuart Geiger (@staeiou) 
# Licensed: Revised BSD 3-clause
# For: Semi-Automated Participant Selection Project, Astro Hack Week 2015
# https://hackpad.com/Semi-Automatic-Participant-Selection-for-Conferences-WgmWoSiovcq


# pip install names
import names
import numpy

num_applicants = 300

gender_categories = ['male','female','']
gender_probability = [.33,.66,.01]

career_categories = ['grad-student','junior-faculty','senior-faculty','']
career_probability = [.1,.5,.3,.1]

country_categories = ['OECD','non-OECD','']
country_probability = [.90,.09,.01]

subfield_categories = ['solar','cosmology','astrophysics','exoplanets','']
subfield_probability = [.1,.5,.2,.1,.1]

print("name, gender, career_stage, country, subfield")


for count in range(num_applicants):
    
    c_gender = numpy.random.choice(gender_categories, p=gender_probability)
    c_full_name = names.get_full_name(gender=c_gender)
    c_career_stage = numpy.random.choice(career_categories, p=career_probability)
    c_country = numpy.random.choice(country_categories, p=country_probability)
    c_subfield = numpy.random.choice(subfield_categories, p=subfield_probability)
    
    print(c_full_name,c_gender,c_career_stage,c_country,c_subfield, sep=", ")
