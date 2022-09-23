from django.db import models
from gdstorage.storage import GoogleDriveStorage
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

permission = GoogleDriveFilePermission(
   GoogleDrivePermissionRole.READER,
   GoogleDrivePermissionType.USER,
   "mailing.torche@gmail.com",
)
# Define Google Drive Storage
gd_storage = GoogleDriveStorage(permissions=(permission, ))

class RegistrationData(models.Model):
    nomor_invoice = models.CharField(max_length=254, unique=True)
    tanggal = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    nama_lengkap = models.CharField(max_length=254)
    nomor_telefon = models.CharField(max_length=254)
    program_studi = models.CharField(max_length=254)
    universitas = models.CharField(max_length=254)
    informasi_mengenai_torche = models.CharField(max_length=500)
    metode_pembelajaran = models.CharField(max_length=254)
    mata_kuliah = models.CharField(max_length=254)
    materi = models.TextField()
    aplikasi_simulasi = models.CharField(max_length=254)
    jumlah_sesi_yang_diikuti = models.CharField(max_length=254)
    jumlah_peserta = models.CharField(max_length=10)
    lampiran_file_siswa = models.FileField(upload_to='lampiran_siswa/%Y/%m/%d/', storage=gd_storage)
    lampiran_invoice = models.URLField(max_length=1000)
    lampiran_surat_tugas = models.URLField(max_length=1000)
    sesi_hari = models.TextField()
    sesi_jam = models.TextField()
    biaya = models.CharField(max_length=254)
    notes_for_tutor = models.TextField()
    referral_code = models.CharField(max_length=254)
    email_anggota_1 = models.CharField(max_length=1000)
    nama_lengkap_anggota_1 = models.CharField(max_length=1000)
    nomor_telefon_anggota_1 = models.CharField(max_length=1000)
    akun_discord_anggota_1 = models.CharField(max_length=1000)
    email_anggota_2 = models.CharField(max_length=1000)
    nama_lengkap_anggota_2 = models.CharField(max_length=1000)
    nomor_telefon_anggota_2 = models.CharField(max_length=1000)
    akun_discord_anggota_2 = models.CharField(max_length=1000)
    email_anggota_3 = models.CharField(max_length=1000)
    nama_lengkap_anggota_3 = models.CharField(max_length=1000)
    nomor_telefon_anggota_3 = models.CharField(max_length=1000)
    akun_discord_anggota_3 = models.CharField(max_length=1000)
    email_anggota_4 = models.CharField(max_length=1000)
    nama_lengkap_anggota_4 = models.CharField(max_length=1000)
    nomor_telefon_anggota_4 = models.CharField(max_length=1000)
    akun_discord_anggota_4 = models.CharField(max_length=1000)
    email_anggota_5 = models.CharField(max_length=1000)
    nama_lengkap_anggota_5 = models.CharField(max_length=1000)
    nomor_telefon_anggota_5 = models.CharField(max_length=1000)
    akun_discord_anggota_5 = models.CharField(max_length=1000)
    email_anggota_6 = models.CharField(max_length=1000)
    nama_lengkap_anggota_6 = models.CharField(max_length=1000)
    nomor_telefon_anggota_6 = models.CharField(max_length=1000)
    akun_discord_anggota_6 = models.CharField(max_length=1000)
    email_anggota_7 = models.CharField(max_length=1000)
    nama_lengkap_anggota_7 = models.CharField(max_length=1000)
    nomor_telefon_anggota_7 = models.CharField(max_length=1000)
    akun_discord_anggota_7 = models.CharField(max_length=1000)
    email_anggota_8 = models.CharField(max_length=1000)
    nama_lengkap_anggota_8 = models.CharField(max_length=1000)
    nomor_telefon_anggota_8 = models.CharField(max_length=1000)
    akun_discord_anggota_8 = models.CharField(max_length=1000)
    email_anggota_9 = models.CharField(max_length=1000)
    nama_lengkap_anggota_9 = models.CharField(max_length=1000)
    nomor_telefon_anggota_9 = models.CharField(max_length=1000)
    akun_discord_anggota_9 = models.CharField(max_length=1000)
    email_anggota_10 = models.CharField(max_length=1000)
    nama_lengkap_anggota_10 = models.CharField(max_length=1000)
    nomor_telefon_anggota_10 = models.CharField(max_length=1000)
    akun_discord_anggota_10 = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.nomor_invoice, self.nama_lengkap)

class ReferralCode(models.Model):
    referral_code = models.CharField(max_length=254)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.referral_code)