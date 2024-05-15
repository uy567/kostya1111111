import requests

def request_holesky_tokens(wallets):
    # Замените на свой API ключ и адрес контракта токена
    api_key = 'DFXUR1MNHGBEXX22IUY5DUVRIQRGZF1RS5'
    token_contract_address = '0x0e79065B5F11b5BD1e62B935A600976ffF3754B9'
    api_url = 'https://faucet.chainstack.com/holesky-testnet-faucet'

    for wallet in wallets:
        params = {
            'module': 'account',
            'action': 'tokenbalance',
            'contractaddress': token_contract_address,
            'address': wallet,
            'tag': 'latest',
            'apikey': api_key
        }
        response = requests.get(api_url, params=params)
        data = response.json()
        if data['status'] == '1':
            balance = int(data['result']) / 10**18  # Преобразование баланса из wei в ETH
            print(f"Баланс токенов для адреса {wallet}: {balance} ETH")
        else:
            print(f"Ошибка при запросе баланса для адреса {wallet}: {data['message']}")

if __name__ == "__main__":
    # Список адресов кошельков, для которых вы хотите запросить тестовые токены
    wallets = [
        "0xe1f34862a8fc1011e394bb28c316de30d27e1cd1",
        "0x227a14163b0bd6a9a6f781bcc3db8d1666378abc",
        "0x93fc7eccb723a0a00b312a81b8cbfc24e187c117",
        # Добавьте другие адреса по мере необходимости
    ]
    request_holesky_tokens(wallets)
