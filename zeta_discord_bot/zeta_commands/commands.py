import os
import solathon
from zetamarkets_py.client import Client
from zetamarkets_py.types import Asset,OrderArgs, OrderOptions, Side

d = {}
endpoint = os.getenv("ENDPOINT", "https://api.mainnet-beta.solana.com")

class Commands:
    
    async def details(privkey):
        
        wallet = solathon.Keypair.from_private_key(privkey)
        asset = Asset.SOL
        client = await Client.load(endpoint=endpoint, wallet=wallet, assets=[asset])
        summary = await client.get_account_risk_summary()
        return summary
    
    
    
    async def create_order(privkey):
        lst = []
        wallet = solathon.Keypair.from_private_key(privkey)
        asset = Asset.SOL
        client = await Client.load(endpoint=endpoint, wallet=wallet.private_key, assets=[asset])
        side = Side.Bid
        order = OrderArgs(price=0.1, size=0.1, side=side)
        print(f"Placing {order.side} order: {order.size}x {str(asset)}-PERP @ ${order.price}")
        await client.place_orders_for_market(asset=asset, orders=[order])
        open_orders = await client.fetch_open_orders(Asset.SOL)
        for order in open_orders:
            lst.append(f"- {order.side.name} {order.info.size}x {str(asset)}-PERP @ ${order.info.price}")
        return lst


        # print(f"Cancelling order with id: {open_orders[0].order_id}")
        # await client.cancel_order(Asset.SOL, order_id=open_orders[0].order_id, side=side)

    def store(uname,pkey):
        d[uname] = pkey
    
    def retrieve(uname):
        return d[uname]
    






