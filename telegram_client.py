from telethon import TelegramClient as BaseTelegramClient
from telethon.sessions import Session


class TelegramClient(BaseTelegramClient):
    def __init__(
        self,
        session: str | Session,
        api_id: int,
        api_hash: str,
    ):
        super().__init__(session, api_id, api_hash)

    async def init(self):
        # Calling .connect() may raise a connection error False, so you need
        # to except those before continuing. Otherwise you may want to retry
        # as done here.
        print('Connecting to Telegram servers...')
        try:
            await self.connect()
        except IOError:
            # We handle IOError and not ConnectionError because
            # PySocks' errors do not subclass ConnectionError
            # (so this will work with and without proxies).
            print('Initial connection failed. Retrying...')
            await self.connect()

        # If the user hasn't called .sign_in() yet, they won't
        # be authorized. The first thing you must do is authorize. Calling
        # .sign_in() should only be done once as the information is saved on
        # the *.session file so you don't need to enter the code every time.
        if not await self.is_user_authorized():
            print('First run. Sending code request...')
            user_phone = input('Enter your phone: ')
            await self.sign_in(user_phone)

            self_user = None
            while self_user is None:
                code = input('Enter the code you just received: ')
                try:
                    self_user = await self.sign_in(code=code)

                # Two-step verification may be enabled, and .sign_in will
                # raise this error. If that's the case ask for the password.
                # Note that getpass() may not work on PyCharm due to a bug,
                # if that's the case simply change it for input().
                except SessionPasswordNeededError:
                    pw = getpass('Two step verification is enabled. '
                                 'Please enter your password: ')

                    self_user = await self.sign_in(password=pw)
