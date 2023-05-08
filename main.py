"""
Applikasi Deteksi Gempa terkini
"""
from datetime import datetime

from gempaterkini import GempaTerkini


today = datetime.now()

if __name__ == '__main__':
    print('Applikasi Utama')
    print(f'Current Time: {today}')
    gempa_di_indonesia = GempaTerkini('https://www.bmkg.go.id')
    gempa_di_indonesia.run()


