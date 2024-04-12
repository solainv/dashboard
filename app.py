
# # Import erforderlicher Bibliotheken
# import pandas as pd
# import plotly.graph_objects as go
# import plotly.express as px
# import dash
# from dash import dcc
# from dash import html
# from dash.dependencies import Input, Output, State

# # Daten importieren
# airline_data = pd.read_csv('airline_data.csv')
# airline_data['FlightDate'] = pd.to_datetime(airline_data['FlightDate'])

# # Extrahiere die Monatsabkürzungen und ordne sie nach dem Kalendermonat
# airline_data['MonthShort'] = airline_data['FlightDate'].dt.strftime('%b')
# airline_data['MonthShort'] = pd.Categorical(airline_data['MonthShort'], categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ordered=True)

# # Create a dash application
# app = dash.Dash(__name__)

# # Define the layout of the dashboard
# app.layout = html.Div(className='main-container', children=[
#     # Header-Division
#     html.Div([
#         # Hauptüberschrift des Dashboards
#         html.H1('Dashboard zur Leistung der Fluggesellschaften', style={'textAlign': 'center', 'color': '#fff', 'font-size': '3em'}),
#         # Optionaler Absatz
#         html.P('''Willkommen zum Dashboard zur Leistung der Fluggesellschaften! Dieses Dashboard bietet eine umfassende 
#                 Visualisierung der Leistungsdaten verschiedener Fluggesellschaften. Verfolgen Sie die Gesamtzahl der Flüge,
#                 durchschnittliche Ankunftsverzögerungen, Entfernungen und Abflugzeiten, um Einblicke in die Leistung der 
#                 Fluggesellschaften zu erhalten. Mit interaktiven Filtern können Sie den gewünschten Zeitraum auswählen 
#                 und die Daten genau nach Ihren Bedürfnissen analysieren. Tauchen Sie ein und entdecken Sie die Muster und 
#                 Trends im Luftverkehr''',
#                 style={'textAlign': 'left', 'color': '#fff', 'font-size': '1.2em', 'font-family':'arial'})
#     ], style={'backgroundColor': 'rgba(48, 0, 38, 0.88)', 'padding': '20px'}),

#     # Body-Division
#     html.Div([
#         # Filter-Division (links, 20% der Breite)
#         html.Div([
#             html.Label("Datum auswählen:", style={'font-weight': 'bold', 'font-size': '1.2em',
#             'color':'#fff', 'font-family':'Times new Roman'}),
#             dcc.DatePickerRange(
#                 id='input-date-range',
#                 min_date_allowed=airline_data['FlightDate'].min(),
#                 max_date_allowed=airline_data['FlightDate'].max(),
#                 initial_visible_month=airline_data['FlightDate'].max(),
#                 start_date=airline_data['FlightDate'].min(),
#                 end_date=airline_data['FlightDate'].max(),
#                 display_format='DD.MM.YYYY'  # Europäisches Datumsformat
#             )
            
#         ], style={'width':'10%', 'float': 'left', 'padding': '20px'}),

#         # Dashboard-Grid (rechts, restliche Breite)
#         html.Div([
#             # Grid-Layout für die Diagramme
#             html.Div([
#                 # Erstes Diagramm: Balkendiagramm und KPI für Gesamtflüge (neu)
#                 html.Div([
#                     dcc.Graph(id='bar-plot', style={'width': '80%', 'display': 'inline-block', 'marginRight': '5px'}),  # Lücke hinzugefügt
#                     html.Div([
#                         html.Div([
#                             html.H2(id='total-flights-kpi', style={'textAlign': 'center', 'color': '#fff'}),
#                             html.P('Gesamtflüge', style={'textAlign': 'center', 'color': '#fff'})
#                         ], style={'backgroundColor': 'rgba(48, 0, 38, 0.88)', 'padding': '20px'})
#                     ], style={'width': '18%', 'display': 'inline-block', 'verticalAlign': 'top'}),
                    
#                 ], style={'width': '100%', 'display': 'inline-block'}),
                
