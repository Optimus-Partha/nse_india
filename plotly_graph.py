import plotly.graph_objects as go
import plotly
import pandas as pd

df = pd.read_excel(r'C:\Users\partha.singha\PycharmProjects\StockMarket\StockMarket_2021_11_23.xlsx')

fig = go.Figure([go.Scatter(x=df['Time_Stamp'], y=df['Calls VOLUME'])])
fig_2 = go.Figure([go.Scatter(x=df['Time_Stamp'], y=df['Nifty'])])

plotly.offline.plot(fig_2)
