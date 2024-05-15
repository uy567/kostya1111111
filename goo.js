const metamaskWalletAddress = '0xe1f34862a8fc1011e394bb28c316de30d27e1cd1';

const faucetUrl = 'https://blastapi.io/faucets/ethereum-holesky';

const requestData = {
    address: metamaskWalletAddress,
    amount: '00025',
    symbol: 'hETH'
};

async function requestTokens() {
    try {
        const response = await fetch(faucetUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        });
        const data = await response.json();
        console.log('Токены успешно запрошены:', data);
    } catch (error) {
        console.error('Ошибка при запросе токенов:', error);
    }
}

requestTokens();
