from flask import Flask, render_template      
import chromepass as cp
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

@app.route('/script', methods=['GET', 'POST'])
def foo():
    '''execute whatever code you want when the button gets clicked here'''
    print('hi')
    cp.output_csv(cp.main())
    return "Hello, "





if __name__ == "__main__":
    app.run(debug=True)
