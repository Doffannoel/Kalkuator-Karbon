from django.shortcuts import render
from .forms import ListrikForm, SampahForm, BahanBakarForm
from .utils import hitung_emisi_listrik, hitung_emisi_sampah, hitung_emisi_bahan_bakar
import logging

def kalkulator(request):
    logger = logging.getLogger(__name__)  # Gunakan logger
    hasil = []
    total_emisi = 0

    # Log data POST yang diterima
    logger.info(f"POST data: {request.POST}")

    # Buat instance form dengan prefix (untuk GET request)
    listrik_form = ListrikForm(prefix='listrik')
    sampah_form = SampahForm(prefix='sampah')
    bahan_bakar_form = BahanBakarForm(prefix='bahan_bakar')

    if request.method == 'POST':
        # Validasi ListrikForm dengan prefix
        if 'listrik-daya' in request.POST or 'listrik-waktu' in request.POST:
            listrik_form = ListrikForm(request.POST, prefix='listrik')
            logger.info("Validating ListrikForm...")
            if listrik_form.is_valid():
                logger.info("ListrikForm is valid.")
                daya = listrik_form.cleaned_data.get('daya')
                waktu = listrik_form.cleaned_data.get('waktu')
                logger.info(f"Cleaned data from ListrikForm - Daya: {daya}, Waktu: {waktu}")
                if daya and waktu:
                    emisi_listrik = hitung_emisi_listrik(daya, waktu)
                    total_emisi += emisi_listrik
                    hasil.append(f"Emisi dari Peralatan Listrik: {emisi_listrik:.4f} kg CO₂")
            else:
                logger.warning(f"ListrikForm errors: {listrik_form.errors}")

        # Validasi SampahForm dengan prefix
        if 'sampah-total' in request.POST and 'sampah-jenis' in request.POST:
            sampah_form = SampahForm(request.POST, prefix='sampah')
            logger.info("Validating SampahForm...")
            if sampah_form.is_valid():
                logger.info("SampahForm is valid.")
                jenis = sampah_form.cleaned_data.get('jenis')
                total = sampah_form.cleaned_data.get('total')
                logger.info(f"Cleaned data from SampahForm - Jenis: {jenis}, Total: {total}")
                if jenis and total:
                    emisi_sampah = hitung_emisi_sampah(jenis, total)
                    total_emisi += emisi_sampah
                    hasil.append(f"Emisi dari Sampah: {emisi_sampah:.4f} kg CO₂")
            else:
                logger.warning(f"SampahForm errors: {sampah_form.errors}")

        # Validasi BahanBakarForm dengan prefix
        if 'bahan_bakar-total' in request.POST and 'bahan_bakar-jenis' in request.POST:
            bahan_bakar_form = BahanBakarForm(request.POST, prefix='bahan_bakar')
            logger.info("Validating BahanBakarForm...")
            if bahan_bakar_form.is_valid():
                logger.info("BahanBakarForm is valid.")
                jenis = bahan_bakar_form.cleaned_data.get('jenis')
                total = bahan_bakar_form.cleaned_data.get('total')
                logger.info(f"Cleaned data from BahanBakarForm - Jenis: {jenis}, Total: {total}")
                if jenis and total:
                    emisi_bahan_bakar = hitung_emisi_bahan_bakar(jenis, total)
                    total_emisi += emisi_bahan_bakar
                    hasil.append(f"Emisi dari Bahan Bakar: {emisi_bahan_bakar:.4f} kg CO₂")
            else:
                logger.warning(f"BahanBakarForm errors: {bahan_bakar_form.errors}")

    return render(request, 'kalkulator/kalkulator.html', {
        'listrik_form': listrik_form,
        'sampah_form': sampah_form,
        'bahan_bakar_form': bahan_bakar_form,
        'hasil': hasil,
        'total_emisi': total_emisi,
    })


    