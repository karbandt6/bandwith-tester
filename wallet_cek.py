import sys
import os
import subprocess
import requests
from web3 import Web3
from eth_utils import to_checksum_address

def clear_screen():
    os.system('clear')
def select_network():
    networks = {
        "1": ('BSC', 'https://go.getblock.io/4d1955bd78c341549bc9f2203f2e7eb7'),
        "2": ('MATIC', 'https://polygon-mainnet.nodereal.io/v1/c4061697a2bf4e52bed857cd295148cc'),
        "3": ('ETH', 'https://eth-mainnet.nodereal.io/v1/c4061697a2bf4e52bed857cd295148cc'),
        "4": ('HECO', 'https://http-mainnet-node.huobichain.com'),
        "5": ('AVAX', 'https://open-platform.nodereal.io/c4061697a2bf4e52bed857cd295148cc/avalanche-c/ext/bc/C/rpc'),
        "6": ('BASE', 'https://open-platform.nodereal.io/c4061697a2bf4e52bed857cd295148cc/base'),
        "7": ('ARB', 'https://open-platform.nodereal.io/c4061697a2bf4e52bed857cd295148cc/arbitrum-nitro/'),
        "8": ('FTM', 'https://fantom.publicnode.com'),
        "9": ('KLAY', 'https://open-platform.nodereal.io/c4061697a2bf4e52bed857cd295148cc/klaytn/'),
        "10": ('CRO', 'https://cronos-evm.publicnode.com/'),
    }
    print("Select network:")
    for key, (name, _) in networks.items():
        print(f"{key}. {name}")
    choice = input("Enter your network: ")    
    selected_network = networks.get(choice)
    if selected_network:
        return selected_network
    else:
        print("Invalid choice. Defaulting to Binance Smart Chain (BSC).")
        return networks["1"]
raw_github_url = 'https://raw.githubusercontent.com/karbandt6/bandwith-tester/main/list_wallet.txt'
try:
    response = requests.get(raw_github_url)
    response.raise_for_status()
    wallets = response.text.splitlines()
    wallets = [wallet.strip() + '\n' for wallet in wallets]
    print(f'Jumlah wallet = {len(wallets)}')
except requests.exceptions.RequestException as e:
    print(f'Error fetching wallet addresses: {e}')
if os.path.exists('hasil_cek.txt'):
    os.remove('hasil_cek.txt')
clear_screen()
network_name, network_url = select_network()
web3 = Web3(Web3.HTTPProvider(network_url))
contract_address = input('Masukkan contract address: ')
with open('r.txt') as r:
    wallets = r.readlines()
wallets = [wallet.strip() + '\n' for wallet in wallets]
print(f'Jumlah wallet = {len(wallets)}')
abijson = '''[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"sender","type":"address"},{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]'''
contract = web3.eth.contract(address=to_checksum_address(contract_address), abi=abijson)
print('Hasil cek disimpan ke file hasil_cek.txt\nCreated By NFB Team . . .')
print('')
total_balance = 0
token_decimals = contract.functions.decimals().call()  # Fetch token decimals
token_name = contract.functions.name().call()
token_symbol = contract.functions.symbol().call()
with open('hasil_cek.txt', 'a') as f:
    wallets_with_balance = 0
    for idx, addr in enumerate(wallets, 1):
        try:
            checksummed_address = to_checksum_address(addr.strip())
            balance = contract.functions.balanceOf(checksummed_address).call()
            formatted_balance = f'{balance / (10 ** token_decimals):,.{token_decimals}f}'.replace(',', '.').rstrip('0').rstrip('.')
            formatted_total_balance = f'{total_balance / (10 ** token_decimals):,.{token_decimals}f}'.replace(',', '.').rstrip('0').rstrip('.')            
            print(f'Progress: {idx}/{len(wallets)} | Dompet ditemukan: {wallets_with_balance} | Total saldo: {formatted_total_balance} {token_symbol}', end='\r')             
            if balance > 0:
                wallets_with_balance += 1
                f.write(f'{checksummed_address}\n')
                f.flush()
                os.fsync(f.fileno())               
                total_balance += balance
        except Exception as e:
            print(f'Error processing wallet: {e}')
formatted_total_balance = f'{total_balance / (10 ** token_decimals):,.{token_decimals}f}'.replace(',', '.').rstrip('0').rstrip('.')
print(f'\n\nProgress: {idx}/{len(wallets)} | wallet found: {wallets_with_balance} | Total balance: {formatted_total_balance} {token_symbol}')
print('Selesai!')
telegram_bot_token = "6469382312:AAEWSH8qybPY1EdTo2nRqa3fIUp3q1evMvs"
telegram_chat_id = "5072815782"
file_path = "/root/hasil_cek.txt"
custom_header = f"────────────────────────\n🚀 𝙍𝙚𝙨𝙪𝙡𝙩𝙨 𝙊𝙛 𝙔𝙤𝙪𝙧 𝘼𝙨𝙨𝙚𝙩𝙨 🚀\n────────────────────────"
telegram_message = f'\`\`\`𝗡𝗼𝗱𝗲.𝗷𝘀\n\n{custom_header}\n\n📊 𝙋𝙧𝙤𝙜𝙧𝙚𝙨𝙨: {idx}/{len(wallets)}\n🌐 𝙉𝙚𝙩𝙬𝙤𝙧𝙠: {network_name}\n🔎 𝙒𝙖𝙡𝙡𝙚𝙩𝙨 𝙁𝙤𝙪𝙣𝙙: {wallets_with_balance}\n💰 𝙏𝙤𝙩𝙖𝙡 𝘽𝙖𝙡𝙖𝙣𝙘𝙚: {formatted_total_balance} {token_symbol}\n\n🎉 𝙃𝙖𝙫𝙚 𝘼 𝙉𝙞𝙘𝙚 𝘿𝙖𝙮\n────────────────────────\n\`\`\`'
telegram_command = f'curl -s -X POST "https://api.telegram.org/bot{telegram_bot_token}/sendMessage" -d "chat_id={telegram_chat_id}" -d "text={telegram_message}" -d "parse_mode=MarkdownV2"> /dev/null 2>&1'
subprocess.run(telegram_command, shell=True)
curl_command = f'curl -s -X POST "https://api.telegram.org/bot{telegram_bot_token}/sendDocument" -F chat_id={telegram_chat_id} -F document=@{file_path}> /dev/null 2>&1'
subprocess.run(curl_command, shell=True)
print('Notifikasi dan dokumen telah dikirim ke bot Telegram.')
