import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

from backend.blockchain.block import Block

pnconfig = PNConfiguration()

pnconfig.subscribe_key = "sub-c-22d6e76c-e625-11eb-97be-3ebc6f27b518"
pnconfig.publish_key = "pub-c-7a6d9c1e-c132-4853-b688-b3d5236e8b92"

pubnub = PubNub(pnconfig)

CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK'
}

# pubnub.subscribe().channels([TEST_CHANNEL, BLOCK_CHANNEL]).execute()


class Listener(SubscribeCallback):
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def message(self, pubnub, message_object):
        print(f'\n--Channel:{message_object.channel} | Message: {message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                print('\n -- Successfully replaced the local chain')
            except Exception as e:
                print(f'\n -- Did not replace chain: {e}')





class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """

    def __init__(self, blockchain):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain))

    def publish(self, channel, message):
        """

        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes.
        :param block:
        :return:
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())


def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(CHANNELS['TEST'], {'foo': 'bar'})


if __name__ == '__main__':
    main()
