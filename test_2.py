import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

dataset = pd.read_excel(r'C:\Users\partha.singha\PycharmProjects\StockMarket\StockMarket_2021_12_03.xlsx',usecols=['Calls OI','Puts STRIKE PRICE','Puts OI','Nifty','Time_Stamp'])
max_time_stamp = dataset['Time_Stamp'].max()
new_data_set = dataset.loc[dataset.Time_Stamp == max_time_stamp].copy()
put_stock_prices = new_data_set['Puts STRIKE PRICE'].to_list()

gds1 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[3]]
fig1 = px.line(gds1, x='Time_Stamp', y=["Calls OI","Puts OI"], title='For Strike Price '+str(put_stock_prices[3]))
gds2 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[4]]
fig2 = px.line(gds2, x='Time_Stamp', y=["Calls OI","Puts OI"], title='For Strike Price '+str(put_stock_prices[4]))
gds3 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[5]]
fig3 = px.line(gds3, x='Time_Stamp', y=["Calls OI","Puts OI"], title='For Strike Price '+str(put_stock_prices[5]))


app.layout = html.Div(children=[
    html.H1(children='Stock Market Personalized Dashboard'),

    html.Div(children='''
        STRIKE PRICE BEHAVIOUR
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig1
    ),
    dcc.Graph(
            id='example-graph2',
            figure=fig2
    ),
    dcc.Graph(
        id='example-graph3',
        figure=fig3
    ),
])

if __name__ == '__main__':
    app.run_server()