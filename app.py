import dash
from dash import dcc,html
from dash.dependencies import Input, Output, State



########### Define your variables ######
myheading1='Diamond Price Prediction (from 54k dataset, 4 Cs - Carat, Cut, Color, Clarity)'
image1='Diamond.png'
tabtitle = 'Diamond Price Prediction'
sourceurl = 'https://www.kaggle.com/datasets/shivam2503/diamonds'
githublink = 'https://github.com/Malathy-Muthu/501-linear-reg-ames-housing'


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([
        html.Img(src=app.get_asset_url(image1), style={'width': '30%', 'height': 'auto'}, className='four columns'),
        html.Div([
                html.H3('Features of Diamond:'),
                html.Div('Carat'),
                dcc.Input(id='carat', value=0.5, type='number', min=0.2, max=5.01, step=0.1),
                html.Div('Cut-Fair(1), Good, Very Good, Premium, Ideal(5)'),
                dcc.Input(id='cut', value=2, type='number', min=1, max=5, step=1),
                html.Div('Color-from J-worst(1) to D-best(7)'),
                dcc.Input(id='color', value=4, type='number', min=1, max=7, step=1),
                html.Div('Clarity-I1-worst(1), SI2, SI1, VS2, VS1, VVS2, VVS1, IF-best(8))'),
                dcc.Input(id='clarity', value=3, type='number', min=1, max=8, step=1),
                html.Div('y:width in mm'),
                dcc.Input(id='y', value=3.0, type='number', min=1.0, max=10.9, step=.1),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Div('Predicted Price = (-4472.18 * Baseline) + ($10253.31 * carat) +  (-652.38 * y) + ($111.72 * cut) + ($325.83 * color) + ($519.77 * clarity)',style={'font-family':'verdana','color': 'green', 'fontSize': 20}),
                html.Br(),
                html.Div('R square = 0.9040',style={'font-family':'verdana','color': 'green', 'fontSize': 20}),
                html.Br(),
                html.Br(),
                html.A('Google Spreadsheet', href='https://docs.google.com/spreadsheets/d/1ktCtc4LMj2AbaLN8J349vXZ7X7M434XfR43h8YRKmzo/edit#gid=0'),
                html.Br(),
                html.A('Code on Github', href=githublink),
                html.Br(),
                html.A("Data Source", href=sourceurl)

            ], className='four columns'),
            html.Div([
                html.Button(children='Submit', id='submit-val', n_clicks=0,
                                style={
                                'background-color': 'green',
                                'color': 'white',
                                'margin-left': '5px',
                                'verticalAlign': 'center',
                                'horizontalAlign': 'center'}
                                ),
                html.H3('Predicted Diamond Price:'),
                html.Div(id='Results')
            ], className='four columns')
        ], className='twelve columns',
    ),
    html.Br()

    ]
)
######### Define Callback
@app.callback(
    Output(component_id='Results', component_property='children'),
    Input(component_id='submit-val', component_property='n_clicks'),
    State(component_id='carat', component_property='value'),
    State(component_id='cut', component_property='value'),
    State(component_id='color', component_property='value'),
    State(component_id='clarity', component_property='value'),
    State(component_id='y', component_property='value')

)
def ames_lr_function(clicks,carat,cut,color,clarity,y):
    if clicks==0:
        return "waiting for inputs"
    else:
        y = [-4472.18 + 10253.31*carat + 111.72*cut + 325.83*color + 519.77*clarity+ -652.38*y]
        formatted_y = "${:,.2f}".format(y[0])
        return formatted_y



############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
