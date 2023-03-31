from flask import Flask, render_template, request
import piReader
import time
import random

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=('GET', 'POST'))
def index():
    vReader = piReader.Reader1
    if request.method == 'POST':
        if request.form['formID'] == 'H10302form':
            if request.form['cardNumberH10302'] == '':
                return render_template('index.html')
            else:
                piReader.sendData(piReader.sendH10302(request.form['cardNumberH10302']), vReader)
        elif request.form['formID'] == 'H10301form':
            if (request.form['facilityCode26'] == '') or (request.form['cardNumber26'] == ''):
                return render_template('index.html')
            else:
                piReader.sendData(piReader.sendH10301(request.form['facilityCode26'], request.form['cardNumber26']), vReader)
        elif request.form['formID'] == 'H10304form':
            if (request.form['facilityCodeH10304'] == '') or (request.form['cardNumberH10304'] == ''):
                return render_template('index.html')
            else:
                piReader.sendData(piReader.sendH10304(request.form['facilityCodeH10304'], request.form['cardNumberH10304']), vReader)
        elif request.form['formID'] == '12006270498':
            piReader.sendData(piReader.sendH10302(12006270498), vReader)
        elif request.form['formID'] == '12006270499':
            piReader.sendData(piReader.sendH10302(12006270499), vReader)
        elif request.form['formID'] == '12006270500':
            piReader.sendData(piReader.sendH10302(12006270450), vReader)
        elif request.form['formID'] == '1554/245645':
            piReader.sendData(piReader.sendH10304(1554, 245645), vReader)
        elif request.form['formID'] == '22/205':
            piReader.sendData(piReader.sendH10301(22, 205), vReader)
        elif request.form['formID'] == 'multi37Bit':
            cn = 12006270495
            while cn < 12006270500:
                piReader.sendData(piReader.sendH10302(cn), vReader)
                time.sleep(.25)
                cn = cn +1
        elif request.form['formID'] == '26bit5x':
            i = 1
            while i < 6:
                piReader.sendData(piReader.sendH10302(12006270498), vReader)
                time.sleep(.25)
                i = i + 1
        elif request.form['formID'] == 'random37Bit':
            cn = random.randrange(0, 34359738367)
            piReader.sendData(piReader.sendH10302(cn), vReader)
            print(cn)
    return render_template('index.html')
