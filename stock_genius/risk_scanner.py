#!/usr/bin/env python3
"""
Risk Scanner - 风险扫描模块
"""

from typing import List, Dict
from .analyzer import StockData


class RiskScanner:
    """风险扫描器"""
    
    def __init__(self):
        self.data = StockData()
    
    def scan(self, codes: List[str]) -> List[str]:
        """
        扫描股票风险
        
        Args:
            codes: 股票代码列表
            
        Returns:
            List[str]: 风险提示列表
        """
        alerts = []
        
        for code in codes:
            data = self.data.get_a_stock(code)
            price = data.get("price", 0)
            change = data.get("change", 0)
            
            # 风险检查
            if change > 9:
                alerts.append(f"🔴 {code} {data.get('name')} 涨幅过大({change:+.1f}%)，注意回调风险")
            elif change < -9:
                alerts.append(f"🟠 {code} {data.get('name')} 跌幅较大({change:+.1f}%)，关注支撑位")
            elif change > 5:
                alerts.append(f"🟡 {code} {data.get('name')} 涨幅较高({change:+.1f}%)，谨慎追高")
        
        if not alerts:
            alerts.append("✅ 扫描完成，未发现明显风险")
        
        return alerts


if __name__ == "__main__":
    # 演示
    scanner = RiskScanner()
    alerts = scanner.scan(["588830", "600519", "000858"])
    for a in alerts:
        print(a)
