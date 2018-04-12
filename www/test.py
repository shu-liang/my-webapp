import orm
from models import User,Blog,Comment
import asyncio, aiomysql

async def test():

    #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='c@123456',db='mywebappdb')

    #没有设置默认值的一个都不能少
    u = User(name='dflhuang', email='dflhuang@qq.com', passwd='0123', image='about:blank',id='110')

    await u.save()
	
    await orm.destory_pool()

# 获取EventLoop:
loop = asyncio.get_event_loop()

#把协程丢到EventLoop中执行
loop.run_until_complete(test())

#关闭EventLoop
loop.close()
