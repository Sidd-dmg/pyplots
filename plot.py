from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server

_pltdata = pd.read_csv('_week2.csv',sep=",")



app.layout = html.Div([
    html.H4('Data Analysis of Electricity Consumption. '),
    dcc.Dropdown(_pltdata.columns, id='dropdown'),
     dcc.Graph(id="graph"),
    #html.Div(id='pandas-output-container-1')
])



@app.callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def update_line_chart(val_chosen):
    pltdata = pd.read_csv('_week2.csv',sep=',') # replace with your own data source
    para=val_chosen
    print(para)
    fig = px.line(pltdata, x='time', y=para)
    fig.update_layout(
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True,
                   height=800, width= 1900)
    return fig

if __name__ == "__main__":
    app.run_server(debug=False)

