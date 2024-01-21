from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load data from Excel file into a DataFrame
data_path = 'Dataset Task 1.xlsx'
df = pd.read_excel(data_path)

# Define an endpoint to get data
@app.route('/get_data', methods=['GET'])
def get_data():
    # Convert DataFrame to JSON and return
    data_json = df.head(10).to_json(orient='records')
    return jsonify(data_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)