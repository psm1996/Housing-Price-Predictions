import pandas as pd 
data=pd.read_csv('total_dataset.csv',converters={"House ID": lambda x: int(x,16)})
labels=pd.read_csv('house_prices.csv',converters={"House ID": lambda x: int(x,16)})

print (data.info())
print('='*40)
print (labels.info())
print ('='*40)

# using merge function of pandas library to add Golden Price(target) in created dataset
df=pd.merge(data,labels,how='outer')
# sorting will help to split these dataset as missing files are sorted
df.sort_values(by=['House ID'],inplace=True)

#train test split by slicing
train=df[:16500]
test=df[16500:]


# saving to csv files
print (train.info(),test.info())
df.to_csv('Final_dataset.csv',index=False)
train.to_csv('train_dataset.csv',index=False)
test.to_csv('test_dataset.csv',index=False)
print (df.info())
print('='*40)
print (df.columns.values)
print('='*40)
print('Test and Train datasets are created successfully !')