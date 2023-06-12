from flask import Flask, render_template,jsonify
app = Flask(__name__)
ITEMS=[{
  "name":"Galaxy",
  "desc":"Vast collections of stars"
  },
{
  "name":"planets",
  "desc":"Celestial bodies in space"
},
{
  "name":"nebulae",
  "desc":"Cosmic art in celestial canvas"
}
       ]
@app.route("/")
def helloworld():
  return render_template("home.html",item=ITEMS)
@app.route("/api/item")
def list_items():
  return jsonify(ITEMS)
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
  