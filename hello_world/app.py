from flask import Flask, render_template

app   = Flask(__name__)
model = "Chaiwat" 

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result')
def result():
  return render_template('result.html', model=model)



if __name__ == '__main__':
  app.run(debug=True)
