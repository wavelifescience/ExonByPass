library(keras)
library(tensorflow)

testset=read.csv("Example_input_table.csv",stringsAsFactors = F) 
testset=as.matrix(testset)   
model=keras::load_model_hdf5(filepath = "Exon_ByPass_v01.h5")
probs=keras::predict_proba(model, testset)
write.csv(probs,file = "out_probs.csv")
