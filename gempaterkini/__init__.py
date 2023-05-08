import requests
import bs4

"""
Method = fungsi
Field / attribute = variable
Constructor = method yang dipanggil pertama kali saat object diciptakan, gunakan untuk
mendeklarasikan semua field pada class ini
Polymorphism = Aksi yang berbeda, dilakukan oleh pemnggilan method yang sama yang terjadi
karena perwarisan
"""

class Bencana:
    def __init__(self, url, description):
        self.description = description
        self.result = None
        self.url = url

    def tampilkan_keterangan(self):
        print(self.description)

    def ekstraksi_data(self):
        print('ekstraksi_data class banjir terkini')

    def tampilkan_data(self):
        print('tampilkan_data class banjir terkini')

    def run(self):
        self.ekstraksi_data()
        self.tampilkan_data()

class BanjirTerkini(Bencana):
    def __init__(self, url):
        super(BanjirTerkini, self).__init__(url,
                                            'NOT YET IMPLEMENTED')

    def tampilkan_keterangan(self):
        print(f'Under Construction{self.description}')

class GempaTerkini(Bencana):
    def __init__(self, url):
        super(GempaTerkini, self).__init__(url, 'Gempa Terkini dari BMKG')

    def ekstraksi_data(self):
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
            content = requests.get(self.url)
        except Exception:
            return None
        if content.status_code == 200:
            soup = bs4.BeautifulSoup(content.text,'html.parser') #1. INSTASIATION = Penciptaan object dari class
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
            self.result = hasil
        else:
            return None

    def tampilkan_data(self):
        if self.result is None:
            print("Tidak bisa menemukan data gempat terkini")
            return
        print('Gempa Terakhir berdasarkan BMKG')
        print(f"Tanggal: {self.result['tanggal']}")
        print(f"Waktu: {self.result['waktu']}")
        print(f"magnitudo: {self.result['magnitudo']}")
        print(f"kedalaman: {self.result['kedalaman']}")
        print(f"lokasi: {self.result['lokasi']}")
        print(f"koordinat: LS={self.result['koordinat']['ls']}, BT={self.result['koordinat']['bt']}")
        print(f"dirasakan: {self.result['dirasakan']}")

if __name__ == '__main__':
    gempa_di_indonesia = GempaTerkini('https://bmkg.go.id')
    gempa_di_indonesia.tampilkan_keterangan()
    gempa_di_indonesia.run()

    banjir_di_indonesia = BanjirTerkini('Not Yet')
    banjir_di_indonesia.tampilkan_keterangan()
    banjir_di_indonesia.run()


    daftar_bancana = []
    daftar_bancana.append(gempa_di_indonesia)
    daftar_bancana.append(banjir_di_indonesia)
    print('\nSemua Bencana yang ada')
    for becana in daftar_bancana:
        becana.tampilkan_keterangan()

