"""
Applikasi Deteksi Gempa terkini
"""
from datetime import datetime

import gempaterkini
from gempaterkini import ekstraksi_data, tampilkan_data

today = datetime.now()

if __name__ == '__main__':
    print(f'Info Gempa terkini {gempaterkini.description}')
    print('Applikasi Utama')
    print(f'Current Time: {today}')
    result = ekstraksi_data()
    tampilkan_data(result)