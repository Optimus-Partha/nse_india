import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(id='controls-container', style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Stock Market Dashboard', style={
        'textAlign': 'center',
        'color': colors['text']}),

    html.Div(children=[
        dcc.Graph(id="graph1", style={'width': '68.20vh', 'height': '67.5vh', 'display': 'inline-block'},
                  animate=True),
        dcc.Graph(id="graph2", style={'width': '68.20vh', 'height': '67.5vh', 'display': 'inline-block'},
                  animate=True),
        dcc.Graph(id="graph3", style={'width': '68.30vh', 'height': '67.5vh', 'display': 'inline-block'},
                  animate=True),
        dcc.Graph(id="graph4", style={'width': '68.20vh', 'height': '68.20vh', 'display': 'inline-block'},
                  animate=True),
        dcc.Graph(id="graph5", style={'width': '68.20vh', 'height': '68.20vh', 'display': 'inline-block'},
                  animate=True),
        dcc.Graph(id="graph6", style={'width': '68.30vh', 'height': '68.20vh', 'display': 'inline-block'},
                  animate=True),
        dcc.Graph(id="graph7", style={'width': '68.20vh', 'height': '68.20vh', 'display': 'inline-block'},
                  animate=True),
        dcc.Graph(id="graph8", style={'width': '68.20vh', 'height': '68.20vh', 'display': 'inline-block'},
                  animate=True),
        dcc.Graph(id="graph9", style={'width': '68.30vh', 'height': '68.20vh', 'display': 'inline-block'}, animate=True)
    ]),
    html.H6(children='Powered By Partha  ', style={
            'textAlign': 'right',
            'color': colors['text']}),
    dcc.Interval(
        id='graph-update',
        interval=60000,
        n_intervals=0
    )
])


@app.callback(
    [Output('graph1', 'figure'), Output('graph2', 'figure'), Output('graph3', 'figure'),
     Output('graph4', 'figure'), Output('graph5', 'figure'), Output('graph6', 'figure'),
     Output('graph7', 'figure'), Output('graph8', 'figure'), Output('graph9', 'figure')],
    [Input('graph-update', 'n_intervals')]
)
def update_graph_scatter(n):
    dataset = pd.read_excel("StockMarket_" + str(datetime.date.today()).replace('-', '_') + '.xlsx',
                            usecols=['Calls OI', 'Puts STRIKE PRICE', 'Puts OI', 'Nifty', 'Time'])
    max_Time = dataset['Time'].max()
    dataset['Calls OI'] = dataset['Calls OI'].str.replace(",", "")
    dataset['Calls OI'] = dataset['Calls OI'].astype(float)
    dataset['Puts OI'] = dataset['Puts OI'].str.replace(",", "")
    dataset['Puts OI'] = dataset['Puts OI'].astype(float)
    new_data_set = dataset.loc[dataset.Time == max_Time].copy()
    put_stock_prices = new_data_set['Puts STRIKE PRICE'].to_list()
    # dataset['Time'] = dataset['Time'].str.replace(" IST","")


    gds1 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[0]]
    fig1 = px.line(gds1, x='Time', y=["Calls OI", "Nifty", "Puts OI"],
                   title='Strick Price ' + str(put_stock_prices[0]),template='plotly_dark')
    fig1.update_layout(title_x=0.5)
    # fig1.update_layout(
    #         title={
    #         'y': 0.9,
    #         'x': 0.5,
    #         'xanchor': 'center',
    #         'yanchor': 'top'},
    #     font_family="Courier New",
    #     font_color="white",
    #     title_font_color="white",
    #     legend_title_font_color="white",
    #     paper_bgcolor='rgba(35, 39, 41, 1)',
    #     plot_bgcolor='rgba(0,0,0,0)',
    #     xaxis=dict(ticks="outside", mirror=False, showline=True,showgrid=False),
    #     yaxis=dict(ticks="outside", mirror=False, showline=True,showgrid=False)
    # )
    # fig1.update_xaxes(showline=True,showgrid=False)
    # fig1.update_yaxes(showline=True,showgrid=False)

    gds2 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[1]]
    fig2 = px.line(gds2, x='Time', y=["Calls OI", "Nifty", "Puts OI"],
                   title='Strick Price ' + str(put_stock_prices[1]),template='plotly_dark')
    fig2.update_layout(title_x=0.5)
    gds3 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[2]]
    fig3 = px.line(gds3, x='Time', y=["Calls OI", "Nifty", "Puts OI"],
                   title='Strick Price ' + str(put_stock_prices[2]),template='plotly_dark')
    fig3.update_layout(title_x=0.5)
    gds4 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[3]]
    fig4 = px.line(gds4, x='Time', y=["Calls OI", "Nifty", "Puts OI"],
                   title='Strick Price ' + str(put_stock_prices[3]),template='plotly_dark')
    fig4.update_layout(title_x=0.5)
    gds5 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[4]]
    fig5 = px.line(gds5, x='Time', y=["Calls OI", "Nifty", "Puts OI"],
                   title='Strick Price ' + str(put_stock_prices[4]),template='plotly_dark')
    fig5.update_layout(title_x=0.5)
    gds6 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[5]]
    fig6 = px.line(gds6, x='Time', y=["Calls OI", "Nifty", "Puts OI"],
                   title='Strick Price ' + str(put_stock_prices[5]),template='plotly_dark')
    fig6.update_layout(title_x=0.5)
    gds7 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[6]]
    fig7 = px.line(gds7, x='Time', y=["Calls OI", "Nifty", "Puts OI"],
                   title='Strick Price ' + str(put_stock_prices[6]),template='plotly_dark')
    fig7.update_layout(title_x=0.5)
    gds8 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[7]]
    fig8 = px.line(gds8, x='Time', y=["Calls OI", "Nifty", "Puts OI"],
                   title='Strick Price ' + str(put_stock_prices[7]),template='plotly_dark')
    fig8.update_layout(title_x=0.5)
    gds9 = dataset.loc[dataset['Puts STRIKE PRICE'] == put_stock_prices[8]]
    fig9 = px.line(gds9, x='Time', y=["Calls OI", "Nifty", "Puts OI"],
                   title='Strick Price ' + str(put_stock_prices[8]),template='plotly_dark')
    fig9.update_layout(title_x=0.5)
    return fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9


if __name__ == '__main__':
    app.run_server(port=8065, debug=False)
