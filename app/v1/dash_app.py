import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import requests

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Stock Data Viewer"),
    dcc.Input(id='stock-input', value='AAPL', type='text'),
    html.Button('Submit', id='submit-btn'),
    dcc.Graph(id='stock-graph')
])

@app.callback(
    Output('stock-graph', 'figure'),
    [Input('submit-btn', 'n_clicks')],
    [Input('stock-input', 'value')]
)
def update_graph(n_clicks, ticker):
    if n_clicks is not None:

        response = requests.get(f'http://web:8080/stocks/{ticker}')
        data = response.json()

        dates = [entry['Date'] for entry in data]
        close_prices = [entry['Close'] for entry in data]

        return {
            'data': [go.Scatter(x=dates, y=close_prices, mode='lines', name=ticker)],
            'layout': go.Layout(title=f'Stock Price for {ticker}')
        }

    return {}

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
