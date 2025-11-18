class PaketLiburan:
    def _init_(self, nama, harga, kesenangan):
        self.nama = nama
        self.harga = harga
        self.kesenangan = kesenangan
        self.rasio = kesenangan / harga  # Kunci Greedy!

def greedy_pilih_paket(paket_list, budget):
    # STEP 1: Sorting berdasarkan rasio (DESC)
    paket_sorted = sorted(paket_list, 
                         key=lambda x: x.rasio, 
                         reverse=True)
    
    paket_terpilih = []
    total_harga = 0
    total_kesenangan = 0
    
    # STEP 2: Iterasi & pilih paket
    for paket in paket_sorted:
        if total_harga + paket.harga <= budget:
            paket_terpilih.append(paket)
            total_harga += paket.harga
            total_kesenangan += paket.kesenangan
    
    return paket_terpilih, total_harga, total_kesenangan