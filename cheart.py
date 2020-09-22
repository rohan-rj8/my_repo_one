import pandas as pd
from bokeh.plotting import figure, output_file, show
def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)

links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}
p_data = pd.read_csv(links['GDP'])
print(p_data)

csv_path=links["GDP"]
d1=pd.read_csv(csv_path)            #defining the dataframe
d1.head()                           #displaying first five rows of the dataframe

csv_path1=links["unemployment"]
d2=pd.read_csv(csv_path1)                   #defining the dataframe
d2.head()                                   #displaying first five rows of the dataframe


d3=d2[d2['unemployment']>8.5]                #extracting the part of the dataframe d2 to a new dataframe
d3

csv_path1=links['GDP']
gdp_dataframe1=pd.read_csv(csv_path1)
x = pd.DataFrame(gdp_dataframe1, columns=['date'])
x.head()

csv_path2=links['GDP']
gdp_dataframe2=pd.read_csv(csv_path2)
gdp_change = pd.DataFrame(gdp_dataframe2, columns=['change-current'])
gdp_change.head()

csv_path3=links['unemployment']
unemploy_dataframe1= pd.read_csv(csv_path3)
unemployment = pd.DataFrame(unemploy_dataframe1, columns=['unemployment'])
unemployment.head()

title = "Unemployment stats according to GDP"

file_name = "index.html"

make_dashboard(x=x, gdp_change=gdp_change, unemployment=unemployment, title=title, file_name=file_name)

