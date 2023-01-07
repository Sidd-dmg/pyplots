from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

#_pltdata = pd.read_csv('D:\\Project_TeamPower\\webdevelopment\\New folder\\_week2.csv',sep=",")

_pltdata = ['Ptot','Pr','Py','Pb','Pfavg','Pfr','Pfy','Pfb','St','Sr','Sy','Sb','Vlavg','Vry','Vyb','Vbr','Vlnavg','Vr','Vy','Vb','Itot','Ir','Iy','Ib','freq','Energy','vah']

app.layout = html.Div([
    html.H1('Data Analysis of Electricity Consumption. '),
    html.I("Select the date for ploting.[format:YYYY-MM-DD]"),
    html.Br(),
    dcc.Input(id="dates", type="text", placeholder="", debounce=True ,value="2022-10-01"),
    dcc.Dropdown(_pltdata, id='dropdown'),
    dcc.Graph(id="graph"),
    #html.Div(id='pandas-output-container-1')
])



@app.callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"),
    Input("dates","value"))
def update_line_chart(dropdown,dates):
    push_date = "indouk_4_"+str(dates)+".txt"

    path= "data/" + push_date # Plz add github file locatio path in "".in this kind of format 'D:\\Project_TeamPower\\webdevelopment\\New folder\\_week2.csv'

    data_write = 'time,meter,Ptot,Pr,Py,Pb,Pfavg,Pfr,Pfy,Pfb,St,Sr,Sy,Sb,Vlavg,Vry,Vyb,Vbr,Vlnavg,Vr,Vy,Vb,Itot,Ir,Iy,Ib,freq,Energy,vah'

    output_file = open('Data.csv','w')
    with open(path,'r') as scan:
       output_file.write(data_write+'\n')
       output_file.write(scan.read())
    output_file.close()
   
    data_path='Data.csv' # here add  the path of output file generated in "" similar to 'D:\\Project_TeamPower\\webdevelopment\\New folder\\_week2.csv' format

    pltdata = pd.read_csv(data_path,sep=',') # replace with your own data source
    para=dropdown
    print(para)
    fig = px.line(pltdata, x='time', y=para)
    fig.update_layout(
                  #plot_bgcolor='rgb(230, 230,230),
                   showlegend=True,
                   height=800)
    return fig


app.run_server(debug=True)

