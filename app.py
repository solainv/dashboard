# Import erforderlicher Bibliotheken
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Daten importieren und vorbereiten
def prepare_data():
    try:
        # Daten laden
        df = pd.read_csv('airline_data.csv')
        
        # Datenbereinigung und -vorbereitung
        airline_data = df.loc[(df['Year'] >= 2010) & (df['Year'] <= 2020)].copy()
        airline_data['FlightDate'] = pd.to_datetime(airline_data['FlightDate'])
        airline_data['MonthShort'] = airline_data['FlightDate'].dt.strftime('%b')
        airline_data['MonthShort'] = pd.Categorical(airline_data['MonthShort'], categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ordered=True)
        airline_data['DepTime'] = pd.to_datetime(airline_data['DepTime'], format='%H%M', errors='coerce').dt.strftime('%H:%M')
        airline_data['DepTime_seconds'] = pd.to_datetime(airline_data['DepTime'], format='%H:%M').dt.hour * 3600 + pd.to_datetime(airline_data['DepTime'], format='%H:%M').dt.minute * 60
        airline_data = airline_data.sort_values(by='DepTime_seconds')


        
        return airline_data
    except Exception as e:
        print("Fehler beim Laden der Daten:", e)
        return None

# Dash-Anwendung erstellen
app = dash.Dash(__name__)
server = app.server

# Daten vorbereiten
airline_data = prepare_data()

# Standard Start- und Enddaten setzen
default_start_date = airline_data['FlightDate'].min()
default_end_date = airline_data['FlightDate'].max()

# Layout der Anwendung definieren
app.layout = html.Div(className='main-container', children=[
    # Header-Division
    html.Div([
        # Hauptüberschrift des Dashboards
        html.H1('Dashboard zur Leistung der Fluggesellschaften', style={'textAlign': 'center', 'color': '#fff', 'font-size': '3em'}),
        # Optionaler Absatz
        html.P('''Willkommen zum Dashboard zur Leistung der Fluggesellschaften! Dieses Dashboard bietet eine umfassende 
                Visualisierung der Leistungsdaten verschiedener Fluggesellschaften. Verfolgen Sie die Gesamtzahl der Flüge,
                durchschnittliche Ankunftsverzögerungen, Entfernungen und Abflugzeiten, um Einblicke in die Leistung der 
                Fluggesellschaften zu erhalten. Mit interaktiven Filtern können Sie den gewünschten Zeitraum auswählen 
                und die Daten genau nach Ihren Bedürfnissen analysieren. Tauchen Sie ein und entdecken Sie die Muster und 
                Trends im Luftverkehr''',
                style={'textAlign': 'left', 'color': '#fff', 'font-size': '1.2em', 'font-family':'arial'})
    ], style={'backgroundColor': 'rgba(48, 0, 38, 0.88)', 'padding': '20px'}),

    # Body-Division
    html.Div([
        # Filter-Division (links, 20% der Breite)
        html.Div([
            html.Label("Filtern nach Datum:", style={'font-size': '1.2em', 'color':'#ff0', 'font-family':'sans-serif'}),
            dcc.DatePickerRange(
                id='input-date-range',
                min_date_allowed=default_start_date,
                max_date_allowed=default_end_date,
                initial_visible_month=default_end_date,
                start_date=default_start_date,
                end_date=default_end_date,
                display_format='DD.MM.YYYY'  # Europäisches Datumsformat
            ),
            html.Label("Fluggesellschaften auswählen:", style={'font-size': '1.2em', 'color':'#ff0', 'font-family':'sans-serif'}),
            dcc.Dropdown(
                id='airline-dropdown',
                options=[{'label': i, 'value': i} for i in airline_data['Reporting_Airline'].unique()],
                value=airline_data['Reporting_Airline'].unique(),
                multi=True,
            )
        ], style={'width':'22%', 'float': 'left', 'padding': '20px'}),

        # Dashboard-Grid (rechts, restliche Breite)
        html.Div([
            # Grid-Layout für die Diagramme
            html.Div(
                [
              # Erste Zeile im Raster:  
                html.Div(
                    [
                    # Balkendiagramm
                    dcc.Graph(id='bar-plot', style={'width': '70%', 'display': 'inline-block', 'marginRight': '2px', 'marginLeft': '0'}),  # Angepasste Breite und Abstände
                    # KPIs für Gesamtflüge
                    html.Div([
                        # KPI für Gesamtflüge
                        html.Div([
                            html.H2(id='total-flights-kpi', style={'textAlign': 'center', 'color': '#fff', 'fontSize':'32px'}),
                            html.P('Total Flüge', style={'textAlign': 'center', 'color': '#fff'})
                        ], style={'backgroundColor': 'rgba(48, 0, 38, 0.88)', 'padding': '20px'}),
                        html.Div(style={'width': '100%', 'height': '2px', 'margin': '2px 0', 'background-color': 'transparent'}),  # Vertikales Lückchen mit 2 Pixeln Höhe und 10 Pixeln oberem und unterem Abstand
                        # KPI für Gesamtverzögerung
                        html.Div([
                            html.H2(id='arr-delay-kpi', style={'textAlign': 'center', 'color': '#fff', 'fontSize':'32px'}),
                            html.P('Total Verzögerung (min)', style={'textAlign': 'center', 'color': '#fff'})
                        ], style={'backgroundColor': 'rgba(48, 0, 38, 0.88)', 'padding': '20px'})
                    ], style={'width': '29%', 'display': 'inline-block', 'verticalAlign': 'top'}),


                        
                    ], style={'width': '100%', 'display': 'inline-block'}
                    
                        ),
                        
                ]
                    ),
            # Zweite Zeile im Raster
            html.Div(
                [
                # Balkendiagramm Häufigkeit der Top 1 Zielstaaten
                html.Div(dcc.Graph(id='bar2-plot'), style={'width': '33%', 'display': 'inline-block'}),
                # Horizontales Lüchchen
                html.Div(style={'width': '2px', 'height': '2px', 'display': 'inline-block'}),  

                # Liniendiagramm
                html.Div(dcc.Graph(id='line-plot'), style={'width': '66%', 'display': 'inline-block'}),
                ]
                    ),
            # Dritte Zeile im Raster
            html.Div([
                # Streudiagramm
                html.Div(dcc.Graph(id='scatter-plot'), style={'width': '66%', 'display': 'inline-block'}),
                # Horizontales Lüchchen
                html.Div(style={'width': '2px', 'height': '2px', 'display': 'inline-block'}),  
                # pieplot
                html.Div(dcc.Graph(id='pie-plot'), style={'width': '33%', 'display': 'inline-block'}),
            ]),
             # vertikale Ausrichtung als Spaltenlayout
            ], style={'width':'80%', 'float': 'right', 'padding': '20px', 'backgroundColor': 'rgba(48, 0, 38, 0.5)', 'display': 'flex', 'flex-direction': 'column'}) 

    ], style={'display': 'flex', 'flex-direction': 'row', 'backgroundColor': 'rgba(48, 0, 38, 0.5)'}
    ),

    # Footer-Division (5% der Höhe)
    html.Div([
        html.Footer([
            html.P('\u00A9  2024 Solaiman Karroumi. Alle Rechte vorbehalten.', 
                   style={'textAlign': 'center', 'color': '#000', 'font-size': '1.2em', 'background':'#ccff00c4','margin':'0'})
        ], style={'padding': '0px'})
    ], style={'height': '2%'})
], 
# style für
style={'display': 'flex', 'flex-direction': 'column', 'min-height': '100vh', 'margin':'0', 'padding':'0'})

