import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Value": [10, 20, 15, 8]
})

# Create a bar chart
fig = px.bar(df, x="Category", y="Value", title="Sample Bar Chart")

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Sample Dashboard'),
    html.Div(children='''This is a simple dashboard powered by Dash.'''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

