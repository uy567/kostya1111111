from web3 import Web3
import pandas as pd
import os

# Specify the path to the Excel file
excel_path = 'C:\\Users\\User\\Desktop\\Script\\Metamask_10000.xlsx'

# Load the Excel file
df = pd.read_excel(excel_path)

# Get private keys from the second column (assuming the first column is index 0)
private_keys = df.iloc[:, 1].dropna()  # Remove any NaN values

# Initialize Web3
web3 = Web3(Web3.HTTPProvider('https://rpc.holesky.ethpandaops.io'))

# Example: Use the first private key to perform operations
private_key = private_keys[0].strip()  # Trim any extra whitespace
account = web3.eth.account.from_key(private_key)
public_address = account.address

print("Using public address:", public_address)

# Further operations such as sending transactions, querying balances etc.
# Example of how to print account balance
balance = web3.eth.get_balance(public_address)
print("ETH Balance:", web3.fromWei(balance, 'ether'))

# If you need to interact with a contract, setup the contract instance
contract_address = '0xYourContractAddressHere'
contract_abi = 'YourContractABIHere'

contract = web3.eth.contract(address=contract_address, abi=contract_abi)
# Example of a contract call
# result = contract.functions.yourFunctionName().call()

# Example of sending a transaction
# nonce = web3.eth.getTransactionCount(public_address)
# txn = contract.functions.yourFunctionName().buildTransaction({
#     'chainId': 1,
#     'gas': 200000,
#     'gasPrice': web3.toWei('50', 'gwei'),
#     'nonce': nonce,
# })
# signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
# txn_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
# receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
# print("Transaction receipt:", receipt)