#             ]),
#             # Zweite Zeile im Raster
#             html.Div([
#                 # Drittes Diagramm: Streudiagramm
#                 html.Div(dcc.Graph(id='scatter-plot'), style={'width': '33%', 'display': 'inline-block'}),
#                 html.Div(style={'width': '2px', 'height': '2px', 'display': 'inline-block'}),  # Horizontales Lüchchen

#                 # Viertes Diagramm: Zweites Balkendiagramm
#                 html.Div(dcc.Graph(id='bar2-plot'), style={'width': '33%', 'display': 'inline-block'}),
#                 html.Div(style={'width': '2px', 'height': '2px', 'display': 'inline-block'}),  # Horizontales Lüchchen

#                 # Zweites Diagramm: Liniendiagramm
#                 html.Div(dcc.Graph(id='line-plot'), style={'width': '33%', 'display': 'inline-block'}),
#             ]),
#         ], style={'width':'90%', 'float': 'right', 'padding': '20px', 'backgroundColor': 'rgba(48, 0, 38, 0.5)', 'display': 'flex', 'flex-direction': 'column'})  # vertikale Ausrichtung als Spaltenlayout

#     ], style={'display': 'flex', 'flex-direction': 'row', 'backgroundColor': 'rgba(48, 0, 38, 0.5)'}),

#     # Footer-Division (5% der Höhe)
#     html.Div([
#         html.Footer([
#             html.P('\u00A9  2024 Solaiman Karroumi. Alle Rechte vorbehalten.', 
#                    style={'textAlign': 'center', 'color': '#000', 'font-size': '1.2em', 'background':'#ccff00c4','margin':'0'})
#         ], style={'padding': '0px'})
#     ], style={'height': '2%'})
# ], style={'display': 'flex', 'flex-direction': 'column', 'min-height': '100vh', 'margin':'0', 'padding':'0'})

# # Callbacks für die Diagramme und KPI
# @app.callback(
#     Output(component_id='input-date-range', component_property='end_date'),
#     [Input(component_id='input-date-range', component_property='start_date')]
# )
# def update_end_date(start_date):
#     # Überprüfe, ob das Startdatum größer als das aktuelle Enddatum ist
#     if start_date is not None:
#         current_end_date = airline_data['FlightDate'].max()
#         start_date = pd.to_datetime(start_date)
#         if start_date > current_end_date:
#             return current_end_date  # Setze das Enddatum auf das maximale Datum in den Daten
#     return None  # Lasse das Enddatum unverändert

# @app.callback(Output(component_id='bar-plot', component_property='figure'), 
#               Output(component_id='line-plot', component_property='figure'),
#               Output(component_id='scatter-plot', component_property='figure'),
#               Output(component_id='bar2-plot', component_property='figure'),
#               Output(component_id='total-flights-kpi', component_property='children'),
#               Input(component_id='input-date-range', component_property='start_date'),
#               Input(component_id='input-date-range', component_property='end_date'))
# def update_plots(start_date, end_date):
#     # Filtern der Daten nach dem ausgewählten Zeitraum
#     filtered_data = airline_data[(airline_data['FlightDate'] >= start_date) & (airline_data['FlightDate'] <= end_date)]

#     # Balkendiagramm
#     bar_data = filtered_data.groupby('Reporting_Airline')['Flights'].sum().reset_index()
#     bar_fig = px.bar(bar_data, x='Reporting_Airline', y='Flights', 
#                      title='Flugleistung nach Flügen', 
#                      labels={'Reporting_Airline': 'Fluggesellschaft', 'Flights': 'Total Flüge'},
#                      color='Reporting_Airline')
#     bar_fig.update_layout(xaxis_tickangle=35, plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)',font_color='#fff',)  

#     # Liniendiagramm
#     line_data = filtered_data.groupby('MonthShort')['ArrDelay'].mean().reset_index()
#     line_fig = px.line(line_data, x='MonthShort', y='ArrDelay', 
#                        title='Durchschnittliche Ankunftsverzögerung <br>nach Monat', 
#                        labels={'Month': 'Monat', 'ArrDelay': 'Durchschnittliche Ankunftsverzögerung'},
#                        template='plotly_white', color_discrete_sequence=['yellow'])
#     line_fig.update_layout(xaxis_tickangle=35, plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)', font_color='#fff')

