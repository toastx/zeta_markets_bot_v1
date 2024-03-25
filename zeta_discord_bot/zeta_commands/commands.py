import os
from zetamarkets_py.client import Client
from zetamarkets_py.types import Asset,OrderArgs, OrderOptions, Side
from solders.keypair import Keypair
import anchorpy
from dotenv import load_dotenv

load_dotenv()

d = {}
endpoint = os.getenv("ENDPOINT")


class Commands:

    async def details(privkey):
        wallet = anchorpy.Wallet(Keypair.from_base58_string(privkey))
        asset = Asset.SOL
        client = await Client.load(endpoint=endpoint, wallet=wallet, assets=[asset])
        summary = await client.get_account_risk_summary()
        return summary
    
    async def create_order(privkey):
        wallet = anchorpy.Wallet(Keypair.from_base58_string(privkey))
        asset = Asset.SOL
        client = await Client.load(endpoint=endpoint, wallet=wallet, assets=[asset])
        side = Side.Bid
        order = OrderArgs(price=0.1, size=0.1, side=side)
        msg = f"Placing {order.side} order: {order.size}x {str(asset)}-PERP @ ${order.price}"
        await client.place_orders_for_market(asset=asset, orders=[order])
        return msg

    async def view_order(privkey):
        string = ""
        wallet = anchorpy.Wallet(Keypair.from_base58_string(privkey))
        asset = Asset.SOL
        client = await Client.load(endpoint=endpoint, wallet=wallet, assets=[asset])
        open_orders = await client.fetch_open_orders(Asset.SOL)
        for order in open_orders:
            string+=(f"- {order.side.name} {order.info.size}x {str(asset)}-PERP @ ${order.info.price}")
        return string
    

        # print(f"Cancelling order with id: {open_orders[0].order_id}")
        # await client.cancel_order(Asset.SOL, order_id=open_orders[0].order_id, side=side)

    def store(uname,pkey):
        d[uname] = pkey
    
    def retrieve(uname):
        return d[uname]
    






