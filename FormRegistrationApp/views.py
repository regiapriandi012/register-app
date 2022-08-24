from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from .forms import CourseRegistrationForm, SessionCSEForm, SessionCEMForm, SessionCETForm, SessionCPSForm, SessionCREForm, SessionEECForm, SessionFACForm, SessionFCAForm, SessionFCHForm, SessionFHTForm, SessionFMTForm, SessionFPMForm, SessionFP1Form, SessionFP2Form, SessionMEBForm, SessionNCEForm, SessionOCEForm, SessionPCDForm, SessionPDDForm, SessionPEDForm, SessionPPDForm, SessionTPHForm, JumlahPeserta
from django.http import HttpResponseRedirect
from .models import RegistrationData, ReferralCode
from django.views import generic
import datetime
from PIL import Image
from io import BytesIO
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.template.loader import render_to_string


NAMA_MATA_KULIAH = (
        ("Cell Culture for Engineers", "Cell Culture for Engineers"),
        ("Chemical Engineering Mathematics", "Chemical Engineering Mathematics"),
        ("Chemical Engineering Thermodynamics", "Chemical Engineering Thermodynamics"),
        ("Chemical Process Simulation", "Chemical Process Simulation"),
        ("Chemical Reaction Engineering", "Chemical Reaction Engineering"),
        ("Engineering Economy", "Engineering Economy"),
        ("Fundamentals of Analytical Chemistry", "Fundamentals of Analytical Chemistry"),
        ("Fundamentals of Calculus", "Fundamentals of Calculus"),
        ("Fundamentals of Chemistry", "Fundamentals of Chemistry"),
        ("Fundamentals of Heat Transfer", "Fundamentals of Heat Transfer"),
        ("Fundamentals of Mass Transfer", "Fundamentals of Mass Transfer"),
        ("Fluid and Particles Mechanics", "Fluid and Particles Mechanics"),
        ("Fundamentals of Physics 1", "Fundamentals of Physics 1"),
        ("Fundamentals of Physics 2", "Fundamentals of Physics 2"),
        ("Mass and Energy Balances", "Mass and Energy Balances"),
        ("Numerical Computation for Engineers", "Numerical Computation for Engineers"),
        ("Organic Chemistry for Engineers", "Organic Chemistry for Engineers"),
        ("Process Control and Dynamics", "Process Control and Dynamics"),
        ("Product Design and Development", "Product Design and Development"),
        ("Process Equipment Design", "Process Equipment Design"),
        ("Process Plant Design", "Process Plant Design"),
        ("Transport Phenomena", "Transport Phenomena")
    )

registration_number_q1 = 0
registration_number_q2 = 0
registration_number_q3 = 0
registration_number_q4 = 0

registration_number_q1_invoice = ""
registration_number_q2_invoice = ""
registration_number_q3_invoice = ""
registration_number_q4_invoice = ""

