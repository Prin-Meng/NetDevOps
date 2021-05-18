import hvac

client = hvac.Client(
    url='https://192.168.0.166:8200',
    token="s.SmqXBFAZPmIIRN0rqpzsPc13",  # 使用权限被控制的令牌
    # token="s.WcsuqUPtTGUQc75oFj4PWc0N",  # 管理员令牌
    verify="/opt/certs/ca.pem"
)

# 是否认证
# print(client.is_authenticated())

# 是否解锁
# print(client.sys.is_sealed())
