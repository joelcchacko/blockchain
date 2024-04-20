import hashlib

class CoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Ann sends 2"
t2 = "ron sends 1"
t3 = "rode sends 1"
t4 = "ollu sends 1"
t5 = "mike sends 3"

initial_block = CoinBlock("Initial string", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = CoinBlock(initial_block.block_data, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)


third_block = CoinBlock(second_block.block_data, [t5, t1])

print(third_block.block_data)
print(third_block.block_hash)