#     # Streudiagramm
#     scatter_fig = px.scatter(filtered_data, x='Distance', y='DepTime', 
#                               title='Entfernung vs. Abflugzeit', 
#                               labels={'Distance': 'Abstand', 'DepTime': 'Abflugzeit'},
#                               template='plotly_white', color_discrete_sequence=['lightgreen'])
#     scatter_fig.update_layout(plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)', font_color='#fff')
    
#     # Zweites Balkendiagramm
#     state_counts = filtered_data['DestStateName'].value_counts()
#     top_10_DestStats = pd.DataFrame(state_counts.sort_values(ascending=False).head(10))
#     bar2_fig = px.bar(x=top_10_DestStats.index, y=top_10_DestStats['count'], 
#                       title='Häufigkeit der Top 10 Zielstaaten',
#                       labels={'x': 'Zielstaat', 'y': 'Häufigkeit'}, 
#                       template='plotly_white', color_discrete_sequence=['red'])
#     bar2_fig.update_layout(plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)', font_color='#fff', xaxis_tickangle=35) 
    
#     # KPI für Gesamtflüge
#     total_flights = filtered_data['Flights'].sum()
#     total_flights_kpi = f'{total_flights}'
    
#     return bar_fig, line_fig, scatter_fig, bar2_fig, total_flights_kpi

# # Run the application
# if __name__ == '__main__':
#     app.run_server(debug=True)







# # Import erforderlicher Bibliotheken
# import pandas as pd
# import plotly.graph_objects as go
# import plotly.express as px
# import dash
# from dash import dcc
# from dash import html
# from dash.dependencies import Input, Output, State

# # Daten importieren
# try:
#     airline_data = pd.read_csv('airline_data.csv')
#     airline_data['FlightDate'] = pd.to_datetime(airline_data['FlightDate'])

#     # Extrahiere die Monatsabkürzungen und ordne sie nach dem Kalendermonat
#     airline_data['MonthShort'] = airline_data['FlightDate'].dt.strftime('%b')
#     airline_data['MonthShort'] = pd.Categorical(airline_data['MonthShort'], categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ordered=True)
# except Exception as e:
#     print("Fehler beim Laden der Daten:", e)

# # Create a dash application
# app = dash.Dash(__name__)

# # Define the layout of the dashboard
# app.layout = html.Div(className='main-container', children=[
#     # Header-Division
#     html.Div([
#         # Hauptüberschrift des Dashboards
#         html.H1('Dashboard zur Leistung der Fluggesellschaften', style={'textAlign': 'center', 'color': '#fff', 'font-size': '3em'}),
#         # Optionaler Absatz
#         html.P('''Willkommen zum Dashboard zur Leistung der Fluggesellschaften! Dieses Dashboard bietet eine umfassende 
#                 Visualisierung der Leistungsdaten verschiedener Fluggesellschaften. Verfolgen Sie die Gesamtzahl der Flüge,
#                 durchschnittliche Ankunftsverzögerungen, Entfernungen und Abflugzeiten, um Einblicke in die Leistung der 
#                 Fluggesellschaften zu erhalten. Mit interaktiven Filtern können Sie den gewünschten Zeitraum auswählen 
#                 und die Daten genau nach Ihren Bedürfnissen analysieren. Tauchen Sie ein und entdecken Sie die Muster und 
#                 Trends im Luftverkehr''',
#                 style={'textAlign': 'left', 'color': '#fff', 'font-size': '1.2em', 'font-family':'arial'})
#     ], style={'backgroundColor': 'rgba(48, 0, 38, 0.88)', 'padding': '20px'}),

