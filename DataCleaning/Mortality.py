import pandas as pd
import matplotlib.pyplot as plt 
import warnings
warnings.filterwarnings("ignore")

#reading the data file
data=pd.read_csv('data.csv')



#=========================================================================================================================================================
	#Question1 : Plot a graph to gain insights into the underfive Mortality rates of all the countries in the year 1990 sorted in an ascending order
	#if the Graph is too dense then display first 10 and last 10 countries

#=========================================================================================================================================================

#filtering the data for 1990
y90 = data[data['Year']==1990]

#sorting the 1990 data based on mortality rates
One = y90.sort_values('Under-five mortality rate (probability of dying by age 5 per 1000 live births)',ascending=True)

#cleans the under five mortality rate column and takes the integer value for plotting
for i in range(One.shape[0]):
	One['Under-five mortality rate (probability of dying by age 5 per 1000 live births)'].iloc[i]=int(float(One['Under-five mortality rate (probability of dying by age 5 per 1000 live births)'].iloc[i][:4]))

#taking the first 10 frames and the last 10 frames to avoid crowding of bar graphs
One=pd.concat([One[:10],One[-10:]])
#plotting the data with country on x axis and under-five mortality rate on y axis
ax=One.plot('Country','Under-five mortality rate (probability of dying by age 5 per 1000 live births)',kind='bar',title="Question1:The First and The last 10 Countries: ")

#setting the x and y axis
ax.set_xlabel("Country")
ax.set_ylabel("Mortality Rate")
ax.legend(loc='best')

#restricting the x axis till 20 countries
plt.locator_params(nbins=20)
#displaying the plot
plt.show()

#=========================================================================================================================================================
	#Question2 : Plot a graph to gain insights into the underfive Mortality rates of all the countries in the year 2015 sorted in an ascending order
	#if the Graph is too dense then display first 10 and last 10 countries

#=========================================================================================================================================================

#filtering the data for 2015
y15 = data[data['Year']==2015]
#sorting the 1990 data based on mortality rates
Two = y15.sort_values('Under-five mortality rate (probability of dying by age 5 per 1000 live births)',ascending=True)
#cleans the under five mortality rate column and takes the integer value for plotting
for i in range(Two.shape[0]):
	Two['Under-five mortality rate (probability of dying by age 5 per 1000 live births)'].iloc[i]=int(float(Two['Under-five mortality rate (probability of dying by age 5 per 1000 live births)'].iloc[i][:4]))

#taking the first 10 frames and the last 10 frames to avoid crowding of bar graphs
Two=pd.concat([Two[:10],Two[-10:]])
#plotting the data with country on x axis and under-five mortality rate on y axis
ax=Two.plot('Country','Under-five mortality rate (probability of dying by age 5 per 1000 live births)',kind='bar',title="Question2:The First and The last 10 Countries: ")

ax.set_xlabel("Country")
ax.set_ylabel("Mortality Rate")
ax.legend(loc='best')

#restricting the x axis till 20 countries
plt.locator_params(nbins=20)
#displaying the plot
plt.show()


#=========================================================================================================================================================
	#Question3 : Plot a graph to gain insights into the underfive Mortality rates for any three countries of you choice from 1990 to 2015.
	#Display the graph as line trends from 1990 to 2015 

#=========================================================================================================================================================

Count3=pd.concat([data[data['Country']=='China'],data[data['Country']=='Canada'],data[data['Country']=='Bahrain']])
#cleans the under five mortality rate column and takes the integer value for plotting
for i in range(Count3.shape[0]):
	Count3['Under-five mortality rate (probability of dying by age 5 per 1000 live births)'].iloc[i]=int(float(Count3['Under-five mortality rate (probability of dying by age 5 per 1000 live births)'].iloc[i][:4]))
	Count3['Neonatal mortality rate (per 1000 live births)'].iloc[i]=int(float(Count3['Neonatal mortality rate (per 1000 live births)'].iloc[i][:4]))
	Count3['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'].iloc[i]=int(float(Count3['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'].iloc[i][:4]))

# fig,ax=plt.subplots()

for name in ['Bahrain','Canada','China']:
	ax.plot(Count3[Count3['Country']==name].Year,Count3[Count3['Country']==name]['Under-five mortality rate (probability of dying by age 5 per 1000 live births)'],label=name)

ax.set_xlabel('Year')
ax.set_ylabel('Mortality Rate')
ax.legend(loc='best')
plt.title('Question3:The mortality rate trends: ')
plt.show()


#=========================================================================================================================================================
	#Question4 : Plot a bar graph to gain insights into the Reduction rates of any three countries 
	#the reduction rate of a country is the mortality rate of 2015 divided by the reduction rate of 1990
#=========================================================================================================================================================

# fig,ax=plt.subplots()
names=list()
values=list()
for name in ['Bahrain','Canada','China']:
	a=Count3[(Count3['Country']==name) & (Count3['Year']==1990)]['Under-five mortality rate (probability of dying by age 5 per 1000 live births)']
	b=Count3[(Count3['Country']==name) & (Count3['Year']==2015)]['Under-five mortality rate (probability of dying by age 5 per 1000 live births)']
	names.append(name)
	values.append(a.iloc[0]//b.iloc[0])
	

plt.bar(names,values)
plt.xlabel('Country')
plt.ylabel('Reduction Rate')
plt.title('Question4: Reduction Ratios of the companies')
plt.show()


# Count3 = Count3[Count3['Year']==2015].drop('Year',1)
# bah=Count3[Count3['Country']=='Bahrain']
# arg=Count3[Count3['Country']=='Argentina']
# chi=Count3[Count3['Country']=='China']
# can=Count3[Count3['Country']=='Canada']

# up=[arg['Under-five mortality rate (probability of dying by age 5 per 1000 live births)'],bah['Under-five mortality rate (probability of dying by age 5 per 1000 live births)'],chi['Under-five mortality rate (probability of dying by age 5 per 1000 live births)'],can['Under-five mortality rate (probability of dying by age 5 per 1000 live births)']]
# np=[arg['Neonatal mortality rate (per 1000 live births)'],bah['Neonatal mortality rate (per 1000 live births)'],chi['Neonatal mortality rate (per 1000 live births)'],can['Neonatal mortality rate (per 1000 live births)']]
# ip=[arg['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'],bah['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'],chi['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'],can['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)']]

