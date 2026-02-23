from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Shoes", "price": 1000},
    {"name": "Bag", "price": 1500},
    {"name": "Watch", "price": 2000}
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)