#     # Body-Division
#     html.Div([
#         # Filter-Division (links, 20% der Breite)
#         html.Div([
#             html.Label("Datum auswählen:", style={'font-weight': 'bold', 'font-size': '1.2em',
#             'color':'#fff', 'font-family':'Times new Roman'}),
#             dcc.DatePickerRange(
#                 id='input-date-range',
#                 min_date_allowed=airline_data['FlightDate'].min(),
#                 max_date_allowed=airline_data['FlightDate'].max(),
#                 initial_visible_month=airline_data['FlightDate'].max(),
#                 start_date=airline_data['FlightDate'].min(),
#                 end_date=airline_data['FlightDate'].max(),
#                 display_format='DD.MM.YYYY'  # Europäisches Datumsformat
#             )
            
#         ], style={'width':'10%', 'float': 'left', 'padding': '20px'}),

#         # Dashboard-Grid (rechts, restliche Breite)
#         html.Div([
#             # Grid-Layout für die Diagramme
#             html.Div([
#                 # Erstes Diagramm: Balkendiagramm und KPI für Gesamtflüge (neu)
#                 html.Div([
#                     dcc.Graph(id='bar-plot', style={'width': '80%', 'display': 'inline-block', 'marginRight': '5px'}),  # Lücke hinzugefügt
#                     html.Div([
#                         html.Div([
#                             html.H2(id='total-flights-kpi', style={'textAlign': 'center', 'color': '#fff'}),
#                             html.P('Gesamtflüge', style={'textAlign': 'center', 'color': '#fff'})
#                         ], style={'backgroundColor': 'rgba(48, 0, 38, 0.88)', 'padding': '20px'})
#                     ], style={'width': '18%', 'display': 'inline-block', 'verticalAlign': 'top'}),
                    
#                 ], style={'width': '100%', 'display': 'inline-block'}),
                
#             ]),
#             # Zweite Zeile im Raster
#             html.Div([
#                 # Drittes Diagramm: Streudiagramm
#                 html.Div(dcc.Graph(id='scatter-plot'), style={'width': '33%', 'display': 'inline-block'}),
#                 html.Div(style={'width': '2px', 'height': '2px', 'display': 'inline-block'}),  # Horizontales Lüchchen

#                 # Viertes Diagramm: Zweites Balkendiagramm
#                 html.Div(dcc.Graph(id='bar2-plot'), style={'width': '33%', 'display': 'inline-block'}),
#                 html.Div(style={'width': '2px', 'height': '2px', 'display': 'inline-block'}),  # Horizontales Lüchchen

#                 # Zweites Diagramm: Liniendiagramm
#                 html.Div(dcc.Graph(id='line-plot'), style={'width': '33%', 'display': 'inline-block'}),
#             ]),
#         ], style={'width':'90%', 'float': 'right', 'padding': '20px', 'backgroundColor': 'rgba(48, 0, 38, 0.5)', 'display': 'flex', 'flex-direction': 'column'})  # vertikale Ausrichtung als Spaltenlayout

#     ], style={'display': 'flex', 'flex-direction': 'row', 'backgroundColor': 'rgba(48, 0, 38, 0.5)'}),

#     # Footer-Division (5% der Höhe)
#     html.Div([
#         html.Footer([
#             html.P('\u00A9  2024 Solaiman Karroumi. Alle Rechte vorbehalten.', 
#                    style={'textAlign': 'center', 'color': '#000', 'font-size': '1.2em', 'background':'#ccff00c4','margin':'0'})
#         ], style={'padding': '0px'})
#     ], style={'height': '2%'})
# ], style={'display': 'flex', 'flex-direction': 'column', 'min-height': '100vh', 'margin':'0', 'padding':'0'})

# # Callbacks für die Diagramme und KPI
# @app.callback(
#     Output(component_id='input-date-range', component_property='end_date'),
#     [Input(component_id='input-date-range', component_property='start_date')]
# )
# def update_end_date(start_date):
#     try:
#         # Überprüfe, ob das Startdatum größer als das aktuelle Enddatum ist
#         if start_date is not None:
#             current_end_date = airline_data['FlightDate'].max()
#             start_date = pd.to_datetime(start_date)
#             if start_date > current_end_date:
#                 return current_end_date  # Setze das Enddatum auf das maximale Datum in den Daten
#         return None  # Lasse das Enddatum unverändert
#     except Exception as e:
#         print("Fehler beim Aktualisieren des Enddatums:", e)
#         return None

