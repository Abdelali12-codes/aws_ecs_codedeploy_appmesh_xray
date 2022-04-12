from flask import Flask,render_template, request

@app.route('/')  
def message():  
      return "<html><body><h1>Hi, welcome to the website</h1><h2><a href='/form'> Login</a> </h2></body></html>"  

if __name__ == '__main__':  
   app.run(debug = True, host='0.0.0.0', port="5000")
