# Project-File-Creator
Creates project files with a certain format file
Like:

trading_bot/
│
├── config/
│   ├── __init__.py
│   ├── config.py              # 配置文件
│   └── logging_config.py      # 日志配置
│
├── core/
│   ├── __init__.py
│   ├── bot.py                 # 交易机器人核心类
│   └── exceptions.py          # 自定义异常类
│
├── data/
│   ├── __init__.py
│   ├── data_feed.py          # 数据获取和处理
│   └── indicators.py         # 技术指标计算
│
├── exchange/
│   ├── __init__.py
│   ├── binance_futures.py    # 币安合约接口封装
│   └── exchange_abc.py       # 交易所抽象基类
│
├── risk/
│   ├── __init__.py
│   ├── position.py           # 持仓管理
│   └── risk_manager.py       # 风险控制
│
├── strategy/
│   ├── __init__.py
│   ├── strategy_abc.py       # 策略抽象基类
│   ├── ma_strategy.py        # 移动平均线策略
│   └── grid_strategy.py      # 网格策略
│
├── utils/
│   ├── __init__.py
│   ├── logger.py            # 日志工具
│   └── helpers.py           # 辅助函数
│
└── main.py                  # 主程序入口
