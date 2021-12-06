import pyupbit

#업비트 open API code
access = "cB46UIiQet2DrsD1ycq2RLZ85BWFylv9nxTJgP5K"          # 본인 값으로 변경
secret = "kSKGzwgD8Qq6ESNVcWdNRQDUxAlCOI0X2x505fXH"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
