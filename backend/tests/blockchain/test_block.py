from backend.blockchain.block import Block

def test_mine_block():
    last_block = Block.genesis()
    data = 'test-data'
    block = Block.mine_block(last_block,data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == data
