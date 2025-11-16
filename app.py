from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data
data = pd.read_csv('static/dataset.csv')
subjects = data['Subject'].tolist()

@app.route('/', methods=['GET', 'POST'])
def index():
    status = None
    selected_subject = None
    pending_1st = None
    pending_2nd = None

    if request.method == 'POST':
        selected_subject = request.form.get('subject')
        row = data[data['Subject'] == selected_subject].iloc[0]
        total = row['Total']
        eval1 = row['1st Evaluation']
        eval2 = row['2nd Evaluation']

        pending_1st = total - eval1
        pending_2nd = total - eval2

        # Set status based on the evaluations
        if total == eval1 == eval2:
            status = 'NOT-PENDING'  # Capitalize 'NOT-PENDING'
        else:
            status = 'PENDING'  # Capitalize 'PENDING'

    return render_template(
        'index.html',
        subjects=subjects,
        status=status,
        selected=selected_subject,
        pending_1st=pending_1st,
        pending_2nd=pending_2nd
    )

if __name__ == '__main__':
    app.run(debug=True)
