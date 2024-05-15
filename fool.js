const { ethers } = require("ethers");

async function requestTestTokens() {
    // Подключение к сети Ethereum через MetaMask
    await window.ethereum.enable();
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    
    // Адрес контракта токена ETH и ABI контракта
    const tokenContractAddress = "0xTokenContractAddress";
    const tokenContractABI = [ /* ABI контракта */ ];

    // Создание экземпляра контракта
    const tokenContract = new ethers.Contract(tokenContractAddress, tokenContractABI, provider);

    // Вызов метода контракта для запроса тестовых токенов
    const recipientAddress = "0xRecipientAddress";
    const amount = ethers.utils.parseEther("10"); // Запрашиваемое количество токенов
    const transaction = await tokenContract.transfer(recipientAddress, amount);

    // Отправка транзакции через MetaMask
    await transaction.wait();
    console.log("Тестовые токены отправлены успешно.");
}

// Вызов функции для запроса тестовых токенов
requestTestTokens();
