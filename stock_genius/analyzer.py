#!/usr/bin/env python3
"""
AI Stock Genius - 股票分析器核心模块 v1.1
增强版：加入更多分析维度
"""

import json
from datetime import datetime
from typing import Optional, Dict, Any, List

try:
    import akshare as ak
except ImportError:
    ak = None


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
    def get_realtime_quotes(codes: List[str]) -> List[Dict]:
        """批量获取实时行情"""
        results = []
        for code in codes:
            data = StockData.get_a_stock(code)
            results.append(data)
        return results
    
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
    """AI分析引擎 v1.1"""
    
    def __init__(self, model: str = "minimax"):
        self.model = model
    
    def analyze(self, data: Dict, position: float = 0, holding_months: int = 0) -> str:
        """AI分析并生成报告"""
        code = data.get("code", "未知")
        name = data.get("name", "未知")
        price = data.get("price", 0)
        change = data.get("change", 0)
        
        # 趋势分析
        trend = self._analyze_trend(change)
        
        # 操作建议
        action, action_detail = self._get_action(change, position, holding_months)
        
        # 风险评估
        risk_level = self._assess_risk(change, price)
        
        # 生成报告
        report = f"""
🧠 AI分析: {code} {name}
{'='*40}

📊 行情:
• 价格: {price:.2f} 元
• 涨跌幅: {change:+.2f}%

📈 趋势: {trend}
🎯 建议: {action}
🛡️ 风险: {risk_level}

💡 {action_detail}

{'='*40}
⏰ {data.get('timestamp', '')[:19]}
⚠️ 仅供参考，不构成投资建议
"""
        return report.strip()
    
    def _analyze_trend(self, change: float) -> str:
        """分析趋势"""
        if change > 3:
            return "📈 强势上涨，可能继续冲高"
        elif change > 0:
            return "➡️ 小幅上涨，震荡整理"
        elif change > -3:
            return "➡️ 小幅下跌，观望为主"
        else:
            return "📉 明显下跌，谨防回调"
    
    def _get_action(self, change: float, position: float, holding_months: int) -> tuple:
        """获取操作建议"""
        if position == 0:
            # 未持仓
            if change > 7:
                return "⚠️ 建议观望", "涨幅过大，追高风险高"
            elif change > 3:
                return "🔍 轻仓关注", "可小资金试仓"
            elif change < -7:
                return "📈 关注机会", "超跌可能反弹"
            elif change < -3:
                return "🔍 关注支撑", "等待企稳信号"
            else:
                return "➡️ 建议观察", "走势平稳"
        else:
            # 有持仓
            if change > 20:
                return "⛽ 建议减仓", "收益可观，落袋为安"
            elif change > 10:
                return "💼 继续持有", "处于上升趋势"
            elif change > 0:
                return "➡️ 持有观望", "保持当前仓位"
            elif change > -10:
                return "🛡️ 持有等待", "耐心等待反弹"
            else:
                return "⚠️ 考虑止损", "亏损较大，需谨慎"
    
    def _assess_risk(self, change: float, price: float) -> str:
        """风险评估"""
        if change > 9:
            return "🔴 高风险"
        elif change > 5:
            return "🟡 中风险"
        elif change > -5:
            return "🟢 低风险"
        else:
            return "🟠 中风险"


class Analyzer:
    """股票分析器主类"""
    
    def __init__(self):
        self.data = StockData()
        self.ai = AIAnalyzer()
    
    def analyze(self, code: str, position: float = 0, holding_months: int = 0) -> str:
        """
        分析股票并给出建议
        """
        data = self.data.get_a_stock(code)
        report = self.ai.analyze(data, position, holding_months)
        return report
    
    def batch_analyze(self, codes: List[str]) -> Dict[str, str]:
        """批量分析"""
        results = {}
        for code in codes:
            results[code] = self.analyze(code)
        return results


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
