from flask import Flask, render_template
import pandas as pd
import numpy as np  # not explicitly used in this code
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

df = pd.read_csv('data/MTA_Subway_Terminal_On-Time_Performance__2015-2019.csv')
df['date'] = pd.to_datetime(df['month'], format='%Y-%m')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month


@app.route('/')
def dashboard():
    return render_template('home.html')

@app.route('/data-overview')
def data_overview():
    
    total_records = len(df)
    start_year = df['year'].min()
    end_year = df['year'].max()
    
    return render_template('data_overview.html', total_records=total_records, start_year=start_year, end_year=end_year) 

if __name__ == '__main__':
    app.run(debug=True)