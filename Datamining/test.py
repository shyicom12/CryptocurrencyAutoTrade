import pyupbit

#업비트 open API code
access = "accese key"          # 본인 값으로 변경
secret = "secret key"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
