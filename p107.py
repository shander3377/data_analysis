
import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("C:/Users/pankaj/Desktop/agrim/coding/c97/Data-Analysis-by-visualisation/data.csv")

means = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

fig = px.scatter(means, 
x="student_id",
 y="level", 
 size="attempt", 
 color="attempt")

fig.show()
