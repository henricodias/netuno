import MetaTrader5 as mt5
import talib as tb
import pandas as pd
import numpy as np



#configura parâmetros da biblioteca pandas
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)
pd.set_option('mode.chained_assignment', None)

#importa dados do ativo
ticker = 'WINJ22'
mt5.initialize()
mt5.symbol_select(ticker)

df = mt5.copy_rates_from_pos(ticker, mt5.TIMEFRAME_M5, 0, 2112)
df = pd.DataFrame(df)
df['time'] = pd.to_datetime(df['time'], unit='s')
# df = df.set_index('time') #tempo em index



df['body'] = df['close'] - df['open']

#df['candle'] = np.sign(df['close'] - df['open'])

for i in df:
    if df['body'][i] > 0:
        df['candle'] = 'positivo'
    elif df['body'][i] < 0:
        df['candle'] = 'negativo'
    else:
        df['candle'] = 'neutro'


# if (df['body'] > 0):
#     df['lowerShadow'] = df['open'] - df['low']
#     df['upperShadow'] = df['high'] - df['close']
# elif(df['body'] < 0):
#     df['lowerShadow'] = df['close'] - df['low']
#     df['upperShadow'] = df['high'] - df['open']
# else:
#     df['lowerShadow'] = df['close'] - df['low']
#     df['upperShadow'] = df['high'] - df['close']
#
# if(df['body'].iloc[-1] > 0):
#     if(df['lowerShadow'].iloc[-1] >= (2.5 * df['body'].iloc[-1]) and df['upperShadow'].iloc[-1] < 40):
#         df['hammer'] = 1
#     else:
#         df['hammer'] = 0
# elif(  df['body'].iloc[-1] < 0):
#     if (df['lowerShadow'].iloc[-1] >= (2.5 * df['body'].iloc[-1]) and df['upperShadow'].iloc[-1] < 40):
#         df['hammer'] = 1
#     else:
#         df['hammer'] = 0
# else:
#     df['hammer'] = 0



print(df)