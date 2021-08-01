class TransactionPool:
    def __init__(self):
        self.transaction_map = {}

    def set_transaction(self, transaction):
        """

        Set a transaction in the transaction pool.
        :param transaction:
        :return:
        """
        self.transaction_map[transaction.id]  = transaction