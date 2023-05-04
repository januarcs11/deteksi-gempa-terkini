import requests
from bs4 import BeautifulSoup

description = 'latest earthquake in Indonesia from BMKG'


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
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text,'html.parser')
        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        ls = None
        bt = None
        pusat = None
        kedalaman = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text

            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data gempat terkini")
        return
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"magnitudo: {result['magnitudo']}")
    print(f"kedalaman: {result['kedalaman']}")
    print(f"lokasi: {result['lokasi']}")
    print(f"koordinat: LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"dirasakan: {result['dirasakan']}")


if __name__ == '__main__':
    print('deskripsi Package', description)
    print('Ini Adalah package gempa terkini')
    print('hai')