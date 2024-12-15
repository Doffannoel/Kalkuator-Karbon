from django import forms

class ListrikForm(forms.Form):
    jenis = forms.ChoiceField(
        choices=[
            ('Lampu LED', 'Lampu LED'),
            ('AC 1 PK', 'AC 1 PK'),
            ('Kulkas', 'Kulkas')
        ],
        label='Jenis Peralatan Listrik',
        required=False  # Tidak wajib diisi
    )
    daya = forms.FloatField(label='Daya (Watt)', required=False)
    waktu = forms.FloatField(label='Waktu (Jam)', required=False)

    def clean(self):
        cleaned_data = super().clean()
        jenis = cleaned_data.get('jenis')
        daya = cleaned_data.get('daya')
        waktu = cleaned_data.get('waktu')

        # Validasi hanya jika salah satu field terkait listrik diisi
        if jenis or daya or waktu:
            if not daya or not waktu:
                raise forms.ValidationError(
                    "Jika Anda ingin menghitung emisi listrik, daya dan waktu harus diisi."
                )
        return cleaned_data


class SampahForm(forms.Form):
    jenis = forms.ChoiceField(
        choices=[
            ('Plastik', 'Sampah Plastik'),
            ('Logam', 'Logam'),
            ('Kaca', 'Kaca'),
            ('Kertas', 'Kertas')
        ],
        required=False
    )
    total = forms.FloatField(label='Total (Kg)', required=False)

    def clean(self):
        cleaned_data = super().clean()
        jenis = cleaned_data.get('jenis')
        total = cleaned_data.get('total')

        # Validasi hanya jika salah satu field terkait sampah diisi
        if jenis or total:
            if not jenis or not total:
                raise forms.ValidationError(
                    "Jika Anda ingin menghitung emisi sampah, jenis dan total harus diisi."
                )
        return cleaned_data


class BahanBakarForm(forms.Form):
    jenis = forms.ChoiceField(
        choices=[
            ('Bensin', 'Bensin'),
            ('Solar', 'Solar'),
            ('LPG', 'LPG'),
            ('Pertalite', 'Pertalite'),
            ('Pertamax', 'Pertamax'),
            ('Biodiesel', 'Biodiesel'),
            ('Ethanol', 'Ethanol'),
        ],
        required=False
    )
    total = forms.FloatField(label='Total (Liter)', required=False)

    def clean(self):
        cleaned_data = super().clean()
        jenis = cleaned_data.get('jenis')
        total = cleaned_data.get('total')

        # Validasi hanya jika salah satu field terkait bahan bakar diisi
        if jenis or total:
            if not jenis or not total:
                raise forms.ValidationError(
                    "Jika Anda ingin menghitung emisi bahan bakar, jenis dan total harus diisi."
                )
        return cleaned_data

