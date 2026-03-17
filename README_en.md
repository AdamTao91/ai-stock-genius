# 🧠 AI Stock Genius

> Tell you whether to BUY or SELL in one sentence | The AI Investment Assistant for Retail Investors

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)]()
[![Stars](https://img.shields.io/github/stars/AdamTao91/ai-stock-genius)]()

## 🚀 Quick Start (5 seconds)

```python
from stock_genius import Analyzer

analyzer = Analyzer()
result = analyzer.analyze("588830", position=200000, holding_months=4)
print(result)
```

## ✨ Why AI Stock Genius?

| Feature | Description |
|---------|-------------|
| ⚡ **Fast** | Get results in 5 seconds |
| 🧠 **Smart** | AI-powered analysis |
| 📊 **Comprehensive** | Technical + Fundamental + Risk |
| 💰 **Free** | Open source & free |

## 📦 Install

```bash
pip install ai-stock-genius
```

Or clone:

```bash
git clone https://github.com/AdamTao91/ai-stock-genius.git
cd ai-stock-genius
pip install -r requirements.txt
python demo.py
```

## 🖥️ CLI

```bash
python -m stock_genius 588830
python -m stock_genius 588830 200000 4
python -m stock_genius --batch 588830 600519 000858
```

## 📊 Supported Markets

- ✅ China A-shares (Shanghai, Shenzhen, Beijing)
- ✅ HK Stocks
- ✅ ETFs
- ✅ Funds

## ⚠️ Disclaimer

- This tool is for reference only
- Invest at your own risk

---

⭐ Star us: https://github.com/AdamTao91/ai-stock-genius
