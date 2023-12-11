import asyncio

from web3 import Web3

from lesson_2.sdk.data.models import Networks
from lesson_2.sdk.client import Client

from eth_account import Account
import secrets

from private_data import private_key1, private_key2, private_key3, proxy

# todo: 1. сделать генератор приватников, 2. client.wallet.balance()
# todo: нужно сделать перебор private key и создание клиента



async def generate_private(private_keys, max_keys=100):
    for _ in range(max_keys):
        private_key = Account.create(secrets.token_bytes(32))._private_key
        private_keys.append(private_key.hex())
        await asyncio.sleep(0.1)

async def main():
    private_keys = []
    await generate_private(private_keys)

    for key in private_keys:
        client = Client(private_key=key, network=Networks.Ethereum, proxy=proxy)
        balance = await client.wallet.balance()
        print(f'balance: {balance} | private_key: {key} | address: {client.account.address}')

    # print(await client.wallet.balance(token_address='0xaf88d065e77c8cc2239327c5edb3a432268e5831'))
    # balance = await client.wallet.balance()
    # balance = await client.wallet.balance()
    # balance = await client.wallet.balance()

    '''
    token_address = Web3.to_checksum_address('0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8')

    tasks = []
    for private_key in [private_key1, private_key2, private_key3]:
        client = Client(private_key=private_key, network=Networks.Arbitrum)
        tasks.append(asyncio.create_task(client.wallet.balance(token_address=token_address)))

    await asyncio.gather(*tasks)
    await asyncio.wait([*tasks])

    for task in tasks:
        print(task.result())
    '''
    '''
    asyncio.gather() принимает список асинхронных задач (coroutines) в качестве аргументов и запускает их одновременно.
    Она возвращает список результатов, соответствующих выполненным задачам в том же порядке, в котором задачи были переданы в функцию.
    Если во время выполнения задачи возникает исключение, asyncio.gather() прекращает выполнение остальных задач и сразу же выбрасывает исключение.

    asyncio.wait() принимает список асинхронных задач (coroutines) в качестве аргументов и запускает их одновременно.
    Она возвращает кортеж из двух множеств: множество выполненных задач и множество невыполненных задач.
    Если во время выполнения задачи возникает исключение, asyncio.wait() продолжает выполнение остальных задач и не выбрасывает исключение.
    '''


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