# @app.callback(Output(component_id='bar-plot', component_property='figure'), 
#               Output(component_id='line-plot', component_property='figure'),
#               Output(component_id='scatter-plot', component_property='figure'),
#               Output(component_id='bar2-plot', component_property='figure'),
#               Output(component_id='total-flights-kpi', component_property='children'),
#               Input(component_id='input-date-range', component_property='start_date'),
#               Input(component_id='input-date-range', component_property='end_date'))
# def update_plots(start_date, end_date):
#     try:
#         # Filtern der Daten nach dem ausgewählten Zeitraum
#         filtered_data = airline_data[(airline_data['FlightDate'] >= start_date) & (airline_data['FlightDate'] <= end_date)]

#         # Balkendiagramm
#         bar_data = filtered_data.groupby('Reporting_Airline')['Flights'].sum().reset_index()
#         bar_fig = px.bar(bar_data, x='Reporting_Airline', y='Flights', 
#                          title='Flugleistung nach Flügen', 
#                          labels={'Reporting_Airline': 'Fluggesellschaft', 'Flights': 'Total Flüge'},
#                          color='Reporting_Airline')
#         bar_fig.update_layout(xaxis_tickangle=35, plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)',font_color='#fff',)  

#         # Liniendiagramm
#         line_data = filtered_data.groupby('MonthShort')['ArrDelay'].mean().reset_index()
#         line_fig = px.line(line_data, x='MonthShort', y='ArrDelay', 
#                            title='Durchschnittliche Ankunftsverzögerung <br>nach Monat', 
#                            labels={'Month': 'Monat', 'ArrDelay': 'Durchschnittliche Ankunftsverzögerung'},
#                            template='plotly_white', color_discrete_sequence=['yellow'])
#         line_fig.update_layout(xaxis_tickangle=35, plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)', font_color='#fff')

#         # Streudiagramm
#         scatter_fig = px.scatter(filtered_data, x='Distance', y='DepTime', 
#                                   title='Entfernung vs. Abflugzeit', 
#                                   labels={'Distance': 'Abstand', 'DepTime': 'Abflugzeit'},
#                                   template='plotly_white', color_discrete_sequence=['lightgreen'])
#         scatter_fig.update_layout(plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)', font_color='#fff')

#         # Zweites Balkendiagramm
#         state_counts = filtered_data['DestStateName'].value_counts()
#         top_10_DestStats = pd.DataFrame(state_counts.sort_values(ascending=False).head(10))
#         bar2_fig = px.bar(x=top_10_DestStats.index, y=top_10_DestStats['count'], 
#                           title='Häufigkeit der Top 10 Zielstaaten',
#                           labels={'x': 'Zielstaat', 'y': 'Häufigkeit'}, 
#                           template='plotly_white', color_discrete_sequence=['red'])
#         bar2_fig.update_layout(plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)', font_color='#fff', xaxis_tickangle=35) 

#         # KPI für Gesamtflüge
#         total_flights = filtered_data['Flights'].sum()
#         total_flights_kpi = f'{total_flights}'

#         return bar_fig, line_fig, scatter_fig, bar2_fig, total_flights_kpi
#     except Exception as e:
#         print("Fehler beim Aktualisieren der Diagramme und KPI:", e)
#         return {}, {}, {}, {}, ''

# # Run the application
# if __name__ == '__main__':
#     app.run_server(debug=True)






import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Daten importieren
try:
    df = pd.read_csv('airline_data.csv')
    airline_data = df.loc[(df['Year'] >= 2018) & (df['Year'] <= 2020)].copy()  # Hier wird eine Kopie des DataFrame erstellt
    airline_data['FlightDate'] = pd.to_datetime(airline_data['FlightDate'])
    airline_data['MonthShort'] = airline_data['FlightDate'].dt.strftime('%b')
    airline_data['MonthShort'] = pd.Categorical(airline_data['MonthShort'], categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ordered=True)
