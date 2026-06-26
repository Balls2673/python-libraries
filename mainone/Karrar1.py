medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
from urllib.request import urlretrieve
#urlretrieve(URL, "filename.csv") URL →   هو الملف الذي يتم تحميله من الإنترنت"filename.csv" → هو اسم حفظه على جهازك  
urlretrieve(medical_charges_url, 'medical.csv')
import pandas as pd
#تم فتح الملف و تحويله إلى جدول يسمى DataFrame, DataFrame = جدول مثل Excel يحتوي صفوف وأعمدة
medical_df = pd.read_csv('medical.csv')

print(medical_df.describe())
print(medical_df.info())

import jovian 
jovian.commit()