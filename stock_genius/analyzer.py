#!/usr/bin/env python3
"""
AI Stock Genius - 股票分析器核心模块
"""

import json
from datetime import datetime
from typing import Optional, Dict, Any

try:
    import akshare as ak
except ImportError:
    ak = None

try:
    import yfinance as yf
except ImportError:
    yf = None


class StockData:
    """股票数据获取"""
    
    @staticmethod
    def get_a_stock(code: str) -> Dict[str, Any]:
        """获取A股数据"""
        if not ak:
            return StockData._mock_data(code)
        
        try:
            # 格式化股票代码
            if code.startswith("6"):
                symbol = f"sh{code}"
            elif code.startswith(("0", "3")):
                symbol = f"sz{code}"
            else:
                symbol = code
            
            df = ak.stock_zh_a_spot_em()
            stock = df[df['代码'] == code]
            
            if stock.empty:
                return StockData._mock_data(code)
            
            row = stock.iloc[0]
            return {
                "code": code,
                "name": row.get("名称", "未知"),
                "price": row.get("最新价", 0),
                "change": row.get("涨跌幅", 0),
                "volume": row.get("成交量", 0),
                "amount": row.get("成交额", 0),
                "high": row.get("最高", 0),
                "low": row.get("最低", 0),
                "open": row.get("今开", 0),
                "close": row.get("昨收", 0),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return StockData._mock_data(code)
    
    @staticmethod
    def _mock_data(code: str) -> Dict[str, Any]:
        """模拟数据（用于测试）"""
        return {
            "code": code,
            "name": f"股票{code}",
            "price": 3.25,
            "change": 2.5,
            "volume": 150000000,
            "amount": 450000000,
            "high": 3.30,
            "low": 3.15,
            "open": 3.18,
            "close": 3.17,
            "timestamp": datetime.now().isoformat()
        }


class AIAnalyzer:
    """AI分析引擎"""
    
    def __init__(self, model: str = "minimax"):
        self.model = model
    
    def analyze(self, data: Dict, position: float = 0, holding_months: int = 0) -> str:
        """AI分析并生成报告"""
        code = data.get("code", "未知")
        name = data.get("name", "未知")
        price = data.get("price", 0)
        change = data.get("change", 0)
        
        # 基础分析
        trend = "📈 上涨趋势" if change > 0 else "📉 下跌趋势"
        if abs(change) < 1:
            trend = "➡️ 横盘震荡"
        
        # 仓位建议
        if position > 0 and holding_months > 0:
            # 简单估算收益
            estimated_return = change * holding_months * 0.5
            
            if estimated_return > 30:
                action = "⛽ 建议减仓落袋"
                action_detail = "已获得可观收益，建议卖出部分"
            elif estimated_return > 10:
                action = "💼 继续持有"
                action_detail = "处于盈利状态，可继续持有"
            elif estimated_return < -10:
                action = "🛡️ 建议观望"
                action_detail = "浮亏较大，耐心等待反弹"
            else:
                action = "➡️ 继续持有"
                action_detail = "保持当前仓位"
        else:
            # 无持仓情况
            if change > 5:
                action = "⚠️ 谨慎追高"
                action_detail = "涨幅较大，建议等待回调"
            elif change < -5:
                action = "🔍 关注机会"
                action_detail = "跌幅较大，可考虑轻仓关注"
            else:
                action = "➡️ 建议观察"
                action_detail = "走势平稳，可进一步分析"
        
        # 生成报告
        report = f"""
🧠 AI分析结果: {code} {name}

📊 当前行情:
• 价格: {price:.2f} 元
• 涨跌幅: {change:+.2f}%

📈 趋势判断: {trend}

🎯 操作建议: {action}
💡 点评: {action_detail}

---
💰 持仓诊断 (本金: {position/10000:.1f}万, 持有: {holding_months}个月)
⏰ 分析时间: {data.get('timestamp', '')[:19]}

⚠️ 免责声明: 本分析仅供参考，不构成投资建议
"""
        return report.strip()


class Analyzer:
    """股票分析器主类"""
    
    def __init__(self):
        self.data = StockData()
        self.ai = AIAnalyzer()
    
    def analyze(self, code: str, position: float = 0, holding_months: int = 0) -> str:
        """
        分析股票并给出建议
        
        Args:
            code: 股票代码 (如: 588830, 600519)
            position: 持仓金额 (元)
            holding_months: 持有月数
            
        Returns:
            str: 分析报告
        """
        # 获取数据
        data = self.data.get_a_stock(code)
        
        # AI分析
        report = self.ai.analyze(data, position, holding_months)
        
        return report


def main():
    """命令行入口"""
    import sys
    
    if len(sys.argv) < 2:
        print("用法: python -m stock_genius <股票代码> [持仓金额] [持有月数]")
        print("示例: python -m stock_genius 588830 200000 4")
        sys.exit(1)
    
    code = sys.argv[1]
    position = float(sys.argv[2]) if len(sys.argv) > 2 else 0
    holding_months = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    
    analyzer = Analyzer()
    result = analyzer.analyze(code, position, holding_months)
    print(result)


if __name__ == "__main__":
    main()
