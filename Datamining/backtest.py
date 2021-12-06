import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-BTC", count=7) #OHLCV(open, high, low, close, volume)
df['range'] = (df['high'] - df['low']) * 0.5 #변동폭 * k 계산, (고가-저가)*k
df['target'] = df['open'] + df['range'].shift(1) #매수가(target), range column을 한칸씩 밑으로 내린다(shift)

fee = 0.0032
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")