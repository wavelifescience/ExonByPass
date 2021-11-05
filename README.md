# README #

### Requirements ###

* Python with Tensorflow and Keras packages

### OR ###

* R with Tensorflow and Keras packages

## Input CSV ##

See Example_input_table.csv for formating. Each row represents 100 amino acid that are converted to a numeric using the Amino Acid Numeric Mapping Table.csv. 

* The first 25 amino acids (1-25) should represent the last 25 amino acids of the the exon upstream of the exon of interest.

* The next 25 amino acids (26-50) should represent the 1st 25 amino acids of the exon of interest.

* The next 25 amino acids (51-75) should represent the last 25 amino acids of the exon of interest.

* The last 25 amino acids (76-100) should represent the first 25 amino acids of the exon downstream of the exon of interest.

See NAR publication Predicting Exon Criticality from Protein Sequence Figure 1A for more detail. 

# Usage #

## Python ##
```
python ./predict_python.py
```
## R ##
```R
library(keras)
library(tensorflow)

testset=read.csv("Example_input_table.csv",stringsAsFactors = F) 
testset=as.matrix(testset)   
model=keras::load_model_hdf5(filepath = "Exon_ByPass_v01.h5")
probs=keras::predict_proba(model, testset)
write.csv(probs,file = "out_probs.csv")
```
