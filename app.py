import dash
from dash import html, dcc
import dash_daq as daq
from dash.dependencies import Input, Output
import spacy
import os

# Initialize the Dash app
app = dash.Dash(__name__)

# Load the Spacy model
nlp = spacy.load("en_core_web_sm")

# Get all book files in the data directory
all_books = [b for b in os.scandir('books') if b.name.endswith('.pdf')]

# Sort dir entries by name
all_books.sort(key=lambda x: x.name)

# Tell Dash to use the external CSS file
app.css.append_css({"external_url": "style.css"})

# Define the layout
app.layout = html.Div(
    id = "body",
    className="body night-body",
    children=[
        # Header
        html.Header(
            id="header",
            className='header',
            children=[
                html.H1("The hunger games network"),
                html.Div(
                    className="toggle-container",
                    children=[
                        daq.ToggleSwitch(
                            id='theme-toggle',
                            label=[
                                html.Img(src="sun.svg", style={'height': '20px', 'width': '20px'}),
                                html.Img(src="moon.svg", style={'height': '20px', 'width': '20px'})
                            ],
                            value=True
                        )
                    ]
                )
            ]
        ),

        # Two Columns
        html.Div(
            className="columns-container",
            children=[
                html.Div(
                    className="column column-left",
                    style={'width': '35%'},
                    children=[
                        # Left column content
                        # html.H2("Left Column"),
                        html.Div(
                            className="dropdown",
                            children = [
                                dcc.Dropdown(
                                id="book-checklist",
                                options=[{"label": book.name, "value": book.path} for book in all_books],
                                value=[],
                                placeholder = "Select one or more books to analyze",
                                multi=True
                            ),
                            ]
                            
                        ),
                        html.Div(
                            children=[
                                html.Button(id='process-button', className='button', style={'vertical-align': 'middle'}, children=[
                                    html.Span('Process selected books')
                                ])
                            ]
                        ),
                        
                        # Space for explanation
                        html.Div(
                            className="explanation",
                            children=[
                                html.H2("About"),
                                html.P("This is a project that uses web scraping and natural language processing to analyze the relationship between the characters in The Hunger Games book series."),
                                html.P(["This project was inspired by the ", html.A("Thu-vu92 The witcher network", href="https://github.com/thu-vu92/the_witcher_network"), " repo."]),
                                html.P("This analysis has two main goals:"),
                                html.Ul(
                                    children=[
                                        html.Li("Investigate the characters in The Hunger Games book series regarding:"),
                                        html.Ul(
                                            children=[
                                                html.Li("Importance"),
                                                html.Li("Evolution")
                                            ]
                                        ),
                                        html.Li("Investigate the communities in The Hunger Games book series.")
                                    ]
                                )
                            ]
                        )
                        
                    ]
                    
                ),
                
                html.Div(
                    className="column",
                    style={'width': '65%'},
                    children=[
                        # Right column content
                        html.H2("Right Column"),
                        html.Div(id="output-container"),
                        # ...
                    ]
                )
            ]
        ),

        
    ]
)

@app.callback(
    Output('body', 'className'),
    [Input('theme-toggle', 'value')]
)
def update_header_class(theme):
    if theme:
        return 'body night-body'
    else:
        return 'body day-body'


@app.callback(
    Output("output-container", "children"),
    [Input("process-button", "n_clicks")],
    [dash.dependencies.State("book-checklist", "value")]
)
def process_books(n_clicks, selected_books):
    if n_clicks == 0 or not selected_books:
        return html.Div()


    return html.Div([
        html.H3("Analysis Results"),
        # Display other analysis results here
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
