"""
Murakkab Kalkulyator - Flask Web Server
"""

from flask import Flask, render_template, request, jsonify
from calculator import Calculator
import webbrowser
import threading
import os
import sys

# Flask ilovasini yaratish
app = Flask(__name__)
calc = Calculator()

# Static va template papkalarini sozlash
if getattr(sys, 'frozen', False):
    # PyInstaller bilan .exe yaratilganda
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)


@app.route('/')
def index():
    """Asosiy sahifa"""
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    """Hisoblash API"""
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        
        if not expression:
            return jsonify({'error': 'Ifoda kiritilmagan'}), 400
        
        result = calc.calculate(expression)
        
        return jsonify({
            'result': result,
            'expression': expression
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/function/<func_name>', methods=['POST'])
def function_call(func_name):
    """Maxsus funksiyalarni chaqirish"""
    try:
        data = request.get_json()
        value = float(data.get('value', 0))
        
        # Funksiyani chaqirish
        if func_name == 'square':
            result = calc.square(value)
        elif func_name == 'cube':
            result = calc.cube(value)
        elif func_name == 'sqrt':
            result = calc.sqrt(value)
        elif func_name == 'cbrt':
            result = calc.cbrt(value)
        elif func_name == 'factorial':
            result = calc.factorial(int(value))
        elif func_name == 'sin':
            result = calc.sin(value)
        elif func_name == 'cos':
            result = calc.cos(value)
        elif func_name == 'tan':
            result = calc.tan(value)
        elif func_name == 'log':
            result = calc.log(value)
        elif func_name == 'ln':
            result = calc.ln(value)
        elif func_name == 'inverse':
            result = calc.inverse(value)
        else:
            return jsonify({'error': 'Noma\'lum funksiya'}), 400
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/power', methods=['POST'])
def power():
    """Daraja hisoblash"""
    try:
        data = request.get_json()
        base = float(data.get('base', 0))
        exponent = float(data.get('exponent', 0))
        
        result = calc.power(base, exponent)
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/percentage', methods=['POST'])
def percentage():
    """Foiz hisoblash"""
    try:
        data = request.get_json()
        value = float(data.get('value', 0))
        percent = float(data.get('percent', 0))
        
        result = calc.percentage(value, percent)
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Xotira funksiyalari
@app.route('/memory/add', methods=['POST'])
def memory_add():
    """Xotiraga qo'shish (M+)"""
    try:
        data = request.get_json()
        value = float(data.get('value', 0))
        result = calc.memory_add(value)
        return jsonify({'memory': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/memory/subtract', methods=['POST'])
def memory_subtract():
    """Xotiradan ayirish (M-)"""
    try:
        data = request.get_json()
        value = float(data.get('value', 0))
        result = calc.memory_subtract(value)
        return jsonify({'memory': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/memory/recall', methods=['GET'])
def memory_recall():
    """Xotirani chaqirish (MR)"""
    try:
        result = calc.memory_recall()
        return jsonify({'memory': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/memory/clear', methods=['POST'])
def memory_clear():
    """Xotirani tozalash (MC)"""
    try:
        result = calc.memory_clear()
        return jsonify({'memory': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Tarix funksiyalari
@app.route('/history', methods=['GET'])
def get_history():
    """Tarixni olish"""
    try:
        history = calc.get_history()
        return jsonify({'history': history})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/history/clear', methods=['POST'])
def clear_history():
    """Tarixni tozalash"""
    try:
        calc.clear_history()
        return jsonify({'message': 'Tarix tozalandi'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def open_browser():
    """Brauzerda ochish"""
    webbrowser.open('http://127.0.0.1:5000')


if __name__ == '__main__':
    # Brauzerda avtomatik ochish
    threading.Timer(1.5, open_browser).start()
    
    # Flask serverni ishga tushirish
    app.run(debug=False, port=5000, host='127.0.0.1')
