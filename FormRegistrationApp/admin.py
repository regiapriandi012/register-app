from django.contrib import admin
from .views import RegistrationData, ReferralCode
# Register your models here.

@admin.register(RegistrationData)
class RegistrationDataAdmin(admin.ModelAdmin):
    list_display = ('nomor_invoice', 'email', 'nama_lengkap', 'nomor_telefon')
    search_fields = ('nomor_invoice', 'email', 'nama_lengkap', 'nomor_telefon', 'tanggal')
    list_filter = ('created_on', 'universitas', 'program_studi', 'metode_pembelajaran')

@admin.register(ReferralCode)
class ReferralCodeAdmin(admin.ModelAdmin):
    list_display = ('referral_code',)
    search_fields = ('referral_code',)
    list_filter = ('created_on',)