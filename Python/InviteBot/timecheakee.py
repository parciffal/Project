import datetime
import asyncio
import db


async def time_cheak(wait_for):
    try:
        now = datetime.datetime.now().date().isoformat()
        dsa = db.DataConn()
        expire = dsa.get_expire()
        for dt in expire:
            kld = (dt[0] == now)
            print(kld)
            if kld:
                print('fuck: ' + str(dt[1]))
            else:
                print('ok')

        await asyncio.sleep(wait_for)
    except Exception as e:
        print(repr(e) + 'Time cheaker')
    finally:
        print("Operation finished")


