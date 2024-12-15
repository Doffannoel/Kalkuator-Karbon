FAKTOR_EMISI_LISTRIK = 0.85  # kg CO2 per kWh
FAKTOR_EMISI_SAMPAH = {
    'Plastik': 2.5,  # kg CO2 per kg
    'Logam': 1.2,
    'Kaca': 0.9,
    'Kertas': 0.5,
}
FAKTOR_EMISI_BAHAN_BAKAR = {
    'Bensin': 2.3,  # kg CO2 per liter
    'Solar': 2.6,
    'LPG': 1.5,
    'Pertalite': 2.1,
    'Pertamax': 2.0,
    'Biodiesel': 1.8,
    'Ethanol': 1.5,
}

def hitung_emisi_listrik(daya, waktu):
    return (daya / 1000) * waktu * FAKTOR_EMISI_LISTRIK

def hitung_emisi_sampah(jenis, total):
    return FAKTOR_EMISI_SAMPAH.get(jenis, 0) * total

def hitung_emisi_bahan_bakar(jenis, total):
    return FAKTOR_EMISI_BAHAN_BAKAR.get(jenis, 0) * total
