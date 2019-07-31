
import pandas as pd


ecom = pd.read_csv('Ecommerce Purchases')


ecom.head()



ecom.info()



ecom['Purchase Price'].mean(



ecom['Purchase Price'].max()



ecom['Purchase Price'].min()



ecom[ecom['Language']=='en'.count()



ecom[ecom['Job'] == 'Lawyer'].info()



ecom['AM or PM'].value_counts()



ecom['Job'].value_counts().head(5)



ecom[ecom['Lot']=='90 WT']['Purchase Price']

ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()



sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25')



ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)


