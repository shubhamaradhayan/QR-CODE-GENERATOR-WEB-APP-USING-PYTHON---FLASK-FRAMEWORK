from flask import Flask,render_template,redirect,request
from ensurepip import version
import qrcode
import image
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    
    if request.method == 'POST':
        data = request.form['data']
        qr = qrcode.QRCode(version=10, box_size=10, border=3 )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black",back_color="white")
        img.save("static/qr.png")        

        redirect("/")
    return render_template("index.html")
    


app.run(debug=True)

    