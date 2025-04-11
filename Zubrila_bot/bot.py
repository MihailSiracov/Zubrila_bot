import asyncio
import logging
from loader import *

import handlers.users.start_and_reg
import handlers.users.reg
import handlers.users.log_out
import handlers.users.lesson_with_personal_db

async def main():
    scheduler.start()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
