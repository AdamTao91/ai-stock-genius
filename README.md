# 🧠 AI Stock Genius - 智能股票分析器

> 一句话告诉你持有的股票该买还是该卖 | 散户投资神器

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)]()
[![Stars](https://img.shields.io/github/stars/AdamTao91/ai-stock-genius)]()
[![Download](https://img.shields.io/pypi/dm/ai-stock-genius)]()

## 🚀 5秒快速开始

```python
from stock_genius import Analyzer

analyzer = Analyzer()
result = analyzer.analyze("588830", position=200000, holding_months=4)
print(result)
```

**输出示例:**
```
🧠 AI分析结果: 588830

📈 趋势: 📉 下跌趋势，短期可能调整
💰 估值: ⚠️ 偏高，当前PE为42.3

🎯 建议: ⛽ 建议减仓30%
💵 目标价: 2.85元
🛡️ 止损: 2.15元

💡 点评: 前期涨幅过大，建议落袋为安
```

## ✨ 为什么选择 AI Stock Genius?

| 特性 | 说明 |
|------|------|
| ⚡ **快** | 5秒出结果，无需等待 |
| 🧠 **智能** | 基于AI分析，非简单指标 |
| 📊 **全面** | 技术面+基本面+风险面 |
| 💰 **免费** | 完全开源免费 |

## 📦 安装

```bash
pip install ai-stock-genius
```

或克隆使用：

```bash
git clone https://github.com/AdamTao91/ai-stock-genius.git
cd ai-stock-genius
pip install -r requirements.txt
python demo.py
```

## 🖥️ 命令行工具

```bash
# 分析单只股票
python -m stock_genius 588830

# 带持仓分析
python -m stock_genius 588830 200000 4

# 批量分析
python -m stock_genius --batch 588830 600519 000858
```

## 📖 功能列表

### 1. 单股诊断
```python
from stock_genius import Analyzer

analyzer = Analyzer()
report = analyzer.analyze("588830", position=200000, holding_months=4)
```

### 2. 组合管理
```python
from stock_genius import Portfolio

portfolio = Portfolio()
portfolio.add("588830", 100000, 4)
portfolio.add("600519", 50000, 6)
print(portfolio.diagnose())
```

### 3. 风险扫描
```python
from stock_genius import RiskScanner

scanner = RiskScanner()
alerts = scanner.scan(["588830", "600519"])
for alert in alerts:
    print(alert)
```

## 📊 支持的市场

- ✅ 中国A股（沪深京）
- ✅ 港股
- ✅ ETF
- ✅ 基金

## 🏗️ 架构

```
ai-stock-genius/
├── stock_genius/
│   ├── analyzer.py        # 股票分析器
│   ├── portfolio.py       # 组合管理
│   └── risk_scanner.py   # 风险扫描
├── demo.py
├── requirements.txt
└── README.md
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## ⚠️ 免责声明

- 本工具仅供投资参考，不构成投资建议
- 投资有风险，入市需谨慎

---

**让每个散户都拥有AI投资顾问** 🧠💰

⭐ Star us: https://github.com/AdamTao91/ai-stock-genius
