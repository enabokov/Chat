import asyncio
from functools import wraps

from asyncpg.pool import Pool


def retry(times):
    def _retry(method):
        @wraps(method)
        async def _call(*args, **kwargs):
            _times = times
            if isinstance(_times, str) and _times == 'forever':
                _times = 30

            for attempt in range(_times):
                print(f'Attempt to {method.__name__}: {attempt}')
                await asyncio.sleep(1)
                try:
                    result = await method(*args, **kwargs)
                    print(f'Connected! {result}')
                    if isinstance(result, Pool):
                        return result
                except:  # noqa
                    pass
            return None
        return _call
    return _retry
