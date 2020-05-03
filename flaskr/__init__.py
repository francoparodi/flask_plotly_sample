from flask import Flask, render_template

import plotly
import plotly.graph_objs as go

import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def index():
    bar = create_plot()
    return render_template('index.html', plot=bar)

def create_plot():

    x = [0, 1, 2, 3, 4, 5]
    y = [10, 11, 12, 9, 10, 11]

    dataFrame = pd.DataFrame({'x': x, 'y': y})
    data = [
        go.Bar(
            x = dataFrame['x'], 
            y = dataFrame['y']
        )
    ]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

if __name__ == '__main__':
    app.run()