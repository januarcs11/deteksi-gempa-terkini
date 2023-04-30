"""
Applikasi Deteksi Gempa terkini
"""
from datetime import datetime
from gempaterkini import ekstraksi_data, tampilkan_data

today = datetime.now()

if __name__ == '__main__':
    print('Applikasi Utama')
    print(f'Current Time: {today}')
    result = ekstraksi_data()
    tampilkan_data(result)