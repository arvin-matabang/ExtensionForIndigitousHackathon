#----------
#keywordProcessor.py
#about:         takes an article and outputs a list of keywords
#created:       october 14, 2020
#author:        arvin ramos matabang, 9:24
#----------

#----------
#package imports
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

def findKeywords (input):
    output = []
    doc = nlp(input)
    for i in doc.ents:
        if i.label_ == "PERSON" or i.label_ == "NORP" or i.label_ == "FAC" or i.label_ == "ORG" or i.label_ == "GPE" or i.label_ == "LOC" or i.label_ == "PRODUCT" or i.label_ == "EVENT" or i.label_ == "WORK_OF_ART" or i.label_ == "LAW" or i.label_ == "LANGUAGE":
            output.append(i.text)
    return output
