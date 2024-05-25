import redis



class REDIS:
    def __init__(self):
        self.bd = redis.Redis(
            host='redis-17449.c308.sa-east-1-1.ec2.redns.redis-cloud.com',
            port=17449,
            password='3LL6YA3wPftbTonEKQJBD2SC6ajFsrP1'
        )

    def expire(self, key, seconds: int):
        self.bd.expire(key, seconds)
    
    def get(self, key) -> any:
        return self.bd.get(key)
    
    def set(self, key, val):
        self.bd.set(key, val)
    
    def delete(self, key):
        self.bd.delete(key)
    
    def exists(self, key: str) -> bool:
        return False if self.bd.get(key) is None else True

# redisbd = REDIS()
# redisbd["teste"] = 3
# print(redisbd["teste"])
# print("teste" in redisbd)