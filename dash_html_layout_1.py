import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import datetime

dataset = pd.read_excel("StockMarket_" + str(datetime.date.today()).replace('-','_') + '.xlsx',usecols=['Calls OI','Puts STRIKE PRICE','Puts OI','Nifty','Time_Stamp'])
max_time_stamp = dataset['Time_Stamp'].max()
dataset['Calls OI'] = dataset['Calls OI'].str.replace(",","")
dataset['Calls OI'] = dataset['Calls OI'].astype(float)
dataset['Puts OI'] = dataset['Puts OI'].str.replace(",","")
dataset['Puts OI'] = dataset['Puts OI'].astype(float)
new_data_set = dataset.loc[dataset.Time_Stamp == max_time_stamp].copy()
put_stock_prices = new_data_set['Puts STRIKE PRICE'].to_list()
# dataset['Time_Stamp'] = dataset['Time_Stamp'].str.replace(" IST","")

gds1 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[0]]
fig1 = px.line(gds1, x='Time_Stamp', y=["Calls OI","Nifty","Puts OI"], title='For Strike Price '+str(put_stock_prices[0]))
gds2 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[1]]
fig2 = px.line(gds2, x='Time_Stamp', y=["Calls OI","Nifty","Puts OI"], title='For Strike Price '+str(put_stock_prices[1]))
gds3 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[2]]
fig3 = px.line(gds3, x='Time_Stamp', y=["Calls OI","Nifty","Puts OI"], title='For Strike Price '+str(put_stock_prices[2]))

gds4 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[3]]
fig4 = px.line(gds4, x='Time_Stamp', y=["Calls OI","Nifty","Puts OI"], title='For Strike Price '+str(put_stock_prices[3]))
gds5 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[4]]
fig5 = px.line(gds5, x='Time_Stamp', y=["Calls OI","Nifty","Puts OI"], title='For Strike Price '+str(put_stock_prices[4]))
gds6 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[5]]
fig6 = px.line(gds6, x='Time_Stamp', y=["Calls OI","Nifty","Puts OI"], title='For Strike Price '+str(put_stock_prices[5]))

gds7 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[6]]
fig7 = px.line(gds7, x='Time_Stamp', y=["Calls OI","Nifty","Puts OI"], title='For Strike Price '+str(put_stock_prices[6]))
gds8 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[7]]
fig8 = px.line(gds8, x='Time_Stamp', y=["Calls OI","Nifty","Puts OI"], title='For Strike Price '+str(put_stock_prices[7]))
gds9 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[8]]
fig9 = px.line(gds9, x='Time_Stamp', y=["Calls OI","Nifty","Puts OI"], title='For Strike Price '+str(put_stock_prices[8]))


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(id='controls-container', children=[
    html.H1(children='Stock Market Personalized Dashboard'),
    html.Div(children=[
        dcc.Graph(id="graph1", style={'width': '67vh', 'height': '67vh','display': 'inline-block'}, figure=fig1),
        dcc.Graph(id="graph2", style={'width': '67vh', 'height': '67vh','display': 'inline-block'}, figure=fig2),
        dcc.Graph(id="graph3", style={'width': '67vh', 'height': '67vh','display': 'inline-block'}, figure=fig3),
        dcc.Graph(id="graph4", style={'width': '67vh', 'height': '67vh', 'display': 'inline-block'}, figure=fig4),
        dcc.Graph(id="graph5", style={'width': '67vh', 'height': '67vh', 'display': 'inline-block'}, figure=fig5),
        dcc.Graph(id="graph6", style={'width': '67vh', 'height': '67vh', 'display': 'inline-block'}, figure=fig6),
        dcc.Graph(id="graph7", style={'width': '67vh', 'height': '67vh', 'display': 'inline-block'}, figure=fig7),
        dcc.Graph(id="graph8", style={'width': '67vh', 'height': '67vh', 'display': 'inline-block'}, figure=fig8),
        dcc.Graph(id="graph9", style={'width': '67vh', 'height': '67vh', 'display': 'inline-block'}, figure=fig9)
    ])
])



if __name__ == '__main__':
    app.run_server(port=8065,debug=False)
