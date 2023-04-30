"""
Applikasi Deteksi Gempa terkini
"""


def ekstraksi_data():
    """
    Tanggal : 30 April 2023,
    Waktu : 08:26:35 WIB
    Magnitudo : 5.0
    Kedalaman: 10 km
    Lokasi: 4.78 LS  133.86 BT

    Pusat GempaL 116 km BaratLaut KEP.ARU-MALUKU
    Keterangan: tidak berpotensi TSUNAMI
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '30 April 2023'
    hasil['waktu'] = '08:26:35 WIB'
    hasil['magnitudo'] = 5.0
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'ls': 4.78, 'bt': 133.86}
    hasil['keterangan'] = 'tidak berpotensi TSUNAMI'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"magnitudo: {result['magnitudo']}")
    print(f"kedalaman: {result['kedalaman']}")
    print(f"lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"keterangan: {result['keterangan']}")



if __name__ == '__main__':
    print('Applikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)