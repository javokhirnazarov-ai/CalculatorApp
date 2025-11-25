"""
Murakkab Kalkulyator - Matematik Operatsiyalar Moduli
"""

import math
import re
from typing import Union, List, Dict


class Calculator:
    """Murakkab matematik operatsiyalarni bajaruvchi kalkulyator klassi"""
    
    def __init__(self):
        self.memory = 0
        self.history: List[Dict[str, str]] = []
        self.last_result = 0
    
    def add_to_history(self, expression: str, result: str):
        """Hisoblash tarixiga qo'shish"""
        self.history.append({
            'expression': expression,
            'result': result
        })
        # Faqat oxirgi 50 ta hisoblashni saqlash
        if len(self.history) > 50:
            self.history.pop(0)
    
    def get_history(self) -> List[Dict[str, str]]:
        """Tarixni olish"""
        return self.history
    
    def clear_history(self):
        """Tarixni tozalash"""
        self.history = []
    
    # Xotira funksiyalari
    def memory_add(self, value: float):
        """Xotiraga qo'shish (M+)"""
        self.memory += value
        return self.memory
    
    def memory_subtract(self, value: float):
        """Xotiradan ayirish (M-)"""
        self.memory -= value
        return self.memory
    
    def memory_recall(self) -> float:
        """Xotirani chaqirish (MR)"""
        return self.memory
    
    def memory_clear(self):
        """Xotirani tozalash (MC)"""
        self.memory = 0
        return self.memory
    
    # Asosiy matematik operatsiyalar
    def calculate(self, expression: str) -> Union[float, str]:
        """
        Matematik ifodani hisoblash
        """
        try:
            # Maxsus funksiyalarni almashtirish
            expression = self._prepare_expression(expression)
            
            # Xavfsiz hisoblash
            result = self._safe_eval(expression)
            
            # Natijani saqlash
            self.last_result = result
            
            # Tarixga qo'shish
            self.add_to_history(expression, str(result))
            
            return result
        except ZeroDivisionError:
            return "Xato: Nolga bo'lish mumkin emas"
        except Exception as e:
            return f"Xato: {str(e)}"
    
    def _prepare_expression(self, expr: str) -> str:
        """Ifodani hisoblash uchun tayyorlash"""
        # Trigonometrik funksiyalar
        expr = expr.replace('sin(', 'math.sin(math.radians(')
        expr = expr.replace('cos(', 'math.cos(math.radians(')
        expr = expr.replace('tan(', 'math.tan(math.radians(')
        
        # Logarifmlar
        expr = expr.replace('log(', 'math.log10(')
        expr = expr.replace('ln(', 'math.log(')
        
        # Faktorial
        expr = re.sub(r'(\d+)!', r'math.factorial(\1)', expr)
        
        # Pi va E
        expr = expr.replace('π', 'math.pi')
        expr = expr.replace('e', 'math.e')
        
        # Daraja
        expr = expr.replace('^', '**')
        
        # Ildizlar
        expr = expr.replace('√(', 'math.sqrt(')
        expr = expr.replace('∛(', 'math.pow(')
        
        return expr
    
    def _safe_eval(self, expr: str) -> float:
        """Xavfsiz ifoda hisoblash"""
        # Ruxsat etilgan funksiyalar va o'zgaruvchilar
        safe_dict = {
            'math': math,
            '__builtins__': {}
        }
        
        result = eval(expr, safe_dict)
        return float(result)
    
    # Maxsus funksiyalar
    def square(self, x: float) -> float:
        """Kvadrat"""
        return x ** 2
    
    def cube(self, x: float) -> float:
        """Kub"""
        return x ** 3
    
    def power(self, base: float, exponent: float) -> float:
        """Daraja"""
        return base ** exponent
    
    def sqrt(self, x: float) -> Union[float, str]:
        """Kvadrat ildiz"""
        if x < 0:
            return "Xato: Manfiy sondan ildiz olib bo'lmaydi"
        return math.sqrt(x)
    
    def cbrt(self, x: float) -> float:
        """Kub ildiz"""
        return math.pow(abs(x), 1/3) * (1 if x >= 0 else -1)
    
    def factorial(self, n: int) -> Union[int, str]:
        """Faktorial"""
        if n < 0:
            return "Xato: Manfiy sondan faktorial olib bo'lmaydi"
        if n > 170:
            return "Xato: Son juda katta"
        return math.factorial(int(n))
    
    def sin(self, x: float) -> float:
        """Sinus (gradusda)"""
        return math.sin(math.radians(x))
    
    def cos(self, x: float) -> float:
        """Kosinus (gradusda)"""
        return math.cos(math.radians(x))
    
    def tan(self, x: float) -> float:
        """Tangens (gradusda)"""
        return math.tan(math.radians(x))
    
    def log(self, x: float) -> Union[float, str]:
        """Logarifm (10 asosda)"""
        if x <= 0:
            return "Xato: Logarifm faqat musbat sonlar uchun"
        return math.log10(x)
    
    def ln(self, x: float) -> Union[float, str]:
        """Natural logarifm"""
        if x <= 0:
            return "Xato: Logarifm faqat musbat sonlar uchun"
        return math.log(x)
    
    def percentage(self, value: float, percent: float) -> float:
        """Foiz hisoblash"""
        return (value * percent) / 100
    
    def inverse(self, x: float) -> Union[float, str]:
        """Teskari son (1/x)"""
        if x == 0:
            return "Xato: Nolga bo'lish mumkin emas"
        return 1 / x