# Callbacks für die Diagramme und KPI
@app.callback(
    [Output('bar-plot', 'figure'),
     Output('line-plot', 'figure'),
     Output('scatter-plot', 'figure'),
     Output('bar2-plot', 'figure'),
     Output('total-flights-kpi', 'children'),
     Output('arr-delay-kpi', 'children'),
     Output('pie-plot', 'figure')],
    [Input('input-date-range', 'start_date'),
     Input('input-date-range', 'end_date'),
     Input('airline-dropdown', 'value')]
)
def update_plots(start_date, end_date, selected_airlines):
    try:
        if start_date is None or end_date is None:
            start_date = default_start_date
            end_date = default_end_date

        # Kopie des gefilterten DataFrame erstellen
        filtered_data = airline_data[(airline_data['FlightDate'] >= start_date) & (airline_data['FlightDate'] <= end_date)].copy()
        
        if selected_airlines:
            filtered_data = filtered_data[filtered_data['Reporting_Airline'].isin(selected_airlines)]
        # Diagramme
        
        # Balkendiagramm für Flugleistung
        bar_data = filtered_data.groupby('Reporting_Airline')['Flights'].sum().reset_index()
        bar_fig = px.bar(bar_data, x='Reporting_Airline', y='Flights', 
                         title='Flugleistung nach Flügen', 
                         labels={'Reporting_Airline': 'Fluggesellschaft', 'Flights': 'Total Flüge'},
                         color='Reporting_Airline')
        bar_fig.update_layout(xaxis_tickangle=35, plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)',font_color='#fff',)  

        # KPI Gesamtflüge
        total_flights = filtered_data['Flights'].sum()
        total_flights_kpi = f'{total_flights}'

        # Summe des Ankunftsverzugs (ArrDelay) berechnen
        sum_arr_delay = filtered_data['ArrDelay'].sum()

        # Bestimmung des Trends (Aufwärts-, Abwärts- oder Stagnation)
        trend_symbol = '🔺' if sum_arr_delay > 0 else ('🔻' if sum_arr_delay < 0 else '')

        # KPI Gesamtverzug
        arr_delay_kpi = f'{sum_arr_delay} {trend_symbol}'


        # Balkendiagramm für die Häufigkeit der Top 10 Zielstaaten
        state_counts = filtered_data['DestStateName'].value_counts()
        top_10_DestStats = pd.DataFrame(state_counts.sort_values(ascending=False).head(10))
        bar2_fig = px.bar(x=top_10_DestStats.index, y=top_10_DestStats['count'], 
                          title='Häufigkeit der Top 10 Zielstaaten',
                          labels={'x': 'Zielstaat', 'y': 'Häufigkeit'}, 
                          template='plotly_white', color_discrete_sequence=['red'])
        bar2_fig.update_layout(plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)',
                                font_color='#fff', xaxis_tickangle=45) 

        # Liniendiagramm für durchschnittliche Ankunftsverzögerung
        line_data = filtered_data.groupby('MonthShort')['ArrDelay'].mean().reset_index()
        line_data = filtered_data.groupby(['Year','Month','DayofMonth'])['ArrDelay'].mean().reset_index()
        # Fügen Sie eine neue Spalte 'Year_Month' hinzu, die die Kombination aus Jahr und Monat enthält
        line_data['Year_Month_day'] = line_data['Year'].astype(str) + '-' + line_data['Month'].astype(str).str.zfill(2)+ '-' + line_data['DayofMonth'].astype(str).str.zfill(2)
        # Plot mit Plotly Express
        line_fig = px.line(line_data, x='Year_Month_day', y='ArrDelay',
                title=' Durchschnittliche Ankunftsverzögerung über die Zeit',
                labels={'ArrDelay': ' Durchschnittliche Ankunftsverzögerung (min)', 'Year_Month_day': 'Jahr-Monat-Tag'},
                template='plotly_white', color_discrete_sequence=['yellow'])

        line_fig.update_layout(xaxis_tickangle=35, plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)', font_color='#fff')
        
        # Streudiagramm für Entfernung vs. Abflugzeit
        scatter_fig = px.scatter(filtered_data, x='Distance', y='DepTime', 
                                  title='Entfernung vs. Abflugzeit', 
                                  labels={'Distance': 'Abstand', 'DepTime': 'Abflugzeit'},
                                  template='plotly_white', color_discrete_sequence=['lightgreen'])
        scatter_fig.update_layout(plot_bgcolor='rgba(84, 83, 83, 0.62)', paper_bgcolor='rgba(48, 0, 38, 0.5)', font_color='#fff')

        #Pie Plot
        pie_plot_data = filtered_data.groupby('DistanceGroup')['Flights'].sum().reset_index()
        total = pie_plot_data['Flights'].sum()
        pie_plot_data['prozent'] = pie_plot_data['Flights'].apply(lambda x: (x/total)*100)
        pie_fig = px.pie(values=pie_plot_data['prozent'], names = pie_plot_data['DistanceGroup'],
                         title='Prozentsatz der Flüge nach <br>Distanzgruppe')
        pie_fig.update_layout(
        plot_bgcolor='rgba(84, 83, 83, 0.62)',
        paper_bgcolor='rgba(48, 0, 38, 0.5)',
        font_color='#fff',
        legend=dict(
            orientation="v",  # Legende vertikal ausrichten
            y=-0,  # Vertikaler Abstand zwischen Titel und Legende anpassen
            xanchor="left",  # Legende am linken Rand der Grafikfläche ausrichten
            x=-0.4,  # Horizontaler Abstand zwischen Legende und Diagramm anpassen
            bgcolor='rgba(0,0,0,0)',  # Hintergrund der Legende transparent machen
            title="Distanzgruppe",  # Legendentitel
            title_font=dict(size=14),  # Schriftgröße des Legendentitels anpassen
                    )
                            )
        return bar_fig, line_fig, scatter_fig, bar2_fig, total_flights_kpi,arr_delay_kpi, pie_fig
    except Exception as e:
        print("Fehler beim Aktualisieren der Diagramme und KPI:", e)
        return {}, '', {}, {}, {}, {}, {}

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)

