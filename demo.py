#!/usr/bin/env python3
"""
AI Stock Genius - 演示脚本
"""

from stock_genius import Analyzer, Portfolio, RiskScanner


def demo_single_stock():
    """演示：单股票分析"""
    print("=" * 50)
    print("📊 单股票分析演示")
    print("=" * 50)
    
    analyzer = Analyzer()
    
    # 分析588830
    print("\n🔍 分析 588830 ETF...")
    result = analyzer.analyze("588830", position=200000, holding_months=4)
    print(result)


def demo_portfolio():
    """演示：组合诊断"""
    print("\n" + "=" * 50)
    print("📈 组合诊断演示")
    print("=" * 50)
    
    portfolio = Portfolio()
    portfolio.add("588830", 100000, 4)
    portfolio.add("600519", 50000, 6)
    portfolio.add("000858", 30000, 2)
    
    print(portfolio.diagnose())


def demo_risk_scan():
    """演示：风险扫描"""
    print("\n" + "=" * 50)
    print("⚠️ 风险扫描演示")
    print("=" * 50)
    
    scanner = RiskScanner()
    alerts = scanner.scan(["588830", "600519", "000858", "300750"])
    
    for alert in alerts:
        print(alert)


def main():
    print("🧠 AI Stock Genius 演示")
    print("=" * 50)
    
    demo_single_stock()
    demo_portfolio()
    demo_risk_scan()
    
    print("\n" + "=" * 50)
    print("✅ 演示完成!")
    print("\n📦 安装: pip install ai-stock-genius")
    print("🔗 GitHub: https://github.com/AdamTao91/ai-stock-genius")


if __name__ == "__main__":
    main()
