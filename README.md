# Project-File-Creator
Creates project files with a certain format file
Like:

trading_bot/
│
├── config/
│   ├── __init__.py
│   ├── config.py              
│   └── logging_config.py      
│
├── core/
│   ├── __init__.py
│   ├── bot.py                 
│   └── exceptions.py          
│
├── data/
│   ├── __init__.py
│   ├── data_feed.py          
│   └── indicators.py         
│
├── exchange/
│   ├── __init__.py
│   ├── binance_futures.py    
│   └── exchange_abc.py       
│
├── risk/
│   ├── __init__.py
│   ├── position.py           
│   └── risk_manager.py       
│
├── strategy/
│   ├── __init__.py
│   ├── strategy_abc.py       
│   ├── ma_strategy.py        
│   └── grid_strategy.py      
│
├── utils/
│   ├── __init__.py
│   ├── logger.py            
│   └── helpers.py           
│
└── main.py                  