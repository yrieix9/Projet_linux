import pandas as pd

import dash

from dash import dcc

from dash import html

from dash.dependencies import Input, Output

import datetime

import schedule



# Charger les données à partir du fichier CSV


df = pd.read_csv('/home/admin/prix.csv', parse_dates=['Date'])



# Créer l'application Dash


app = dash.Dash(__name__)



# Définir le layout de l'application


app.layout = html.Div(children=[


html.H1(children='Prix de l\'action Biocorp'),


 # Ajouter un graphique


dcc.Graph(


id='example-graph'


),



 # Ajouter un intervalle de temps pour la mise à jour automatique du dashboard


dcc.Interval(


id='interval-component',


interval=1*60*1000, # en millisecondes


n_intervals=0


)


])


# Définir la fonction de mise à jour du graphique


@app.callback(Output('example-graph', 'figure'),


[Input('interval-component', 'n_intervals')])


def update_graph(n):


 # Charger les données à partir du fichier CSV


df = pd.read_csv('/home/admin/prix.csv', parse_dates=['Date'])


    


 # Créer la figure pour le graphique


fig = {


'data': [


{'x': df['Date'], 'y': df['Prix'], 'type': 'line', 'name': 'Prix de l\'action>


],


'layout': {


'title': 'Prix de l\'action Biocorp',


'xaxis': {'title': 'Date'},


'yaxis': {'title': 'Prix'}


}


}


    


return fig



# Définir la fonction pour générer le rapport quotidien


def generate_daily_report():


 # Charger les données à partir du fichier CSV


df = pd.read_csv('/home/admin/prix.csv', parse_dates=['Date'])


    


 # Calculer les métriques


open_price = df.iloc[0]['Prix']


close_price = df.iloc[-1]['Prix']


daily_volatility = df['Prix'].pct_change().std() * 100


evolution = (close_price - open_price) / open_price * 100


    


 # Afficher le rapport


print('Daily report for', datetime.datetime.today().strftime('%Y-%m-%d'))


print('Open price:', open_price)


print('Close price:', close_price)


print('Daily volatility:', daily_volatility)


print('Evolution:', evolution)



# Planifier la génération du rapport quotidien à 8pm chaque jour


schedule.every().day.at('20:00').do(generate_daily_report)


if __name__ == '__main__':


app.run_server(host='0.0.0.0',debug=True)
