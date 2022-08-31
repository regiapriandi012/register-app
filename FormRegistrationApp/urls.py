from django.urls import path
from . import views
import datetime
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home_view, name="register"),

    path("metode_pembelajaran/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/", views.metode_pembelajaran, name="metode_pembelajaran"),
    
    path("session_cse/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_cse, name="session_cse"),
    path("session_cem/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_cem, name="session_cem"),
    path("session_cet/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_cet, name="session_cet"),
    path("session_cps/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_cps, name="session_cps"),
    path("session_cre/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_cre, name="session_cre"),
    path("session_eec/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_eec, name="session_eec"),
    path("session_fac/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_fac, name="session_fac"),
    path("session_fca/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_fca, name="session_fca"),
    path("session_fch/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_fch, name="session_fch"),
    path("session_fht/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_fht, name="session_fht"),
    path("session_fmt/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_fmt, name="session_fmt"),
    path("session_fpm/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_fpm, name="session_fpm"),
    path("session_fp1/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_fp1, name="session_fp1"),
    path("session_fp2/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_fp2, name="session_fp2"),
    path("session_meb/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_meb, name="session_meb"),
    path("session_nce/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_nce, name="session_nce"),
    path("session_oce/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_oce, name="session_oce"),
    path("session_pcd/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_pcd, name="session_pcd"),
    path("session_pdd/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_pdd, name="session_pdd"),
    path("session_ped/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_ped, name="session_ped"),
    path("session_ppd/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_ppd, name="session_ppd"),
    path("session_tph/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/", views.session_tph, name="session_tph"),

    path("session_cse/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_cse"),
    path("session_cem/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_cem"),
    path("session_cet/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_cet"),
    path("session_cps/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/<simulasi>", views.jumlah_peserta_simulasi, name="jumlah_peserta_session_cps"),
    path("session_cre/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_cre"),
    path("session_eec/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_eec"),
    path("session_fac/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_fac"),
    path("session_fca/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_fca"),
    path("session_fch/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_fch"),
    path("session_fht/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_fht"),
    path("session_fmt/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_fmt"),
    path("session_fpm/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_fpm"),
    path("session_fp1/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_fp1"),
    path("session_fp2/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_fp2"),
    path("session_meb/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_meb"),
    path("session_nce/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_nce"),
    path("session_oce/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_oce"),
    path("session_pcd/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_pcd"),
    path("session_pdd/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_pdd"),
    path("session_ped/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_ped"),
    path("session_ppd/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_ppd"),
    path("session_tph/jumlah_peserta/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<tentang_torche>/<metode_pembelajaran>/<mata_kuliah>/<jumlah_sesi_yang_ingin_diikuti>/<materi>/", views.jumlah_peserta, name="jumlah_peserta_session_tph"),

    path("invoice_assignment_q1/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q1_invoice>/<quartal_invoice>/", views.invoice_assignment_q1, name="invoice_assignment_q1"),
    path("invoice_assignment_q2/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q2_invoice>/<quartal_invoice>/", views.invoice_assignment_q2, name="invoice_assignment_q2"),
    path("invoice_assignment_q3/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q3_invoice>/<quartal_invoice>/", views.invoice_assignment_q3, name="invoice_assignment_q3"),
    path("invoice_assignment_q4/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q4_invoice>/<quartal_invoice>/", views.invoice_assignment_q4, name="invoice_assignment_q4"),

    #path("invoice_q1/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q1_invoice>/<quartal_invoice>/", views.invoice_q1, name="invoice_q1"),
    #path("invoice_q2/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q2_invoice>/<quartal_invoice>/", views.invoice_q2, name="invoice_q2"),
    #path("invoice_q3/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q3_invoice>/<quartal_invoice>/", views.invoice_q3, name="invoice_q3"),
    #path("invoice_q4/Inv/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q4_invoice>/<quartal_invoice>/", views.invoice_q4, name="invoice_q4"),
    path('get_data/', views.get_data, name='get_data'),

    path('pendaftaran_berhasil/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<metode_pembelajaran>/<mata_kuliah>/<materi>/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q1_invoice>/<quartal_invoice>/', views.send_email_q1, name='send_email_q1'),
    path('pendaftaran_berhasil/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<metode_pembelajaran>/<mata_kuliah>/<materi>/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q2_invoice>/<quartal_invoice>/', views.send_email_q2, name='send_email_q2'),
    path('pendaftaran_berhasil/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<metode_pembelajaran>/<mata_kuliah>/<materi>/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q3_invoice>/<quartal_invoice>/', views.send_email_q3, name='send_email_q3'),
    path('pendaftaran_berhasil/<nama_lengkap>/<email>/<nomor_telefon>/<program_studi>/<universitas>/<metode_pembelajaran>/<mata_kuliah>/<materi>/<jumlah_peserta_invoice>/<metode_pembelajaran_invoice>/<mata_kuliah_invoice>/<registration_number_q4_invoice>/<quartal_invoice>/', views.send_email_q4, name='send_email_q4'),

    path('pendaftaran_berhasil/', views.pendaftaran_berhasil, name='pendaftaran_berhasil'), 
    path('pendaftaran_gagal/', views.pendaftaran_gagal, name='pendaftaran_gagal'),

    path('anggota_kelompok/', views.anggota_kelompok, name='anggota_kelompok'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)