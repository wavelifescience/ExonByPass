import pandas as pd
testset = pd.read_csv("Example_input_table.csv")

from tensorflow import keras 
from tensorflow.keras.models import load_model
model = load_model('Exon_ByPass_v01.h5')
y=model.predict(testset)

output_table = pd.DataFrame(y, columns = ['out'])
output_table.to_csv("out_probs.csv")
print(output_table)
