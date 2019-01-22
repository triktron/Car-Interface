C:\Users\vaneschel\Python37\python.exe -m PyInstaller --hidden-import=cefpython3 --hidden-import=wx.lib.agw.speedmeter --hidden-import=json --add-data apps;apps --add-data icons;icons --add-data libs;libs --add-data services;services --onefile main.py
rmdir build