# Create your views here.
def home_view(request):
    context = {'form': CourseRegistrationForm()}
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            nama_lengkap = form.cleaned_data['nama_lengkap']
            email = form.cleaned_data['email']
            nomor_telefon = form.cleaned_data['nomor_telefon']
            #program_studi = form.cleaned_data['program_studi']
            #universitas = form.cleaned_data['universitas']
            program_studi = request.POST.get('program_studi')
            universitas = request.POST.get('universitas')
            metode_pembelajaran = form.cleaned_data['metode_pembelajaran']
            mata_kuliah = form.cleaned_data['mata_kuliah']

            if program_studi == "Other":
                program_studi = request.POST.get('program_studi_other')
            else:
                program_studi = request.POST.get('program_studi')

            if universitas == "Other":
                universitas = request.POST.get('universitas_other')
            else:
                universitas = request.POST.get('universitas')

            if mata_kuliah == NAMA_MATA_KULIAH[0][0]:
                return redirect("session_cse", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[1][0]:
                return redirect("session_cem", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[2][0]:
                return redirect("session_cet", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[3][0]:
                return redirect("session_cps", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[4][0]:
                return redirect("session_cre", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[5][0]:
                return redirect("session_eec", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[6][0]:
                return redirect("session_fac", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[7][0]:
                return redirect("session_fca", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[8][0]:
                return redirect("session_fch", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[9][0]:
                return redirect("session_fht", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[10][0]:
                return redirect("session_fmt", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[11][0]:
                return redirect("session_fpm", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[12][0]:
                return redirect("session_fp1", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[13][0]:
                return redirect("session_fp2", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[14][0]:
                return redirect("session_meb", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[15][0]:
                return redirect("session_nce", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[16][0]:
                return redirect("session_oce", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[17][0]:
                return redirect("session_pcd", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[18][0]:
                return redirect("session_pdd", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[19][0]:
                return redirect("session_ped", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
            elif mata_kuliah == NAMA_MATA_KULIAH[20][0]:
                return redirect("session_ppd", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)  
            elif mata_kuliah == NAMA_MATA_KULIAH[21][0]:
                return redirect("session_tph", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah)
    else:
        form = CourseRegistrationForm(request.POST)
    return render(request, "FormRegistrationApp/index.html", context)

def session_cse(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionCSEForm()}
    if request.method == 'POST':
        form = SessionCSEForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_cse", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionCSEForm(request.POST)
    return render(request, "FormRegistrationApp/session_cse.html", context)

def session_cem(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionCEMForm()}
    if request.method == 'POST':
        form = SessionCEMForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_cem", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionCEMForm(request.POST)
    return render(request, "FormRegistrationApp/session_cem.html", context)

def session_cet(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionCETForm()}
    if request.method == 'POST':
        form = SessionCETForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_cet", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionCETForm(request.POST)
    return render(request, "FormRegistrationApp/session_cet.html", context)

def session_cps(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionCPSForm()}
    if request.method == 'POST':
        form = SessionCPSForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            simulasi = form.cleaned_data['simulasi']
            return redirect("jumlah_peserta_session_cps", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, simulasi)
    else:
        form = SessionCPSForm(request.POST)
    return render(request, "FormRegistrationApp/session_cps.html", context)

def session_cre(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionCREForm()}
    if request.method == 'POST':
        form = SessionCREForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_cre", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionCREForm(request.POST)
    return render(request, "FormRegistrationApp/session_cre.html", context)

def session_eec(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionEECForm()}
    if request.method == 'POST':
        form = SessionEECForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_eec", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionEECForm(request.POST)
    return render(request, "FormRegistrationApp/session_eec.html", context)

def session_fac(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionFACForm()}
    if request.method == 'POST':
        form = SessionFACForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_fac", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionFACForm(request.POST)
    return render(request, "FormRegistrationApp/session_fac.html", context)

def session_fca(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionFCAForm()}
    if request.method == 'POST':
        form = SessionFCAForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_fca", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionFCAForm(request.POST)
    return render(request, "FormRegistrationApp/session_fca.html", context)

def session_fch(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionFCHForm()}
    if request.method == 'POST':
        form = SessionFCHForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_fch", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionFCHForm(request.POST)
    return render(request, "FormRegistrationApp/session_fch.html", context)

def session_fht(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionFHTForm()}
    if request.method == 'POST':
        form = SessionFHTForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_fht", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionFHTForm(request.POST)
    return render(request, "FormRegistrationApp/session_fht.html", context)

def session_fmt(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionFMTForm()}
    if request.method == 'POST':
        form = SessionFMTForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_fmt", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionFMTForm(request.POST)
    return render(request, "FormRegistrationApp/session_fmt.html", context)

def session_fpm(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionFPMForm()}
    if request.method == 'POST':
        form = SessionFPMForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_fpm", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionFPMForm(request.POST)
    return render(request, "FormRegistrationApp/session_fpm.html", context)

def session_fp1(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionFP1Form()}
    if request.method == 'POST':
        form = SessionFP1Form(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_fp1", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionFP1Form(request.POST)
    return render(request, "FormRegistrationApp/session_fp1.html", context)

def session_fp2(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionFP2Form()}
    if request.method == 'POST':
        form = SessionFP2Form(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_fp2", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionFP2Form(request.POST)
    return render(request, "FormRegistrationApp/session_fp2.html", context)

def session_meb(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionMEBForm()}
    if request.method == 'POST':
        form = SessionMEBForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_meb", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionMEBForm(request.POST)
    return render(request, "FormRegistrationApp/session_meb.html", context)

def session_nce(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionNCEForm()}
    if request.method == 'POST':
        form = SessionNCEForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_nce", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionNCEForm(request.POST)
    return render(request, "FormRegistrationApp/session_nce.html", context)

def session_oce(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionOCEForm()}
    if request.method == 'POST':
        form = SessionOCEForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_oce", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionOCEForm(request.POST)
    return render(request, "FormRegistrationApp/session_oce.html", context)

def session_pcd(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionPCDForm()}
    if request.method == 'POST':
        form = SessionPCDForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_pcd", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionPCDForm(request.POST)
    return render(request, "FormRegistrationApp/session_pcd.html", context)

def session_pdd(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionPDDForm()}
    if request.method == 'POST':
        form = SessionPDDForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_pdd", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionPDDForm(request.POST)
    return render(request, "FormRegistrationApp/session_pdd.html", context)

def session_ped(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionPEDForm()}
    if request.method == 'POST':
        form = SessionPEDForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_ped", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionPEDForm(request.POST)
    return render(request, "FormRegistrationApp/session_ped.html", context)

def session_ppd(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionPPDForm()}
    if request.method == 'POST':
        form = SessionPPDForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_ppd", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionPPDForm(request.POST)
    return render(request, "FormRegistrationApp/session_ppd.html", context)

def session_tph(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah):
    context = {'form': SessionTPHForm()}
    if request.method == 'POST':
        form = SessionTPHForm(request.POST)
        if form.is_valid():
            materi = form.cleaned_data['materi']
            return redirect("jumlah_peserta_session_tph", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi)
    else:
        form = SessionTPHForm(request.POST)
    return render(request, "FormRegistrationApp/session_tph.html", context)

def jumlah_peserta(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi):
    context = {'form': JumlahPeserta()}
    if request.method == 'POST':
        form = JumlahPeserta(request.POST)
        if form.is_valid():
            new_data = RegistrationData()

            global registration_number_q1
            global registration_number_q2
            global registration_number_q3
            global registration_number_q4

            global registration_number_q1_invoice
            global registration_number_q2_invoice
            global registration_number_q3_invoice
            global registration_number_q4_invoice

            month_number = datetime.datetime.now().month

            invoice = "Inv/"
            jumlah_peserta_invoice = ""
            metode_pembelajaran_invoice = ""
            mata_kuliah_invoice = ""
            quartal_invoice = ""

            jumlah_peserta = request.POST.get('jumlah_peserta')
            if jumlah_peserta == "Other":
                jumlah_peserta = request.POST.get('jumlah_peserta_lain')
            else:
                jumlah_peserta = request.POST.get('jumlah_peserta')

            if jumlah_peserta <= "3":
                invoice += "P/"
                jumlah_peserta_invoice = "P"
            elif jumlah_peserta > "3":
                invoice += "G/"
                jumlah_peserta_invoice = "G"

            metode_pembelajaran = metode_pembelajaran
            if metode_pembelajaran == "Kelas Konsultasi":
                invoice += "C/"
                metode_pembelajaran_invoice = "C"
            elif metode_pembelajaran == "Kelas Materi":
                invoice += "L/"
                metode_pembelajaran_invoice = "L"
            elif metode_pembelajaran == "Persiapan Ujian":
                invoice += "EP/"
                metode_pembelajaran_invoice = "EP"
            elif metode_pembelajaran == "Konsultasi Perlombaan":
                invoice += "C/"
                metode_pembelajaran_invoice = "C"
            elif metode_pembelajaran == "Konsultasi Skripsi atau Tesis":
                invoice += "C/"
                metode_pembelajaran_invoice = "C"

            mata_kuliah = mata_kuliah
            if mata_kuliah == NAMA_MATA_KULIAH[0][0]:
                invoice += "CCE/"
                mata_kuliah_invoice = "CCE"
            elif mata_kuliah == NAMA_MATA_KULIAH[1][0]:
                invoice += "CEM/"
                mata_kuliah_invoice = "CEM"
            elif mata_kuliah == NAMA_MATA_KULIAH[2][0]:
                invoice += "CTE/"
                mata_kuliah_invoice = "CTE"
            elif mata_kuliah == NAMA_MATA_KULIAH[3][0]:
                invoice += "CPS/"
                mata_kuliah_invoice = "CPS"
            elif mata_kuliah == NAMA_MATA_KULIAH[4][0]:
                invoice += "CRE/"
                mata_kuliah_invoice = "CRE"
            elif mata_kuliah == NAMA_MATA_KULIAH[5][0]:
                invoice += "EEC/"
                mata_kuliah_invoice = "EEC"
            elif mata_kuliah == NAMA_MATA_KULIAH[6][0]:
                invoice += "FAC/"
                mata_kuliah_invoice = "FAC"
            elif mata_kuliah == NAMA_MATA_KULIAH[7][0]:
                invoice += "FCA/"
                mata_kuliah_invoice = "FCA"
            elif mata_kuliah == NAMA_MATA_KULIAH[8][0]:
                invoice += "FCH/"
                mata_kuliah_invoice = "FCH"
            elif mata_kuliah == NAMA_MATA_KULIAH[9][0]:
                invoice += "FHT/"
                mata_kuliah_invoice = "FHT"
            elif mata_kuliah == NAMA_MATA_KULIAH[10][0]:
                invoice += "FMT/"
                mata_kuliah_invoice = "FMT"
            elif mata_kuliah == NAMA_MATA_KULIAH[11][0]:
                invoice += "FPM/"
                mata_kuliah_invoice = "FPM"
            elif mata_kuliah == NAMA_MATA_KULIAH[12][0]:
                invoice += "FP1/"
                mata_kuliah_invoice = "FP1"
            elif mata_kuliah == NAMA_MATA_KULIAH[13][0]:
                invoice += "FP2/"
                mata_kuliah_invoice = "FP2"
            elif mata_kuliah == NAMA_MATA_KULIAH[14][0]:
                invoice += "MEB/"
                mata_kuliah_invoice = "MEB"
            elif mata_kuliah == NAMA_MATA_KULIAH[15][0]:
                invoice += "NCE/"
                mata_kuliah_invoice = "NCE"
            elif mata_kuliah == NAMA_MATA_KULIAH[16][0]:
                invoice += "OCE/"
                mata_kuliah_invoice = "OCE"
            elif mata_kuliah == NAMA_MATA_KULIAH[17][0]:
                invoice += "PCD/"
                mata_kuliah_invoice = "PCD"
            elif mata_kuliah == NAMA_MATA_KULIAH[18][0]:
                invoice += "PDD/"
                mata_kuliah_invoice = "PDD"
            elif mata_kuliah == NAMA_MATA_KULIAH[19][0]:
                invoice += "PED/"
                mata_kuliah_invoice = "PED"
            elif mata_kuliah == NAMA_MATA_KULIAH[20][0]:
                invoice += "PPD/"
                mata_kuliah_invoice = "PPD"
            elif mata_kuliah == NAMA_MATA_KULIAH[21][0]:
                invoice += "TPH/"
                mata_kuliah_invoice = "TPH"

            if month_number >= 1 and month_number <= 3:
                registration_number_q1 += 1
                if registration_number_q1 <= 9:
                    invoice += "0"+str(registration_number_q1)+ "/"
                    registration_number_q1_invoice = "0"+str(registration_number_q1)
                elif registration_number_q1 >= 10:
                    invoice += str(registration_number_q1)+ "/"
                    registration_number_q1_invoice = str(registration_number_q1)
            elif month_number >= 4 and month_number <= 6:
                registration_number_q2 += 1
                if registration_number_q2 <= 9:
                    invoice += "0"+str(registration_number_q2)+ "/"
                    registration_number_q2_invoice = "0"+str(registration_number_q2)
                elif registration_number_q2 >= 10:
                   invoice += str(registration_number_q2)+ "/"
                   registration_number_q2_invoice = str(registration_number_q2)
            elif month_number >= 7 and month_number <= 9:
                registration_number_q3 += 1
                if registration_number_q3 <= 9:
                    invoice += "0"+str(registration_number_q3)+ "/"
                    registration_number_q3_invoice = "0"+str(registration_number_q3)
                elif registration_number_q3 >= 10:                        
                    invoice += str(registration_number_q3)+ "/"
                    registration_number_q3_invoice = str(registration_number_q3)
            elif month_number >= 10 and month_number <= 12:
                registration_number_q4 += 1
                if registration_number_q4 <= 9:
                    invoice += "0"+str(registration_number_q4)+ "/"
                    registration_number_q4_invoice = "0"+str(registration_number_q4)
                elif registration_number_q1 >= 10:
                    invoice += str(registration_number_q4)+ "/"
                    registration_number_q4_invoice = str(registration_number_q4)

            if month_number >= 1 and month_number <= 3:
                invoice += "1-"
                quartal_invoice = "1-"
            elif month_number >= 4 and month_number <= 6:
                invoice += "2-"
                quartal_invoice = "2-"
            elif month_number >= 7 and month_number <= 9:
                invoice += "3-"
                quartal_invoice = "3-"
            elif month_number >= 10 and month_number <= 12:
                invoice += "4-"
                quartal_invoice = "4-"

            year_number = datetime.datetime.now().year
            invoice += "{}".format(str(year_number)[-2:])
            quartal_invoice += "{}".format(str(year_number)[-2:])

            new_data.invoice = invoice
            new_data.nama_lengkap = nama_lengkap
            new_data.email = email
            new_data.nomor_telefon = nomor_telefon
            new_data.program_studi = program_studi
            new_data.universitas = universitas
            new_data.metode_pembelajaran = metode_pembelajaran
            new_data.mata_kuliah = mata_kuliah
            new_data.materi = materi
            new_data.jumlah_sesi_yang_ingin_diikuti = form.cleaned_data['jumlah_sesi_yang_ingin_diikuti']
            
            jumlah_peserta = request.POST.get('jumlah_peserta')
            if jumlah_peserta == "Other":
                jumlah_peserta = request.POST.get('jumlah_peserta_lain')
            else:
                jumlah_peserta = request.POST.get('jumlah_peserta')
            
            new_data.jumlah_peserta = jumlah_peserta
            new_data.nama_anggota_kelompok_bagi_yang_kelompok = form.cleaned_data['nama_anggota_kelompok_bagi_yang_kelompok']
            new_data.alamat_email_anggota_kelompok = form.cleaned_data['alamat_email_anggota_kelompok']
            sesi_dan_jadwal = form.cleaned_data['sesi_dan_jadwal']
            new_data.notes_for_tutor = form.cleaned_data['notes_for_tutor']

            sesi_materi = []
            sesi_tanggal = []
            sesi_jam = []

            for i in range(len(sesi_dan_jadwal.split("],"))):
                sesi_materi.append(sesi_dan_jadwal.split("],")[i].split("[")[0].strip())
                sesi_tanggal.append(sesi_dan_jadwal.split("],")[i].split("[")[1].split(",")[0])
                sesi_jam.append(sesi_dan_jadwal.split("],")[i].split(",")[1].replace(" ", "").replace("]", ""))

            new_data.sesi_materi = sesi_materi
            new_data.sesi_tanggal = sesi_tanggal
            new_data.sesi_jam = sesi_jam

            biaya = 0
            if int(jumlah_peserta) <= 3:
                biaya += (175000 * len(sesi_materi))
            elif int(jumlah_peserta) == 4:
                biaya += (200000 * len(sesi_materi))
            elif int(jumlah_peserta) == 5:
                biaya += (250000 * len(sesi_materi))
            elif int(jumlah_peserta) >= 6:
                biaya += ((250000 + ((int(jumlah_peserta) - 5) * 40000)) * len(sesi_materi))
            new_data.biaya = "{:0,.0f}".format(biaya)

            referral_code = form.cleaned_data['referral_code']
            data_referral_code = ReferralCode.objects.all()
            data_referral_code_list = []
            for i in data_referral_code:
                data_referral_code_list.append(i.referral_code)
            if referral_code in data_referral_code_list:
                new_data.referral_code = form.cleaned_data['referral_code']

            bulan = ""
            if datetime.datetime.now().month == 1:
                bulan = "Januari"
            elif datetime.datetime.now().month == 2:
                bulan = "Februari"
            elif datetime.datetime.now().month == 3:
                bulan = "Maret"
            elif datetime.datetime.now().month == 4:
                bulan = "April"
            elif datetime.datetime.now().month == 5:
                bulan = "Mei"
            elif datetime.datetime.now().month == 6:
                bulan = "Juni"
            elif datetime.datetime.now().month == 7:
                bulan = "Juli"
            elif datetime.datetime.now().month == 8:
                bulan = "Agustus"
            elif datetime.datetime.now().month == 9:
                bulan = "September"
            elif datetime.datetime.now().month == 10:
                bulan = "Oktober"
            elif datetime.datetime.now().month == 11:
                bulan = "November"
            elif datetime.datetime.now().month == 12:
                bulan = "Desember"

            tanggal = str(datetime.datetime.now().day) + " " + bulan + " " + str(datetime.datetime.now().year)
            new_data.tanggal = tanggal

            try:
                new_data.save()
            except:
                return redirect("pendaftaran_gagal")

        if month_number >= 1 and month_number <= 3:
            return redirect("send_email_q1", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q1_invoice, quartal_invoice)
        elif month_number >= 4 and month_number <= 6:
            return redirect("send_email_q2", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q2_invoice, quartal_invoice)
        elif month_number >= 7 and month_number <= 9:
            return redirect("send_email_q3", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q3_invoice, quartal_invoice)
        elif month_number >= 10 and month_number <= 12:
            return redirect("send_email_q4", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice)
    else:
        form = JumlahPeserta(request.POST)
    return render(request, "FormRegistrationApp/jumlah_peserta.html", context)

def jumlah_peserta_simulasi(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, simulasi):
    context = {'form': JumlahPeserta()}
    if request.method == 'POST':
        form = JumlahPeserta(request.POST)
        if form.is_valid():
            new_data = RegistrationData()

            global registration_number_q1
            global registration_number_q2
            global registration_number_q3
            global registration_number_q4

            global registration_number_q1_invoice
            global registration_number_q2_invoice
            global registration_number_q3_invoice
            global registration_number_q4_invoice

            month_number = datetime.datetime.now().month

            invoice = "Inv/"
            jumlah_peserta_invoice = ""
            metode_pembelajaran_invoice = ""
            mata_kuliah_invoice = ""
            quartal_invoice = ""

            jumlah_peserta = request.POST.get('jumlah_peserta')
            if jumlah_peserta == "Other":
                jumlah_peserta = request.POST.get('jumlah_peserta_lain')
            else:
                jumlah_peserta = request.POST.get('jumlah_peserta')

            if jumlah_peserta <= "3":
                invoice += "P/"
                jumlah_peserta_invoice = "P"
            elif jumlah_peserta > "3":
                invoice += "G/"
                jumlah_peserta_invoice = "G"

            metode_pembelajaran = metode_pembelajaran
            if metode_pembelajaran == "Kelas Konsultasi":
                invoice += "C/"
                metode_pembelajaran_invoice = "C"
            elif metode_pembelajaran == "Kelas Materi":
                invoice += "L/"
                metode_pembelajaran_invoice = "L"
            elif metode_pembelajaran == "Persiapan Ujian":
                invoice += "EP/"
                metode_pembelajaran_invoice = "EP"
            elif metode_pembelajaran == "Konsultasi Perlombaan":
                invoice += "C/"
                metode_pembelajaran_invoice = "C"
            elif metode_pembelajaran == "Konsultasi Skripsi atau Tesis":
                invoice += "C/"
                metode_pembelajaran_invoice = "C"

            mata_kuliah = mata_kuliah
            if mata_kuliah == NAMA_MATA_KULIAH[0][0]:
                invoice += "CCE/"
                mata_kuliah_invoice = "CCE"
            elif mata_kuliah == NAMA_MATA_KULIAH[1][0]:
                invoice += "CEM/"
                mata_kuliah_invoice = "CEM"
            elif mata_kuliah == NAMA_MATA_KULIAH[2][0]:
                invoice += "CTE/"
                mata_kuliah_invoice = "CTE"
            elif mata_kuliah == NAMA_MATA_KULIAH[3][0]:
                invoice += "CPS/"
                mata_kuliah_invoice = "CPS"
            elif mata_kuliah == NAMA_MATA_KULIAH[4][0]:
                invoice += "CRE/"
                mata_kuliah_invoice = "CRE"
            elif mata_kuliah == NAMA_MATA_KULIAH[5][0]:
                invoice += "EEC/"
                mata_kuliah_invoice = "EEC"
            elif mata_kuliah == NAMA_MATA_KULIAH[6][0]:
                invoice += "FAC/"
                mata_kuliah_invoice = "FAC"
            elif mata_kuliah == NAMA_MATA_KULIAH[7][0]:
                invoice += "FCA/"
                mata_kuliah_invoice = "FCA"
            elif mata_kuliah == NAMA_MATA_KULIAH[8][0]:
                invoice += "FCH/"
                mata_kuliah_invoice = "FCH"
            elif mata_kuliah == NAMA_MATA_KULIAH[9][0]:
                invoice += "FHT/"
                mata_kuliah_invoice = "FHT"
            elif mata_kuliah == NAMA_MATA_KULIAH[10][0]:
                invoice += "FMT/"
                mata_kuliah_invoice = "FMT"
            elif mata_kuliah == NAMA_MATA_KULIAH[11][0]:
                invoice += "FPM/"
                mata_kuliah_invoice = "FPM"
            elif mata_kuliah == NAMA_MATA_KULIAH[12][0]:
                invoice += "FP1/"
                mata_kuliah_invoice = "FP1"
            elif mata_kuliah == NAMA_MATA_KULIAH[13][0]:
                invoice += "FP2/"
                mata_kuliah_invoice = "FP2"
            elif mata_kuliah == NAMA_MATA_KULIAH[14][0]:
                invoice += "MEB/"
                mata_kuliah_invoice = "MEB"
            elif mata_kuliah == NAMA_MATA_KULIAH[15][0]:
                invoice += "NCE/"
                mata_kuliah_invoice = "NCE"
            elif mata_kuliah == NAMA_MATA_KULIAH[16][0]:
                invoice += "OCE/"
                mata_kuliah_invoice = "OCE"
            elif mata_kuliah == NAMA_MATA_KULIAH[17][0]:
                invoice += "PCD/"
                mata_kuliah_invoice = "PCD"
            elif mata_kuliah == NAMA_MATA_KULIAH[18][0]:
                invoice += "PDD/"
                mata_kuliah_invoice = "PDD"
            elif mata_kuliah == NAMA_MATA_KULIAH[19][0]:
                invoice += "PED/"
                mata_kuliah_invoice = "PED"
            elif mata_kuliah == NAMA_MATA_KULIAH[20][0]:
                invoice += "PPD/"
                mata_kuliah_invoice = "PPD"
            elif mata_kuliah == NAMA_MATA_KULIAH[21][0]:
                invoice += "TPH/"
                mata_kuliah_invoice = "TPH"

            if month_number >= 1 and month_number <= 3:
                registration_number_q1 += 1
                if registration_number_q1 <= 9:
                    invoice += "0"+str(registration_number_q1)+ "/"
                    registration_number_q1_invoice = "0"+str(registration_number_q1)
                elif registration_number_q1 >= 10:
                    invoice += str(registration_number_q1)+ "/"
                    registration_number_q1_invoice = str(registration_number_q1)
            elif month_number >= 4 and month_number <= 6:
                registration_number_q2 += 1
                if registration_number_q2 <= 9:
                    invoice += "0"+str(registration_number_q2)+ "/"
                    registration_number_q2_invoice = "0"+str(registration_number_q2)
                elif registration_number_q2 >= 10:
                   invoice += str(registration_number_q2)+ "/"
                   registration_number_q2_invoice = str(registration_number_q2)
            elif month_number >= 7 and month_number <= 9:
                registration_number_q3 += 1
                if registration_number_q3 <= 9:
                    invoice += "0"+str(registration_number_q3)+ "/"
                    registration_number_q3_invoice = "0"+str(registration_number_q3)
                elif registration_number_q3 >= 10:                        
                    invoice += str(registration_number_q3)+ "/"
                    registration_number_q3_invoice = str(registration_number_q3)
            elif month_number >= 10 and month_number <= 12:
                registration_number_q4 += 1
                if registration_number_q4 <= 9:
                    invoice += "0"+str(registration_number_q4)+ "/"
                    registration_number_q4_invoice = "0"+str(registration_number_q4)
                elif registration_number_q1 >= 10:
                    invoice += str(registration_number_q4)+ "/"
                    registration_number_q4_invoice = str(registration_number_q4)

            if month_number >= 1 and month_number <= 3:
                invoice += "1-"
                quartal_invoice = "1-"
            elif month_number >= 4 and month_number <= 6:
                invoice += "2-"
                quartal_invoice = "2-"
            elif month_number >= 7 and month_number <= 9:
                invoice += "3-"
                quartal_invoice = "3-"
            elif month_number >= 10 and month_number <= 12:
                invoice += "4-"
                quartal_invoice = "4-"

            year_number = datetime.datetime.now().year
            invoice += "{}".format(str(year_number)[-2:])
            quartal_invoice += "{}".format(str(year_number)[-2:])

            new_data.invoice = invoice
            new_data.nama_lengkap = nama_lengkap
            new_data.email = email
            new_data.nomor_telefon = nomor_telefon
            new_data.program_studi = program_studi
            new_data.universitas = universitas
            new_data.metode_pembelajaran = metode_pembelajaran
            new_data.mata_kuliah = mata_kuliah
            new_data.materi = materi
            new_data.aplikasi_simulasi = simulasi
            new_data.jumlah_sesi_yang_ingin_diikuti = form.cleaned_data['jumlah_sesi_yang_ingin_diikuti']
            
            jumlah_peserta = request.POST.get('jumlah_peserta')
            if jumlah_peserta == "Other":
                jumlah_peserta = request.POST.get('jumlah_peserta_lain')
            else:
                jumlah_peserta = request.POST.get('jumlah_peserta')
                
            new_data.jumlah_peserta = jumlah_peserta
            new_data.nama_anggota_kelompok_bagi_yang_kelompok = form.cleaned_data['nama_anggota_kelompok_bagi_yang_kelompok']
            new_data.alamat_email_anggota_kelompok = form.cleaned_data['alamat_email_anggota_kelompok']
            sesi_dan_jadwal = form.cleaned_data['sesi_dan_jadwal']
            new_data.notes_for_tutor = form.cleaned_data['notes_for_tutor']

            sesi_materi = []
            sesi_tanggal = []
            sesi_jam = []

            for i in range(len(sesi_dan_jadwal.split("],"))):
                sesi_materi.append(sesi_dan_jadwal.split("],")[i].split("[")[0].strip())
                sesi_tanggal.append(sesi_dan_jadwal.split("],")[i].split("[")[1].split(",")[0])
                sesi_jam.append(sesi_dan_jadwal.split("],")[i].split(",")[1].replace(" ", "").replace("]", ""))

            new_data.sesi_materi = sesi_materi
            new_data.sesi_tanggal = sesi_tanggal
            new_data.sesi_jam = sesi_jam

            biaya = 0
            if int(jumlah_peserta) <= 3:
                biaya += (175000 * len(sesi_materi))
            elif int(jumlah_peserta) == 4:
                biaya += (200000 * len(sesi_materi))
            elif int(jumlah_peserta) == 5:
                biaya += (250000 * len(sesi_materi))
            elif int(jumlah_peserta) >= 6:
                biaya += ((250000 + ((int(jumlah_peserta) - 5) * 40000)) * len(sesi_materi))
            new_data.biaya = "{:0,.0f}".format(biaya)

            referral_code = form.cleaned_data['referral_code']
            data_referral_code = ReferralCode.objects.all()
            data_referral_code_list = []
            for i in data_referral_code:
                data_referral_code_list.append(i.referral_code)
            if referral_code in data_referral_code_list:
                new_data.referral_code = form.cleaned_data['referral_code']

            bulan = ""
            if datetime.datetime.now().month == 1:
                bulan = "Januari"
            elif datetime.datetime.now().month == 2:
                bulan = "Februari"
            elif datetime.datetime.now().month == 3:
                bulan = "Maret"
            elif datetime.datetime.now().month == 4:
                bulan = "April"
            elif datetime.datetime.now().month == 5:
                bulan = "Mei"
            elif datetime.datetime.now().month == 6:
                bulan = "Juni"
            elif datetime.datetime.now().month == 7:
                bulan = "Juli"
            elif datetime.datetime.now().month == 8:
                bulan = "Agustus"
            elif datetime.datetime.now().month == 9:
                bulan = "September"
            elif datetime.datetime.now().month == 10:
                bulan = "Oktober"
            elif datetime.datetime.now().month == 11:
                bulan = "November"
            elif datetime.datetime.now().month == 12:
                bulan = "Desember"

            tanggal = str(datetime.datetime.now().day) + " " + bulan + " " + str(datetime.datetime.now().year)
            new_data.tanggal = tanggal

            try:
                new_data.save()
            except:
                return redirect("pendaftaran_gagal")

            if month_number >= 1 and month_number <= 3:
                return redirect("send_email_q1", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, simulasi, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q1_invoice, quartal_invoice)
            elif month_number >= 4 and month_number <= 6:
                return redirect("send_email_q2", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, simulasi, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q2_invoice, quartal_invoice)
            elif month_number >= 7 and month_number <= 9:
                return redirect("send_email_q3", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, simulasi, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q3_invoice, quartal_invoice)
            elif month_number >= 10 and month_number <= 12:
                return redirect("send_email_q4", nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, simulasi, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice)
    else:
        form = JumlahPeserta(request.POST)
    return render(request, "FormRegistrationApp/jumlah_peserta.html", context)

"""def get_data(request):
    data = RegistrationData.objects.all()
    context={
      'my_data':data,
    }
    return render(request, 'FormRegistrationApp/get_data.html', context)"""

def create_pdf_assignment(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def invoice_assignment_q1(request, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q1_invoice, quartal_invoice):
    data = RegistrationData.objects.get(invoice="Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q1_invoice, quartal_invoice))
    sesi_materi = data.sesi_materi.replace("[", "").replace("]", "").replace("'", "")
    #sesi_materi = list(data.sesi_materi.replace("[", "").replace("]", "").replace("'", "").split(", "))
    sesi_tanggal = list(data.sesi_tanggal.replace("[", "").replace("]", "").replace("'", ""))
    sesi_jam = list(data.sesi_jam.replace("[", "").replace("]", "").replace("'", ""))
    context={
        'i': data,
        'sesi_materi': sesi_materi,
        'sesi_tanggal': sesi_tanggal,
        'sesi_jam': sesi_jam
    }
    pdf = create_pdf_assignment('FormRegistrationApp/template_pdf_assignment.html', context)
    response = HttpResponse(pdf, content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="Inv/{}/{}/{}/{}/{}.pdf"'.format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q1_invoice, quartal_invoice)
    return response
    #return render(request, 'FormRegistrationApp/template_pdf_assignment.html', context)

def invoice_assignment_q2(request, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q2_invoice, quartal_invoice):
    data = RegistrationData.objects.get(invoice="Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q2_invoice, quartal_invoice))
    sesi_materi = data.sesi_materi.replace("[", "").replace("]", "").replace("'", "")
    #sesi_materi = list(data.sesi_materi.replace("[", "").replace("]", "").replace("'", "").split(", "))
    sesi_tanggal = list(data.sesi_tanggal.replace("[", "").replace("]", "").replace("'", ""))
    sesi_jam = list(data.sesi_jam.replace("[", "").replace("]", "").replace("'", ""))
    context={
        'i': data,
        'sesi_materi': sesi_materi,
        'sesi_tanggal': sesi_tanggal,
        'sesi_jam': sesi_jam
    }
    pdf = create_pdf_assignment('FormRegistrationApp/template_pdf_assignment.html', context)
    response = HttpResponse(pdf, content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="Inv/{}/{}/{}/{}/{}.pdf"'.format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q2_invoice, quartal_invoice)
    return response
    #return render(request, 'FormRegistrationApp/template_pdf_assignment.html', context)

def invoice_assignment_q3(request, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q3_invoice, quartal_invoice):
    data = RegistrationData.objects.get(invoice="Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q3_invoice, quartal_invoice))
    sesi_materi = data.sesi_materi.replace("[", "").replace("]", "").replace("'", "")
    #sesi_materi = list(data.sesi_materi.replace("[", "").replace("]", "").replace("'", "").split(", "))
    sesi_tanggal = list(data.sesi_tanggal.replace("[", "").replace("]", "").replace("'", ""))
    sesi_jam = list(data.sesi_jam.replace("[", "").replace("]", "").replace("'", ""))
    context={
        'i': data,
        'sesi_materi': sesi_materi,
        'sesi_tanggal': sesi_tanggal,
        'sesi_jam': sesi_jam
    }
    pdf = create_pdf_assignment('FormRegistrationApp/template_pdf_assignment.html', context)
    response = HttpResponse(pdf, content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="Inv/{}/{}/{}/{}/{}.pdf"'.format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q3_invoice, quartal_invoice)
    return response
    #return render(request, 'FormRegistrationApp/template_pdf_assignment.html', context)

def invoice_assignment_q4(request, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice):
    data = RegistrationData.objects.get(invoice="Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice))
    sesi_materi = data.sesi_materi.replace("[", "").replace("]", "").replace("'", "")
    #sesi_materi = list(data.sesi_materi.replace("[", "").replace("]", "").replace("'", "").split(", "))
    sesi_tanggal = list(data.sesi_tanggal.replace("[", "").replace("]", "").replace("'", ""))
    sesi_jam = list(data.sesi_jam.replace("[", "").replace("]", "").replace("'", ""))
    context={
        'i': data,
        'sesi_materi': sesi_materi,
        'sesi_tanggal': sesi_tanggal,
        'sesi_jam': sesi_jam
    }
    pdf = create_pdf_assignment('FormRegistrationApp/template_pdf_assignment.html', context)
    response = HttpResponse(pdf, content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="Inv/{}/{}/{}/{}/{}.pdf"'.format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice)
    return response
    #return render(request, 'FormRegistrationApp/template_pdf_assignment.html', context)

"""def invoice_q1(request, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice):
    data = RegistrationData.objects.get(invoice="Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice))
    sesi_materi = data.sesi_materi.replace("[", "").replace("]", "").replace("'", "")
    #sesi_materi = list(data.sesi_materi.replace("[", "").replace("]", "").replace("'", "").split(", "))
    context={
        'i': data,
        'sesi_materi': sesi_materi,
    }
    return render(request, 'FormRegistrationApp/invoice.html', context)

def invoice_q2(request, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice):
    data = RegistrationData.objects.get(invoice="Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice))
    sesi_materi = data.sesi_materi.replace("[", "").replace("]", "").replace("'", "")
    #sesi_materi = list(data.sesi_materi.replace("[", "").replace("]", "").replace("'", "").split(", "))
    context={
        'i': data,
        'sesi_materi': sesi_materi,
    }
    return render(request, 'FormRegistrationApp/invoice.html', context)

def invoice_q3(request, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q3_invoice, quartal_invoice):
    data = RegistrationData.objects.get(invoice="Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q3_invoice, quartal_invoice))
    sesi_materi = data.sesi_materi.replace("[", "").replace("]", "").replace("'", "")
    #sesi_materi = list(data.sesi_materi.replace("[", "").replace("]", "").replace("'", "").split(", "))
    context={
        'i': data,
        'sesi_materi': sesi_materi,
    }
    print(data.sesi_materi)
    return render(request, 'FormRegistrationApp/invoice.html', context)

def invoice_q4(request, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice):
    data = RegistrationData.objects.get(invoice="Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice))
    sesi_materi = data.sesi_materi.replace("[", "").replace("]", "").replace("'", "")
    #sesi_materi = list(data.sesi_materi.replace("[", "").replace("]", "").replace("'", "").split(", "))
    context={
        'i': data,
        'sesi_materi': sesi_materi,
    }
    return render(request, 'FormRegistrationApp/invoice.html', context)"""

def create_pdf(context):
    html = render_to_string('FormRegistrationApp/template_pdf.html', context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return result.getvalue()
    return None

def send_email_q1(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q1_invoice, quartal_invoice):
    data = RegistrationData.objects.get(invoice="Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q1_invoice, quartal_invoice))
    sesi_materi = data.sesi_materi.replace("[", "").replace("]", "").replace("'", "")
    #sesi_materi = list(data.sesi_materi.replace("[", "").replace("]", "").replace("'", "").split(", "))
    context={
        'i': data,
        'sesi_materi': sesi_materi,
    }
    subject = "Torche Class Registration Form - Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q1_invoice, quartal_invoice)
    message = "Terimakasih {}, anda telah memilih kelas {} dengan materi {}, untuk invoice dapat dilihat pada file berikut".format(nama_lengkap, mata_kuliah, sesi_materi)
    emails = [email]
    pdf = create_pdf(context)
    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, emails)
    mail.attach("Inv/{}/{}/{}/{}/{}.pdf".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q1_invoice, quartal_invoice), pdf, 'application/pdf')
    mail.send(fail_silently = False)
    return redirect("pendaftaran_berhasil")

def send_email_q2(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q2_invoice, quartal_invoice):
    data = RegistrationData.objects.get(invoice="Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q2_invoice, quartal_invoice))
    sesi_materi = data.sesi_materi.replace("[", "").replace("]", "").replace("'", "")
    #sesi_materi = list(data.sesi_materi.replace("[", "").replace("]", "").replace("'", "").split(", "))
    context={
        'i': data,
        'sesi_materi': sesi_materi,
    }
    subject = "Torche Class Registration Form - Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q2_invoice, quartal_invoice)
    message = "Terimakasih {}, anda telah memilih kelas {} dengan materi {}, untuk invoice dapat dilihat pada file berikut".format(nama_lengkap, mata_kuliah, sesi_materi)
    emails = [email]
    pdf = create_pdf(context)
    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, emails)
    mail.attach("Inv/{}/{}/{}/{}/{}.pdf".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q1_invoice, quartal_invoice), pdf, 'application/pdf')
    mail.send(fail_silently = False)
    return redirect("pendaftaran_berhasil")

def send_email_q3(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q3_invoice, quartal_invoice):
    data = RegistrationData.objects.get(invoice="Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q3_invoice, quartal_invoice))
    sesi_materi = data.sesi_materi.replace("[", "").replace("]", "").replace("'", "")
    #sesi_materi = list(data.sesi_materi.replace("[", "").replace("]", "").replace("'", "").split(", "))
    context={
        'i': data,
        'sesi_materi': sesi_materi,
    }
    subject = "Torche Class Registration Form - Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q3_invoice, quartal_invoice)
    message = "Terimakasih {}, anda telah memilih kelas {} dengan materi {}, untuk invoice dapat dilihat pada file berikut".format(nama_lengkap, mata_kuliah, sesi_materi)
    emails = [email]
    pdf = create_pdf(context)
    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, emails)
    mail.attach("Inv/{}/{}/{}/{}/{}.pdf".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q3_invoice, quartal_invoice), pdf, 'application/pdf')
    mail.send(fail_silently = False)
    return redirect("pendaftaran_berhasil")

def send_email_q4(request, nama_lengkap, email, nomor_telefon, program_studi, universitas, metode_pembelajaran, mata_kuliah, materi, jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice):
    data = RegistrationData.objects.get(invoice="Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice))
    sesi_materi = data.sesi_materi.replace("[", "").replace("]", "").replace("'", "")
    #sesi_materi = list(data.sesi_materi.replace("[", "").replace("]", "").replace("'", "").split(", "))
    context={
        'i': data,
        'sesi_materi': sesi_materi,
    }
    subject = "Torche Class Registration Form - Inv/{}/{}/{}/{}/{}".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q4_invoice, quartal_invoice)
    message = "Terimakasih {}, anda telah memilih kelas {} dengan materi {}, untuk invoice dapat dilihat pada file berikut".format(nama_lengkap, mata_kuliah, sesi_materi)
    emails = [email]
    pdf = create_pdf(context)
    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, emails)
    mail.attach("Inv/{}/{}/{}/{}/{}.pdf".format(jumlah_peserta_invoice, metode_pembelajaran_invoice, mata_kuliah_invoice, registration_number_q1_invoice, quartal_invoice), pdf, 'application/pdf')
    mail.send(fail_silently = False)
    return redirect("pendaftaran_berhasil")

def pendaftaran_berhasil(request):
    return render(request, 'FormRegistrationApp/pendaftaran_berhasil.html')
    
def pendaftaran_gagal(request):
    return render(request, 'FormRegistrationApp/pendaftaran_gagal.html')