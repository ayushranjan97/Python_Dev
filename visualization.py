import urllib.request
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import os



#download a file from an url into a specified location

if os.path.exists('/Users/SWARNALI DATTA//Downloads/covid.csv'):
    os.remove('/Users/SWARNALI DATTA//Downloads/covid.csv')

print('Beginning the file download.....')
url='https://covid.ourworldindata.org/data/full_data.csv'
urllib.request.urlretrieve(url,'/Users/Ayush/Downloads/covid.csv')
print("Download Complete")


#add csv file to dataframe
data = pd.read_csv('/Users/Ayush/Downloads/covid.csv')
 #create bar graph

df = pd.DataFrame(data)

df.plot(x="location",y=["total_cases","total_deaths"],kind="bar")
# Show the plot
plt.show()



