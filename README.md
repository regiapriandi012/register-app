![](https://img.shields.io/github/license/regiapriandi012/registration-app-django)
![](https://github.com/regiapriandi012/registration-app-django/actions/workflows/codeql.yml/badge.svg)
![](https://github.com/regiapriandi012/registration-app-django/actions/workflows/dependency-review.yml/badge.svg)
![](https://github.com/regiapriandi012/registration-app-django/actions/workflows/docker-image.yml/badge.svg)
![](https://github.com/regiapriandi012/registration-app-django/actions/workflows/docker-publish.yml/badge.svg)

# Django Registration App
### Features
- ### Integrated with Google Drive
  Can automate save file or upload file from registration form to Google Drive.
- ### Integrated with Gmail
  Can send invoice registration document to Gmail.
- ### Integrated with Discord Bot
  Can send notification and file while user registered in app.
### Flowchart
![image](https://user-images.githubusercontent.com/69528812/196679538-8793bccf-c861-4c15-b991-19b4f1c2c9c1.png)

### Requirement Packages
````
arabic-reshaper==2.1.3
asgiref==3.2.10
asn1crypto==1.5.1
cachetools==4.2.4
certifi==2022.6.15
cffi==1.15.1
charset-normalizer==2.1.1
click==8.1.3
cryptography==37.0.4
cssselect2==0.6.0
Django==3.1.1
django-environ==0.9.0
django-googledrive-storage==1.6.0
django-multiselectfield==0.1.12
djongo==1.3.6
dnspython==2.2.1
future==0.18.2
google-api-core==2.10.0
google-api-python-client==2.60.0
google-auth==1.35.0
google-auth-httplib2==0.1.0
googleapis-common-protos==1.56.4
gunicorn==20.0.4
html5lib==1.1
httplib2==0.20.4
idna==3.3
lxml==4.9.1
mock==4.0.3
mongoengine==0.24.2
oauth2client==4.1.3
oscrypto==1.3.0
Pillow==9.2.0
protobuf==4.21.5
psycopg2==2.9.3
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.21
PyDrive==1.3.1
pyHanko==0.13.2
pyhanko-certvalidator==0.19.5
pymongo==3.12.3
pyparsing==3.0.9
PyPDF3==1.0.6
python-bidi==0.4.2
python-dateutil==2.8.2
python-snappy==0.6.1
pytz==2022.2.1
pytz-deprecation-shim==0.1.0.post0
PyYAML==6.0
qrcode==7.3.1
reportlab==3.6.11
requests==2.28.1
rsa==4.9
six==1.16.0
sqlparse==0.2.4
svglib==1.4.1
tinycss2==1.1.1
tqdm==4.64.0
tzdata==2022.2
tzlocal==4.2
uritemplate==4.1.1
uritools==4.0.0
urllib3==1.26.12
webencodings==0.5.1
xhtml2pdf==0.2.8
````

### Directory Structure
```text
└── FormRegistration
    ├── FormRegistration
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── setting.py
    │   ├── urls.py
    │   ├── wsgi.py 
    ├── FormRegistrationApp
    │   ├── migrations
    │   ├── templates
    │   │    ├── FormRegistrationApp
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── urls.py
    │   ├── views.py
    │   └── test.py
    ├── client_secret.json
    ├── db.sqlite3
    ├── manage.py
    ├── requirements.txt
    └── README.md
```

### Model
```
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
    
class ReferralCode(models.Model):
    referral_code = models.CharField(max_length=254)
    created_on = models.DateTimeField(auto_now_add=True)
 ```

### Configuration
##### views.py
```
line 22, webhook = DiscordWebhook(url='<webhook_url>', username="<username>")
line 5, permission = GoogleDriveFilePermission(GoogleDrivePermissionRole.READER, GoogleDrivePermissionType.USER, "<sender_email>",)
```
##### settings.py
```
line 23, SECRET_KEY = '<secret_key>'
line 43, GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = os.path.join(BASE_DIR,'<client_secrets.json path>')
line 140, EMAIL_SENDER = '<sender_email>'
line 141, EMAIL_HOST_USER = "<user_email>"
line 142, EMAIL_HOST_PASSWORD = "<password_application>"
```

### Edit Configuration
#### Google Drive Account
```
file Formregistration/settings.py, line 140
```
#### Change Database
```
file Formregistration/settings.py, line 79
```

### Install
```
pip install requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

### ! Notice
This project is open to front-end devs who want to develop app UI.
