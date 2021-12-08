# import plotly
# from plotly.offline import plot
# from plotly.subplots import make_subplots
# import plotly.graph_objects as go
# import plotly.express as px
#
# fig = make_subplots(
# rows=2, cols=2, shared_xaxes=True,
# vertical_spacing=0.02,horizontal_spacing=0.02)
#
# df = px.data.gapminder().query("continent=='Oceania'")
# # fig = px.line(df, x="year", y="lifeExp", color='country')
#
# fig.add_trace(px.line(df, x="year", y="lifeExp", color='country'),
#           row=1, col=2)
#
# fig.add_trace(px.line(df, x="year", y="lifeExp", color='country'),
#           row=2, col=1)
#
# fig.add_trace(px.line(df, x="year", y="lifeExp", color='country'),
#           row=1, col=1)
#
# # fig.add_trace(go.Scatter(x=[6, 7, 8], y=[1000, 1100, 1200]),
# #           row=2, col=1)
#
# fig.update_layout(height=1200, width=600,
#               title_text="Stacked Subplots with Shared X-Axes")
# fig['layout']['yaxis1'].update(domain=[0, 0.2])
# fig['layout']['yaxis2'].update(domain=[0.3, 0.7])
# fig['layout']['yaxis3'].update(domain=[0.8, 1])
#
# plotly.offline.plot(fig, filename='name.html')

import plotly.express as px
import pandas as pd
import plotly

dataset = pd.read_excel(r'C:\Users\partha.singha\PycharmProjects\StockMarket\StockMarket_2021_12_06.xlsx',usecols=['Calls OI','Puts STRIKE PRICE','Puts OI','Nifty','Time_Stamp'])
max_time_stamp = dataset['Time_Stamp'].max()
dataset['Calls OI'] = dataset['Calls OI'].str.replace(",","")
dataset['Calls OI'] = dataset['Calls OI'].astype(float)
dataset['Puts OI'] = dataset['Puts OI'].str.replace(",","")
dataset['Puts OI'] = dataset['Puts OI'].astype(float)
new_data_set = dataset.loc[dataset.Time_Stamp == max_time_stamp].copy()
put_stock_prices = new_data_set['Puts STRIKE PRICE'].to_list()
gds1 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[3]]
fig1 = px.line(gds1, x='Time_Stamp', y=["Calls OI","Puts OI"])
plotly.offline.plot(fig1)