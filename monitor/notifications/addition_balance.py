from apprise.Apprise import Apprise
from monitor.database import async_session
from monitor.database.queries import get_addition_balance
from monitor.format import *
from monitor.notifications.notification import Notification


class AdditionBalanceNotification(Notification):
    last_balance: int

    def __init__(self, apobj: Apprise) -> None:
        super().__init__(apobj)
        self.last_balance: int = None

    async def condition(self) -> bool:

        async with async_session() as db_session:
           self.new_balance = await get_addition_balance(db_session)
                       
        if self.last_balance is not None and self.new_balance is not None and self.new_balance > self.last_balance:            
            return True
        else:
            self.last_balance = self.new_balance
            return False

    async def trigger(self) -> None:
        self.addition_new_balance = int(self.new_balance) - int(self.last_balance)
        self.balance_baru = int(self.new_balance)/1000000000000
        self.balance_akhir = int(self.last_balance)/1000000000000
        self.last_balance = self.new_balance
        return self.apobj.notify(title='** 💰 Balance Bertambah 💰 **',
           body="Wallet Balance Bertambah\n" +
           f"New: {self.balance_baru} XCH\n" + 
           f"Prev: {self.balance_akhir} XCH\n" +
           f"Addition: {self.addition_new_balance} mojo")
