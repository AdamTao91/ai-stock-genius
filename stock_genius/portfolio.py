#!/usr/bin/env python3
"""
Portfolio - 组合管理模块
"""

from typing import List, Dict, Any
from .analyzer import Analyzer


class Portfolio:
    """投资组合管理"""
    
    def __init__(self):
        self.holdings: List[Dict[str, Any]] = []
        self.analyzer = Analyzer()
    
    def add(self, code: str, position: float, holding_months: int = 1):
        """添加持仓"""
        self.holdings.append({
            "code": code,
            "position": position,
            "holding_months": holding_months
        })
    
    def diagnose(self) -> str:
        """组合诊断"""
        if not self.holdings:
            return "⚠️ 组合为空，请先添加持仓"
        
        total_value = sum(h["position"] for h in self.holdings)
        
        report = f"""
📊 投资组合诊断报告
══════════════════════════════

💰 总持仓: {total_value/10000:.2f} 万元
📈 股票数量: {len(self.holdings)} 只

"""
        
        for i, h in enumerate(self.holdings, 1):
            stock_report = self.analyzer.analyze(
                h["code"], 
                h["position"], 
                h["holding_months"]
            )
            report += f"{'─'*40}\n"
            report += f"【{i}】{stock_report}\n\n"
        
        report += f"""
{'='*40}
⚠️ 免责声明: 本报告仅供参考，不构成投资建议
"""
        
        return report.strip()


if __name__ == "__main__":
    # 演示
    p = Portfolio()
    p.add("588830", 100000, 4)
    p.add("600519", 50000, 2)
    print(p.diagnose())
