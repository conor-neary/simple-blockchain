# A simple transaction class for our blockchain
from datetime import datetime
from hashlib import sha256


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.time = datetime.now()
        self.id = sha256((str(self.sender) + str(self.recipient) +
                          str(self.amount) + str(self.time)).encode()).hexdigest()

    def __str__:
        return self.sender + ' to ' + self.recipient + ':' + self.amount + \
            ' at: ' + self.date
    
    def validate_tx(self):
        pass
