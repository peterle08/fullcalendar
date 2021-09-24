# Created by Hoang Le
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/cal")
def day_grid_month():
    events = [
        {
            'title' : 'Event 1',
            'start' : '2021-09-23',
            'end' : '2021-09-23'
        },
        {
            'title' : 'Event 2',
            'start' : '2021-09-24',
            'end' : '2021-09-25'
        },
        {
            'title' : 'Event 3',
            'start' : '2021-09-25',
            'end' : '2021-09-25'
        },
    ]
    return render_template('calendar.html', events=events)

@app.route("/cal2")
def time_grid_week():
    events = [
        {
            'title' : 'Event 1',
            'start' : '2021-09-22 16:05:25',
            'end' : '2021-09-22 18:30:00'
        },
        {
            'title' : 'Event 2',
            'start' : '2021-09-24 09:00:05',
            'end' : '2021-09-24 16:05:25'
        },
        {
            'title' : 'Event extra',
            'start' : '2021-09-24 09:00:05',
            'end' : '2021-09-24 16:05:25'
        },
        {
            'title' : 'Event 3',
            'start' : '2021-09-25 10:00:05',
            'end' : '2021-09-25 12:05:25'
        },
    ]
    return render_template('gridweek.html', events=events)

if __name__ == "__main__":
    app.run()