except Exception as e:
    print("Fehler beim Laden der Daten:", e)

# Create a dash application
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(className='main-container', children=[
    # Header-Division
    html.Div([
        html.H1('Dashboard zur Leistung der Fluggesellschaften', style={'textAlign': 'center', 'color': '#fff', 'fontSize': '3em'}),
        html.P('''Willkommen zum Dashboard zur Leistung der Fluggesellschaften! Dieses Dashboard bietet eine umfassende 
                Visualisierung der Leistungsdaten verschiedener Fluggesellschaften. Verfolgen Sie die Gesamtzahl der Flüge,
                durchschnittliche Ankunftsverzögerungen, Entfernungen und Abflugzeiten, um Einblicke in die Leistung der 
                Fluggesellschaften zu erhalten. Mit interaktiven Filtern können Sie den gewünschten Zeitraum auswählen 
                und die Daten genau nach Ihren Bedürfnissen analysieren. Tauchen Sie ein und entdecken Sie die Muster und 
                Trends im Luftverkehr''',
                style={'textAlign': 'left', 'color': '#fff', 'fontSize': '1.2em', 'fontFamily':'arial'})
    ], style={'backgroundColor': 'rgba(48, 0, 38, 0.88)', 'padding': '20px'}),

    # Body-Division
    html.Div([
        # Filter-Division (links, 20% der Breite)
        html.Div([
            html.Label("Datum auswählen:", style={'fontWeight': 'bold', 'fontSize': '1.2em',
            'color':'#fff', 'fontFamily':'Times new Roman'}),
            dcc.DatePickerRange(
                id='input-date-range',
                min_date_allowed=airline_data['FlightDate'].min(),
                max_date_allowed=airline_data['FlightDate'].max(),
                initial_visible_month=airline_data['FlightDate'].max(),
                start_date=airline_data['FlightDate'].min(),
                end_date=airline_data['FlightDate'].max(),
                display_format='DD.MM.YYYY'  # Europäisches Datumsformat
            )
        ], style={'width':'10%', 'float': 'left', 'padding': '20px'}),

        # Dashboard-Grid (rechts, restliche Breite)
        html.Div([
            # Grid-Layout für die Diagramme
            html.Div([
                # Erstes Diagramm: Balkendiagramm und KPI für Gesamtflüge (neu)
                html.Div([
                    dcc.Graph(id='bar-plot', style={'width': '80%', 'display': 'inline-block', 'marginRight': '5px'}),
                    html.Div([
                        html.Div([
                            html.H2(id='total-flights-kpi', style={'textAlign': 'center', 'color': '#fff'}),
                            html.P('Gesamtflüge', style={'textAlign': 'center', 'color': '#fff'})
                        ], style={'backgroundColor': 'rgba(48, 0, 38, 0.88)', 'padding': '20px'})
                    ], style={'width': '18%', 'display': 'inline-block', 'verticalAlign': 'top'}),
                ], style={'width': '100%', 'display': 'inline-block'}),
            ]),
            # Zweite Zeile im Raster
            html.Div([
                # Drittes Diagramm: Streudiagramm
                html.Div(dcc.Graph(id='scatter-plot'), style={'width': '33%', 'display': 'inline-block'}),
                html.Div(style={'width': '2px', 'height': '2px', 'display': 'inline-block'}),  # Horizontales Lüchchen

                # Viertes Diagramm: Zweites Balkendiagramm
                html.Div(dcc.Graph(id='bar2-plot'), style={'width': '33%', 'display': 'inline-block'}),
                html.Div(style={'width': '2px', 'height': '2px', 'display': 'inline-block'}),  # Horizontales Lüchchen

                # Zweites Diagramm: Liniendiagramm
                html.Div(dcc.Graph(id='line-plot'), style={'width': '33%', 'display': 'inline-block'}),
            ]),
        ], style={'width':'90%', 'float': 'right', 'padding': '20px', 'backgroundColor': 'rgba(48, 0, 38, 0.5)', 'display': 'flex', 'flexDirection': 'column'})  # vertikale Ausrichtung als Spaltenlayout

    ], style={'display': 'flex', 'flexDirection': 'row', 'backgroundColor': 'rgba(48, 0, 38, 0.5)'}),

    # Footer-Division (5% der Höhe)
    html.Div([
        html.Footer([
            html.P('\u00A9  2024 Solaiman Karroumi. Alle Rechte vorbehalten.', 
                   style={'textAlign': 'center', 'color': '#fff', 'fontFamily':'Arial'})
        ], style={'padding': '10px'})
    ], style={'backgroundColor': 'rgba(48, 0, 38, 0.88)', 'height': '5vh', 'padding': '20px'})
], style={'backgroundColor': '#1E1E1E'})

