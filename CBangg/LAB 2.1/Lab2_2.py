# Import necessary libraries
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Step 1: Data Preparation and Import
# Load the dataset
df = pd.read_csv("LAB 2.1/sales_data.csv")

# Step 2: Designing Interactive Visualizations
# Create a bar chart
bar_chart = px.bar(df, x="Product", y="Amount", title="Total Sales by Product")

# Create a line chart
line_chart = px.line(df, x="Date", y="Amount", title="Daily Sales")

# Create a scatter plot
scatter_plot = px.scatter(df, x="Date", y="Amount", title="Product Sales by Date")

# Step 3: Building an Interactive Dashboard
# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Interactive Sales Dashboard"),
    dcc.Graph(id="bar-chart", figure=bar_chart),
    dcc.Graph(id="line-chart", figure=line_chart),
    dcc.Graph(id="scatter-plot", figure=scatter_plot)
])

# Define interactivity
@app.callback(
    Output("bar-chart", "figure"),
    Output("line-chart", "figure"),
    Output("scatter-plot", "figure"),
    Input("bar-chart", "selectedData")
)
def update_charts(selected_data):
    # Add interactivity here, e.g., filtering based on selected data
    # You can use selected_data to filter and update the visualizations
    return updated_bar_chart, updated_line_chart, updated_scatter_plot

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
