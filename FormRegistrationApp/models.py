from django.db import models

class RegistrationData(models.Model):
    nomor_invoice = models.CharField(max_length=254, unique=True)
    tanggal = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    nama_lengkap = models.CharField(max_length=254)
    nomor_telefon = models.CharField(max_length=254)
    program_studi = models.CharField(max_length=254)
    universitas = models.CharField(max_length=254)
    informasi_mengenai_torche = models.CharField(max_length=254)
    metode_pembelajaran = models.CharField(max_length=254)
    mata_kuliah = models.CharField(max_length=254)
    materi = models.CharField(max_length=5000)
    aplikasi_simulasi = models.CharField(max_length=254)
    jumlah_sesi_yang_diikuti = models.CharField(max_length=254)
    jumlah_peserta = models.CharField(max_length=10)
    nama_anggota_kelompok = models.CharField(max_length=2000)
    email_anggota_kelompok = models.CharField(max_length=2000)
    sesi_materi = models.CharField(max_length=2000)
    sesi_tanggal = models.CharField(max_length=2000)
    sesi_jam = models.CharField(max_length=2000)
    biaya = models.CharField(max_length=254)
    notes_for_tutor = models.CharField(max_length=5000)
    referral_code = models.CharField(max_length=254)
    file_upload = models.FileField(upload_to='documents/%Y/%m/%d')

class ReferralCode(models.Model):
    referral_code = models.CharField(max_length=254)