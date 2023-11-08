import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_last_block()
        new_index = previous_block.index + 1
        new_timestamp = int(time.time())
        new_block = Block(new_index, previous_block.hash, new_timestamp, data)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def create_coin(self, recipient, amount):
        if amount <= 0:
            return False

        sender_balance = self.get_balance("system")
        if sender_balance < amount:
            return False

        self.add_block(f"Create {amount} coins for {recipient}")
        self.add_block(f"Transfer {amount} coins to {recipient}")
        return True

    def transfer_coin(self, sender, recipient, amount):
        if amount <= 0:
            return False

        sender_balance = self.get_balance(sender)
        if sender_balance < amount:
            return False

        self.add_block(f"Transfer {amount} coins from {sender} to {recipient}")
        return True

    def get_balance(self, user):
        balance = 0
        for block in self.chain:
            if "Create" in block.data and user in block.data:
                amount = int(block.data.split(" ")[1])
                balance += amount
            if "Transfer" in block.data and user in block.data:
                amount = int(block.data.split(" ")[1])
                if user == block.data.split("to ")[1]:
                    balance += amount
                if user == block.data.split("from ")[1]:
                    balance -= amount
        return balance

    def mine(self, difficulty):
        target = "0" * difficulty
        last_block = self.get_last_block()
        while last_block.hash[:difficulty] != target:
            new_index = last_block.index + 1
            new_timestamp = int(time.time())
            new_block = Block(new_index, last_block.hash, new_timestamp, f"Mined block {new_index}")
            last_block = new_block
        self.chain.append(last_block)
        print("Block mined:", last_block.hash)

if __name__ == "__main__":
    my_blockchain = Blockchain()
    my_blockchain.create_coin("Alice", 100)
    my_blockchain.transfer_coin("Alice", "Bob", 30)
    my_blockchain.mine(4)

    print("Blockchain is valid:", my_blockchain.is_valid())
