import os
import csv
import http.client
import json
import time
from retrying import retry

def create_wallet(api_key):
    @retry(wait_fixed=1000, stop_max_attempt_number=10)
    def _create_wallet():
        conn = http.client.HTTPSConnection("core.pirichain.com")
        payload = 'language=english'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        conn.request("POST", "/createNewAddress", payload, headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        conn.close()

        wallet_data = json.loads(data)

        if 'pub' in wallet_data:
            return wallet_data
        else:
            print(f"Error: 'pub' key not found in wallet data.")
            raise Exception("Pub key not found in wallet data.")

    try:
        return _create_wallet()
    except Exception as e:
        print(f"Error creating wallet: {e}")
        return None

def save_to_csv(wallet, filename):
    header = ['Alamat', 'Kunci Pribadi', 'Kunci Publik', 'Mnemonic']
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(header)
        writer.writerow([wallet['pub'], wallet['pri'], wallet['publicKey'], wallet['words']])

def display_wallet_info(wallet, index):
    print(f"Dompet {index + 1} berhasil dibuat:")
    print(f"Alamat: {wallet['pub']}")
    print(f"Kunci Pribadi: {wallet['pri']}")
    print(f"Kunci Publik: {wallet['publicKey']}")
    print(f"Mnemonic: {wallet['words']}")
    print("\n")

api_key = "7989-tsjd-9750-eead"

num_wallets = int(input("Masukkan jumlah dompet yang ingin dibuat: "))
csv_filename = "wallets.csv"

for i in range(num_wallets):
    wallet_data = create_wallet(api_key)
    if wallet_data:
        display_wallet_info(wallet_data, i)
        save_to_csv(wallet_data, csv_filename)
    else:
        print(f"Melewati dompet {i + 1} karena terjadi kesalahan.")

    print(f"Progres: {i + 1}/{num_wallets} ({((i + 1) / num_wallets) * 100:.1f}%)")
    time.sleep(1)
    
    os.system('clear')  
