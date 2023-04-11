from flask import Flask, render_template, request, redirect, url_for, session
import piReader
import time
import random

app = Flask(__name__)
app.config['DEBUG'] = True

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def formProcessing(vReader):
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
    elif request.form['formID'] == '37bit5x':
        i = 1
        while i < 6:
            piReader.sendData(piReader.sendH10302(12006270498), vReader)
            time.sleep(.25)
            i = i + 1
    elif request.form['formID'] == 'random37Bit':
        cn = random.randrange(0, 34359738367)
        piReader.sendData(piReader.sendH10302(cn), vReader)
        print(cn)

def pinProcessing(vReader):
    if request.form['formID'] == 'button1':
        piReader.sendData(piReader.sendPIN(1), vReader)
    elif request.form['formID'] == 'button2':
        piReader.sendData(piReader.sendPIN(2), vReader)
    elif request.form['formID'] == 'button3':
        piReader.sendData(piReader.sendPIN(3), vReader)
    elif request.form['formID'] == 'button4':
        piReader.sendData(piReader.sendPIN(4), vReader)
    elif request.form['formID'] == 'button5':
        piReader.sendData(piReader.sendPIN(5), vReader)
    elif request.form['formID'] == 'button6':
        piReader.sendData(piReader.sendPIN(6), vReader)
    elif request.form['formID'] == 'button7':
        piReader.sendData(piReader.sendPIN(7), vReader)
    elif request.form['formID'] == 'button8':
        piReader.sendData(piReader.sendPIN(8), vReader)
    elif request.form['formID'] == 'button9':
        piReader.sendData(piReader.sendPIN(9), vReader)
    elif request.form['formID'] == 'button0':
        piReader.sendData(piReader.sendPIN(0), vReader)
    elif request.form['formID'] == 'button*':
        piReader.sendData(piReader.sendPIN(10), vReader)
    elif request.form['formID'] == 'button#':
        piReader.sendData(piReader.sendPIN(11), vReader)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        if request.form['formID'] == 'Reader1':
            return redirect(url_for('reader1'))
        elif request.form['formID'] == 'Reader2':
            return redirect(url_for('reader2'))
        elif request.form['formID'] == 'Reader3':
            return redirect(url_for('reader3'))
        elif request.form['formID'] == 'Reader4':
            return redirect(url_for('reader4'))
    return render_template('index.html', readerHeader='Choose a Reader')

@app.route('/reader1', methods=('GET', 'POST'))
def reader1():
    if request.method == 'POST':
        if request.form['formID'] == 'pin':
            session['reader_var'] = 'reader1'
            return redirect(url_for('pin'))
        else:
            formProcessing(piReader.Reader1)
    return render_template('vReader.html', readerHeader='Reader 1')

@app.route('/reader2', methods=('GET', 'POST'))
def reader2():
    if request.method == 'POST':
        if request.form['formID'] == 'pin':
            session['reader_var'] = 'reader2'
            return redirect(url_for('pin'))
        else:
            formProcessing(piReader.Reader2)
    return render_template('vReader.html', readerHeader='Reader 2')

@app.route('/reader3', methods=('GET', 'POST'))
def reader3():
    if request.method == 'POST':
        formProcessing(piReader.Reader3)
    return render_template('vReader.html', readerHeader='Reader 3')

@app.route('/reader4', methods=('GET', 'POST'))
def reader4():
    if request.method == 'POST':
        formProcessing(piReader.Reader4)
    return render_template('vReader.html', readerHeader='Reader 4')

@app.route('/pin', methods=('GET', 'POST'))
def pin():
    if request.method == 'POST':
        reader_var = session.get('reader_var', None)
        if request.form['formID'] == 'back':
            return redirect(url_for(reader_var))
        if reader_var == 'reader1':
            pinProcessing(piReader.Reader1)
        elif reader_var == 'reader2':
            pinProcessing(piReader.Reader2)
    return render_template('pin.html', readerHeader='PIN')

if __name__ == '__main__':
    app.run(host="0.0.0.0")