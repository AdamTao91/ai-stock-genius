# 🧠 AI Stock Genius - 智能股票分析器

> 一句话告诉你持有的股票该买还是该卖 | 散户投资神器

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)]()
[![Stars](https://img.shields.io/github/stars/AdamTao91/ai-stock-genius)]()

## 🎯 一句话介绍

**AI Stock Genius** - 让每个散户都拥有自己的AI投资顾问，只需输入股票代码，AI自动分析并给出买卖建议。

## ✨ 核心功能

| 功能 | 说明 |
|------|------|
| 📊 **一键诊断** | 输入股票代码，AI自动分析持仓 |
| 🎯 **买卖建议** | 明确给出"买入/持有/卖出"建议 |
| ⚠️ **风险预警** | 自动识别潜在风险 |
| 📈 **趋势分析** | 技术面+基本面双维度分析 |
| 💡 **操作建议** | 仓位管理、止盈止损指导 |

## 🚀 5秒快速开始

```python
from stock_genius import Analyzer

# 一步到位，AI自动分析
analyzer = Analyzer()
result = analyzer.analyze("588830")  # 入力股票代码

print(result)
# 输出：
# 🧠 AI分析结果: 588830
# 
# 📈 趋势: 📉 下跌趋势，短期可能调整
# 💰 估值: ⚠️ 偏高，当前PE为42.3
# 
# 🎯 建议: ⛔ 建议减仓30%
# 💵 目标价: 2.85元
# 🛡️ 止损: 2.15元
# 
# 💡 点评: 前期涨幅过大，建议落袋为安
```

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

# 分析并生成报告
python -m stock_genius 588830 --report

# 批量分析
python -m stock_genius --batch 588830 600519 000858
```

## 📖 使用示例

### 示例1: 诊断持仓
```python
from stock_genius import Analyzer

analyzer = Analyzer()
report = analyzer.analyze("588830", position=200000, holding_months=4)
print(report)
```

### 示例2: 组合诊断
```python
from stock_genius import Portfolio

portfolio = Portfolio()
portfolio.add("588830", 100000)
portfolio.add("600519", 50000)

report = portfolio.diagnose()
print(report)  # 输出综合诊断报告
```

### 示例3: 风险扫描
```python
from stock_genius import RiskScanner

scanner = RiskScanner()
alerts = scanner.scan(["588830", "600519", "000858"])
for alert in alerts:
    print(f"⚠️ {alert}")
```

## 🏗️ 架构

```
ai-stock-genius/
├── stock_genius/          # 核心分析模块
│   ├── __init__.py
│   ├── analyzer.py        # 股票分析器
│   ├── portfolio.py       # 组合管理
│   ├── risk_scanner.py   # 风险扫描
│   ├── data.py           # 数据获取
│   └── ai.py             # AI分析引擎
├── demo.py               # 演示脚本
├── requirements.txt     # 依赖
└── README.md
```

## 🔧 配置

创建 `config.json`:

```json
{
  "api_key": "your-minimax-api-key",
  "default_position": 100000,
  "risk_level": "moderate",
  "notify_enabled": false
}
```

## 📊 支持的市场

- ✅ 中国A股（沪深京）
- ✅ 港股
- ✅ ETF
- ✅ 基金

## ⚠️ 免责声明

- 本工具仅供投资参考，不构成投资建议
- 投资有风险，入市需谨慎
- AI分析仅供参考，决策需自负

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 License

MIT License

---

**让每个散户都拥有AI投资顾问** 🧠💰

⭐ 如果对你有帮助，请给我们一个 Star！
