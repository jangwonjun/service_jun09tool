from flask import Flask, request, redirect, render_template, url_for, session
from proctitle import setproctitle
from env import FLASK_ENUM
from modules.product_add import product

app = Flask(__name__, static_url_path='/static')
setproctitle.setproctitle(FLASK_ENUM.PROC_NAME)


barcode_data = product()
price = barcode_data.product_review()

@app.route('/')
def main():
    print(f"출력가격 :{price}")
    return render_template('index.html',data=price)

@app.route('/numcode',methods=['POST'])
def numcode():
    barcode_number = request.form.get('barcode_number')
    print(barcode_number)
    return barcode_number

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=FLASK_ENUM.PORT)