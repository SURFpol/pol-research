Tfidf keywords research results
===============================

This document briefly explains how to read the results in [tfidf-keywords.json](tfidf-keywords.json)

The ```id```,```url```, ```keywords``` and ```documents``` keys stem all from the original data, 
which is the stimuleringsregeling corpus.

```keywords_tfidf``` is a calculated result. It is calculated in the following steps:
1)  Split all ```keywords``` into unigrams
2)  Calculate tfidf for any unigram that appears in any of the texts. 
Unigrams that don't occur in any document are left out.
3)  Set the unigrams as keys and their tfidf as the value.

```noun_tfidf``` is also a calculated result. It gets calculated by these steps:
1)   Filter all the nouns from each text
2)   Calculate the tfidf for only the nouns
3)   Select the 10 nouns with the highest tfidf
4)   Set the nouns as keys and their tfidf as the value

There are 20 sources in the results. A source may contain multiple documents, 
but those documents share the same keywords. 
We selected the 20 sources that have the highest sum of ```tfidf_keywords``` values.
This means these sources have the most informative keywords (based on tfidf). 

Especially the course named "Praktische muzieknotatie en audiobewerking", shows sources where ```tfidf_nouns```
is very informative. Just by reading those nouns you get a picture what the lesson is about.
That course material is in PDF.
So Tika is at least capable of reading sufficient amounts of texts from some of the PDF's.    
