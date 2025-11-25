// Murakkab Kalkulyator - Frontend JavaScript

let currentDisplay = '0';
let lastResult = null;
let historyVisible = true;

// Displeyni yangilash
function updateDisplay(value) {
    const display = document.getElementById('display');
    display.value = value;
    currentDisplay = value;
}

// Displeyga qo'shish
function appendToDisplay(value) {
    if (currentDisplay === '0' || currentDisplay === 'Xato' || lastResult !== null) {
        if (value === '.' && currentDisplay === '0') {
            currentDisplay = '0.';
        } else if (['+', '-', '*', '/', '^', '%'].includes(value)) {
            if (lastResult !== null) {
                currentDisplay = lastResult + value;
                lastResult = null;
            } else {
                currentDisplay = value;
            }
        } else {
            currentDisplay = value;
            lastResult = null;
        }
    } else {
        currentDisplay += value;
    }
    updateDisplay(currentDisplay);
}

// Displeyni tozalash
function clearDisplay() {
    currentDisplay = '0';
    lastResult = null;
    updateDisplay(currentDisplay);
    document.getElementById('displayHistory').textContent = '';
}

// Backspace
function backspace() {
    if (currentDisplay.length > 1) {
        currentDisplay = currentDisplay.slice(0, -1);
    } else {
        currentDisplay = '0';
    }
    updateDisplay(currentDisplay);
}

// Hisoblash
async function calculate() {
    try {
        const expression = currentDisplay;
        
        // Tarix displeyiga ko'rsatish
        document.getElementById('displayHistory').textContent = expression;
        
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ expression: expression })
        });
        
        const data = await response.json();
        
        if (data.error) {
            updateDisplay('Xato');
            setTimeout(() => updateDisplay('0'), 2000);
        } else {
            const result = formatNumber(data.result);
            updateDisplay(result);
            lastResult = result;
            
            // Tarixni yangilash
            loadHistory();
        }
    } catch (error) {
        console.error('Xato:', error);
        updateDisplay('Xato');
        setTimeout(() => updateDisplay('0'), 2000);
    }
}

// Funksiyani qo'llash
async function applyFunction(funcName) {
    try {
        const value = parseFloat(currentDisplay);
        
        if (isNaN(value)) {
            updateDisplay('Xato');
            return;
        }
        
        const response = await fetch(`/function/${funcName}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ value: value })
        });
        
        const data = await response.json();
        
        if (data.error) {
            updateDisplay('Xato');
            setTimeout(() => updateDisplay('0'), 2000);
        } else {
            const result = formatNumber(data.result);
            updateDisplay(result);
            lastResult = result;
            
            // Tarixga qo'shish
            document.getElementById('displayHistory').textContent = `${funcName}(${value})`;
        }
    } catch (error) {
        console.error('Xato:', error);
        updateDisplay('Xato');
        setTimeout(() => updateDisplay('0'), 2000);
    }
}

// Xotira funksiyalari
async function memoryAdd() {
    try {
        const value = parseFloat(currentDisplay);
        if (isNaN(value)) return;
        
        const response = await fetch('/memory/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ value: value })
        });
        
        const data = await response.json();
        updateMemoryIndicator(data.memory);
    } catch (error) {
        console.error('Xato:', error);
    }
}

async function memorySubtract() {
    try {
        const value = parseFloat(currentDisplay);
        if (isNaN(value)) return;
        
        const response = await fetch('/memory/subtract', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ value: value })
        });
        
        const data = await response.json();
        updateMemoryIndicator(data.memory);
    } catch (error) {
        console.error('Xato:', error);
    }
}

async function memoryRecall() {
    try {
        const response = await fetch('/memory/recall');
        const data = await response.json();
        
        if (data.memory !== undefined) {
            updateDisplay(formatNumber(data.memory));
            lastResult = null;
        }
    } catch (error) {
        console.error('Xato:', error);
    }
}

async function memoryClear() {
    try {
        const response = await fetch('/memory/clear', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        const data = await response.json();
        updateMemoryIndicator(data.memory);
    } catch (error) {
        console.error('Xato:', error);
    }
}

function updateMemoryIndicator(value) {
    const indicator = document.getElementById('memoryIndicator');
    indicator.textContent = `M: ${formatNumber(value)}`;
    
    // Animatsiya
    indicator.style.transform = 'scale(1.1)';
    setTimeout(() => {
        indicator.style.transform = 'scale(1)';
    }, 200);
}

// Tarix funksiyalari
async function loadHistory() {
    try {
        const response = await fetch('/history');
        const data = await response.json();
        
        const historyList = document.getElementById('historyList');
        
        if (data.history && data.history.length > 0) {
            historyList.innerHTML = '';
            
            // Teskari tartibda ko'rsatish (eng yangi birinchi)
            data.history.reverse().forEach(item => {
                const historyItem = document.createElement('div');
                historyItem.className = 'history-item';
                historyItem.onclick = () => {
                    updateDisplay(item.result);
                    lastResult = null;
                };
                
                historyItem.innerHTML = `
                    <div class="history-expression">${item.expression}</div>
                    <div class="history-result">= ${item.result}</div>
                `;
                
                historyList.appendChild(historyItem);
            });
        } else {
            historyList.innerHTML = '<p class="history-empty">Hozircha tarix bo\'sh</p>';
        }
    } catch (error) {
        console.error('Xato:', error);
    }
}

async function clearHistory() {
    try {
        const response = await fetch('/history/clear', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        if (response.ok) {
            loadHistory();
        }
    } catch (error) {
        console.error('Xato:', error);
    }
}

function toggleHistory() {
    const historyPanel = document.getElementById('historyPanel');
    historyVisible = !historyVisible;
    
    if (historyVisible) {
        historyPanel.classList.remove('hidden');
        loadHistory();
    } else {
        historyPanel.classList.add('hidden');
    }
}

// Sonni formatlash
function formatNumber(num) {
    if (typeof num === 'string') return num;
    
    // Juda kichik yoki katta sonlar uchun
    if (Math.abs(num) < 0.000001 && num !== 0) {
        return num.toExponential(6);
    }
    if (Math.abs(num) > 999999999) {
        return num.toExponential(6);
    }
    
    // Oddiy formatlash
    const rounded = Math.round(num * 1000000) / 1000000;
    return rounded.toString();
}

// Klaviatura qo'llab-quvvatlash
document.addEventListener('keydown', (event) => {
    const key = event.key;
    
    // Raqamlar
    if (key >= '0' && key <= '9') {
        appendToDisplay(key);
    }
    // Operatorlar
    else if (key === '+' || key === '-' || key === '*' || key === '/') {
        appendToDisplay(key);
    }
    // Nuqta
    else if (key === '.') {
        appendToDisplay(key);
    }
    // Enter - hisoblash
    else if (key === 'Enter') {
        event.preventDefault();
        calculate();
    }
    // Backspace
    else if (key === 'Backspace') {
        event.preventDefault();
        backspace();
    }
    // Escape - tozalash
    else if (key === 'Escape') {
        clearDisplay();
    }
    // Qavslar
    else if (key === '(') {
        appendToDisplay('(');
    }
    else if (key === ')') {
        appendToDisplay(')');
    }
});

// Sahifa yuklanganda tarixni yuklash
window.addEventListener('load', () => {
    loadHistory();
});
