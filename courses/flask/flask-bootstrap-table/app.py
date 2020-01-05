
from flask import Flask, render_template
import json

# Create a table that is sortable by header
app = Flask(__name__)

data = [{
  "name": "Alice",
  "score": "10",
  "attention": "122",
  "status": "Student"
},
 {
  "name": "Bob",
  "score": "288",
  "attention": "20",
  "status": "Employee"
}, {
  "name": "Charlene",
  "score": "340",
  "attention": "20",
  "status": "Chief"
}]
# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
columns = [
  {
    "field": "name",
    "title": "name",
    "sortable": True,
  },
  {
    "field": "score",
    "title": "score",
    "sortable": True,
  },
  {
    "field": "attention",
    "title": "attention",
    "sortable": True,
  },
  {
    "field": "status",
    "title": "status",
    "sortable": True,
  }
]

@app.route('/')
def index():
    return render_template("table.html",
      data=data,
      columns=columns,
      title='Flask Bootstrap Table')


if __name__ == '__main__':
    app.run(debug=True)
