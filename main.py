from flask import Flask, render_template, request, redirect , send_file

app=Flask("home")
db={}
@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def camera_number():
  code= request.args.get('code')
  if code :
    existingNumber=db.get(code)
  return render_template(
    "report.html",
    searchingBy=code, 
    )
  

app.run(host="0.0.0.0")