# Callbacks zur Aktualisierung der Diagramme basierend auf den ausgewählten Datumsbereich
@app.callback(
    [Output('bar-plot', 'figure'),
     Output('line-plot', 'figure'),
     Output('scatter-plot', 'figure'),
     Output('bar2-plot', 'figure'),
     Output('total-flights-kpi', 'children')],
    [Input('input-date-range', 'start_date'),
     Input('input-date-range', 'end_date')]
)
def update_plots(start_date, end_date):
    try:
        if start_date is None or end_date is None:
            return {}, {}, {}, {}, "Start- und Enddatum müssen ausgewählt werden."

        # Kopie des gefilterten DataFrame erstellen
        filtered_data = airline_data[(airline_data['FlightDate'] >= start_date) & (airline_data['FlightDate'] <= end_date)].copy()

        bar_data = filtered_data.groupby('Reporting_Airline')['Flights'].sum().reset_index()
        bar_fig = px.bar(bar_data, x='Reporting_Airline', y='Flights', 
                         title='Flugleistung nach Flügen', 
                         labels={'Reporting_Airline': 'Fluggesellschaft', 'Flights': 'Total Flüge'},
                         color='Reporting_Airline')
        bar_fig.update_layout(xaxis_tickangle=35, plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)',font_color='#fff',)  

        line_data = filtered_data.groupby('MonthShort')['ArrDelay'].mean().reset_index()
        line_fig = px.line(line_data, x='MonthShort', y='ArrDelay', 
                           title='Durchschnittliche Ankunftsverzögerung <br>nach Monat', 
                           labels={'Month': 'Monat', 'ArrDelay': 'Durchschnittliche Ankunftsverzögerung'},
                           template='plotly_white', color_discrete_sequence=['yellow'])
        line_fig.update_layout(xaxis_tickangle=35, plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)', font_color='#fff')

        scatter_fig = px.scatter(filtered_data, x='Distance', y='DepTime', 
                                  title='Entfernung vs. Abflugzeit', 
                                  labels={'Distance': 'Abstand', 'DepTime': 'Abflugzeit'},
                                  template='plotly_white', color_discrete_sequence=['lightgreen'])
        scatter_fig.update_layout(plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)', font_color='#fff')

        state_counts = filtered_data['DestStateName'].value_counts()
        top_10_DestStats = pd.DataFrame(state_counts.sort_values(ascending=False).head(10))
        bar2_fig = px.bar(x=top_10_DestStats.index, y=top_10_DestStats['count'], 
                          title='Häufigkeit der Top 10 Zielstaaten',
                          labels={'x': 'Zielstaat', 'y': 'Häufigkeit'}, 
                          template='plotly_white', color_discrete_sequence=['red'])
        bar2_fig.update_layout(plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)', font_color='#fff', xaxis_tickangle=35) 

        total_flights = filtered_data['Flights'].sum()
        total_flights_kpi = f'{total_flights}'

        return bar_fig, line_fig, scatter_fig, bar2_fig, total_flights_kpi
    except Exception as e:
        print("Fehler beim Aktualisieren der Diagramme und KPI:", e)
        return {}, {}, {}, {}, ''

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
