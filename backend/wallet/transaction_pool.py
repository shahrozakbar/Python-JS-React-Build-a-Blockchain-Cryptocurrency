class TransactionPool:
    def __init__(self):
        self.transaction_map = {}

    def set_transaction(self, transaction):
        """

        Set a transaction in the transaction pool.
        :param transaction:
        :return:
        """
        self.transaction_map[transaction.id] = transaction

    def existing_transaction(self, address):

        """
        Find a transaction generated by the address in the trasaction pool
        :param address:
        :return:
        """

        for transaction in self.transaction_map.values():
            if transaction.input['address'] == address:
                return transaction

    def transaction_data(self):
        """
        Return the transaction of the  transaction pool represented in there
        json serialized form.
        :return:
        """

        return list(map(
            lambda transaction: transaction.to_json(),
            self.transaction_map.values()
        ))
