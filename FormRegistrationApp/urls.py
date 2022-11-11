from django.urls import path
from . import views
import datetime
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home_view, name="register"),

    path("metode-pembelajaran/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/", views.metode_pembelajaran, name="metode_pembelajaran"),

    path("mata-kuliah/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/", views.mata_kuliah, name="mata_kuliah"),
    
    path("session-cce/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_cce, name="session_cce"),
    path("session-cem/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_cem, name="session_cem"),
    path("session-cet/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_cet, name="session_cet"),
    path("session-cps/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_cps, name="session_cps"),
    path("session-cre/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_cre, name="session_cre"),
    path("session-eec/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_eec, name="session_eec"),
    path("session-fac/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_fac, name="session_fac"),
    path("session-fca/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_fca, name="session_fca"),
    path("session-fch/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_fch, name="session_fch"),
    path("session-fht/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_fht, name="session_fht"),
    path("session-fmt/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_fmt, name="session_fmt"),
    path("session-fpm/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_fpm, name="session_fpm"),
    path("session-fp1/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_fp1, name="session_fp1"),
    path("session-fp2/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_fp2, name="session_fp2"),
    path("session-meb/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_meb, name="session_meb"),
    path("session-nce/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_nce, name="session_nce"),
    path("session-oce/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_oce, name="session_oce"),
    path("session-pcd/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_pcd, name="session_pcd"),
    path("session-pch/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_pch, name="session_pch"),
    path("session-pdd/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_pdd, name="session_pdd"),
    path("session-ped/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_ped, name="session_ped"),
    path("session-spr/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_spr, name="session_spr"),
    path("session-ppd/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_ppd, name="session_ppd"),
    path("session-tph/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>", views.session_tph, name="session_tph"),

    # path("lampiran/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>/<materi>/<simulasi>/", views.lampiran, name="lampiran"),

    path("jumlah-peserta/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>/<materi>/<simulasi>/", views.jumlah_peserta, name="jumlah_peserta"),

    path("anggota-kelompok_1/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>/<materi>/<simulasi>/<jumlah_peserta>/", views.anggota_kelompok_1, name="anggota_kelompok_1"),
    path("anggota-kelompok_2/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>/<materi>/<simulasi>/<jumlah_peserta>/<email_1>/<nama_lengkap_1>/<nomor_telefon_1>/<akun_discord_1>/", views.anggota_kelompok_2, name="anggota_kelompok_2"),
    path("anggota-kelompok_3/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>/<materi>/<simulasi>/<jumlah_peserta>/<email_1>/<nama_lengkap_1>/<nomor_telefon_1>/<akun_discord_1>/<email_2>/<nama_lengkap_2>/<nomor_telefon_2>/<akun_discord_2>/", views.anggota_kelompok_3, name="anggota_kelompok_3"),
    path("anggota-kelompok_4/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>/<materi>/<simulasi>/<jumlah_peserta>/<email_1>/<nama_lengkap_1>/<nomor_telefon_1>/<akun_discord_1>/<email_2>/<nama_lengkap_2>/<nomor_telefon_2>/<akun_discord_2>/<email_3>/<nama_lengkap_3>/<nomor_telefon_3>/<akun_discord_3>/", views.anggota_kelompok_4, name="anggota_kelompok_4"),
    path("anggota-kelompok_5/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>/<materi>/<simulasi>/<jumlah_peserta>/<email_1>/<nama_lengkap_1>/<nomor_telefon_1>/<akun_discord_1>/<email_2>/<nama_lengkap_2>/<nomor_telefon_2>/<akun_discord_2>/<email_3>/<nama_lengkap_3>/<nomor_telefon_3>/<akun_discord_3>/<email_4>/<nama_lengkap_4>/<nomor_telefon_4>/<akun_discord_4>/", views.anggota_kelompok_5, name="anggota_kelompok_5"),
    path("anggota-kelompok_6/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>/<materi>/<simulasi>/<jumlah_peserta>/<email_1>/<nama_lengkap_1>/<nomor_telefon_1>/<akun_discord_1>/<email_2>/<nama_lengkap_2>/<nomor_telefon_2>/<akun_discord_2>/<email_3>/<nama_lengkap_3>/<nomor_telefon_3>/<akun_discord_3>/<email_4>/<nama_lengkap_4>/<nomor_telefon_4>/<akun_discord_4>/<email_5>/<nama_lengkap_5>/<nomor_telefon_5>/<akun_discord_5>/", views.anggota_kelompok_6, name="anggota_kelompok_6"),
    path("anggota-kelompok_7/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>/<materi>/<simulasi>/<jumlah_peserta>/<email_1>/<nama_lengkap_1>/<nomor_telefon_1>/<akun_discord_1>/<email_2>/<nama_lengkap_2>/<nomor_telefon_2>/<akun_discord_2>/<email_3>/<nama_lengkap_3>/<nomor_telefon_3>/<akun_discord_3>/<email_4>/<nama_lengkap_4>/<nomor_telefon_4>/<akun_discord_4>/<email_5>/<nama_lengkap_5>/<nomor_telefon_5>/<akun_discord_5>/<email_6>/<nama_lengkap_6>/<nomor_telefon_6>/<akun_discord_6>/", views.anggota_kelompok_7, name="anggota_kelompok_7"),
    path("anggota-kelompok_8/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>/<materi>/<simulasi>/<jumlah_peserta>/<email_1>/<nama_lengkap_1>/<nomor_telefon_1>/<akun_discord_1>/<email_2>/<nama_lengkap_2>/<nomor_telefon_2>/<akun_discord_2>/<email_3>/<nama_lengkap_3>/<nomor_telefon_3>/<akun_discord_3>/<email_4>/<nama_lengkap_4>/<nomor_telefon_4>/<akun_discord_4>/<email_5>/<nama_lengkap_5>/<nomor_telefon_5>/<akun_discord_5>/<email_6>/<nama_lengkap_6>/<nomor_telefon_6>/<akun_discord_6>/<email_7>/<nama_lengkap_7>/<nomor_telefon_7>/<akun_discord_7>/", views.anggota_kelompok_8, name="anggota_kelompok_8"),
    path("anggota-kelompok_9/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>/<materi>/<simulasi>/<jumlah_peserta>/<email_1>/<nama_lengkap_1>/<nomor_telefon_1>/<akun_discord_1>/<email_2>/<nama_lengkap_2>/<nomor_telefon_2>/<akun_discord_2>/<email_3>/<nama_lengkap_3>/<nomor_telefon_3>/<akun_discord_3>/<email_4>/<nama_lengkap_4>/<nomor_telefon_4>/<akun_discord_4>/<email_5>/<nama_lengkap_5>/<nomor_telefon_5>/<akun_discord_5>/<email_6>/<nama_lengkap_6>/<nomor_telefon_6>/<akun_discord_6>/<email_7>/<nama_lengkap_7>/<nomor_telefon_7>/<akun_discord_7>/<email_8>/<nama_lengkap_8>/<nomor_telefon_8>/<akun_discord_8>/", views.anggota_kelompok_9, name="anggota_kelompok_9"),
    path("anggota-kelompok_10/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>/<materi>/<simulasi>/<jumlah_peserta>/<email_1>/<nama_lengkap_1>/<nomor_telefon_1>/<akun_discord_1>/<email_2>/<nama_lengkap_2>/<nomor_telefon_2>/<akun_discord_2>/<email_3>/<nama_lengkap_3>/<nomor_telefon_3>/<akun_discord_3>/<email_4>/<nama_lengkap_4>/<nomor_telefon_4>/<akun_discord_4>/<email_5>/<nama_lengkap_5>/<nomor_telefon_5>/<akun_discord_5>/<email_6>/<nama_lengkap_6>/<nomor_telefon_6>/<akun_discord_6>/<email_7>/<nama_lengkap_7>/<nomor_telefon_7>/<akun_discord_7>/<email_8>/<nama_lengkap_8>/<nomor_telefon_8>/<akun_discord_8>/<email_9>/<nama_lengkap_9>/<nomor_telefon_9>/<akun_discord_9>/", views.anggota_kelompok_10, name="anggota_kelompok_10"),

    path("jadwal-belajar/<email>/<nama_lengkap>/<nomor_telefon>/<program_studi>/<angkatan>/<universitas>/<info>/<metode_pembelajaran>/<jumlah_sesi_yang_diikuti>/<mata_kuliah>/<materi>/<simulasi>/<jumlah_peserta>/<email_1>/<nama_lengkap_1>/<nomor_telefon_1>/<akun_discord_1>/<email_2>/<nama_lengkap_2>/<nomor_telefon_2>/<akun_discord_2>/<email_3>/<nama_lengkap_3>/<nomor_telefon_3>/<akun_discord_3>/<email_4>/<nama_lengkap_4>/<nomor_telefon_4>/<akun_discord_4>/<email_5>/<nama_lengkap_5>/<nomor_telefon_5>/<akun_discord_5>/<email_6>/<nama_lengkap_6>/<nomor_telefon_6>/<akun_discord_6>/<email_7>/<nama_lengkap_7>/<nomor_telefon_7>/<akun_discord_7>/<email_8>/<nama_lengkap_8>/<nomor_telefon_8>/<akun_discord_8>/<email_9>/<nama_lengkap_9>/<nomor_telefon_9>/<akun_discord_9>/<email_10>/<nama_lengkap_10>/<nomor_telefon_10>/<akun_discord_10>/", views.jadwal_belajar, name="jadwal_belajar"),

    path("invoice-assignment-q1/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q1_invoice>/<quartal_invoice>/", views.invoice_assignment_q1, name="invoice_assignment_q1"),
    path("invoice-assignment-q2/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q2_invoice>/<quartal_invoice>/", views.invoice_assignment_q2, name="invoice_assignment_q2"),
    path("invoice-assignment-q3/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q3_invoice>/<quartal_invoice>/", views.invoice_assignment_q3, name="invoice_assignment_q3"),
    path("invoice-assignment-q4/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q4_invoice>/<quartal_invoice>/", views.invoice_assignment_q4, name="invoice_assignment_q4"),

    path("invoice-q1/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q1_invoice>/<quartal_invoice>/", views.invoice_q1, name="invoice_q1"),
    path("invoice-q2/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q2_invoice>/<quartal_invoice>/", views.invoice_q2, name="invoice_q2"),
    path("invoice-q3/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q3_invoice>/<quartal_invoice>/", views.invoice_q3, name="invoice_q3"),
    path("invoice-q4/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q4_invoice>/<quartal_invoice>/", views.invoice_q4, name="invoice_q4"),
    path('get-data/', views.get_data, name='get_data'),

    path('pendaftaran-berhasil-q1/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<metode_pembelajaran>/<mata_kuliah>/<materi>/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q1_invoice>/<quartal_invoice>/', views.send_email_q1, name='send_email_q1'),
    path('pendaftaran-berhasil-q2/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<metode_pembelajaran>/<mata_kuliah>/<materi>/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q2_invoice>/<quartal_invoice>/', views.send_email_q2, name='send_email_q2'),
    path('pendaftaran-berhasil-q3/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<metode_pembelajaran>/<mata_kuliah>/<materi>/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q3_invoice>/<quartal_invoice>/', views.send_email_q3, name='send_email_q3'),
    path('pendaftaran-berhasil-q4/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<metode_pembelajaran>/<mata_kuliah>/<materi>/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q4_invoice>/<quartal_invoice>/', views.send_email_q4, name='send_email_q4'),

    path('pendaftaran-berhasil/', views.pendaftaran_berhasil, name='pendaftaran_berhasil'),
    path('pendaftaran-gagal/', views.pendaftaran_gagal, name='pendaftaran_gagal'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)