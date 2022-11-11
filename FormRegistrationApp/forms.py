from django import forms

class MetodePembelajaranForm(forms.Form):
    METODE_PEMBELAJARAN = (
        ("Lecturing Class", "Lecturing Class"),
        ("Consultation Class", "Consultation Class"),
        ("Exam Preparation Class", "Exam Preparation Class"),
    )

    JUMLAH_SESI = (
        ("1", "1"),
        ("2", "2"),
        ("4", "4"),
        ("6", "6"),
        ("8", "8"),
        ("10", "10")
    )

    metode_pembelajaran = forms.ChoiceField(widget=forms.RadioSelect, choices=METODE_PEMBELAJARAN)
    jumlah_sesi_yang_diikuti = forms.ChoiceField(widget=forms.RadioSelect, choices=JUMLAH_SESI)

#--------------------------------------------------------------------------------------------

# Cell Culture for Engineers
class SessionCCEForm(forms.Form):
    SESSION_CCE = (
        ("Tissue Culture", "Tissue Culture"),
    )
    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_CCE)

# Chemical Engineering Mathematics
class SessionCEMForm(forms.Form):
    SESSION_CEM = (
        ("Ordinary Differential Equations: First Order Equations", "Ordinary Differential Equations: First Order Equations"),
    )
    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_CEM)

# Chemical Engineering Thermodynamics
class SessionCETForm(forms.Form):
    SESSION_CET = (
        ("PVT of A Pure Substance and Steam Table", "PVT of A Pure Substance and Steam Table"),
    )
    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_CET)

# Chemical Process Simulation
class SessionCPSForm(forms.Form):
    SESSION_CPS = (
        ("HYSYS Thermodynamics and Streams", "HYSYS Thermodynamics and Streams"),
    )

    SIMULATION_SOFTWARE = (
        ("UniSim Design", "UniSim Design"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_CPS)
    simulasi = forms.ChoiceField(widget=forms.RadioSelect, choices=SIMULATION_SOFTWARE)

# Chemical Reaction Engineering
class SessionCREForm(forms.Form):
    SESSION_CRE = (
        ("Mole Balances and Rate Law", "Mole Balances and Rate Law"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_CRE)

# Engineering Economy
class SessionEECForm(forms.Form):
    SESSION_EEC = (
        ("Time Value of Money", "Time Value of Money"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_EEC)

# Fundamentals of Analytical Chemistry
class SessionFACForm(forms.Form):
    SESSION_FAC = (
        ("Gravimetric Methods of Analysis", "Gravimetric Methods of Analysis"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FAC)

# Fundamentals of Calculus
class SessionFCAForm(forms.Form):
    SESSION_FCA = (
        ("Basics of Calculus: Numbers and Functions", "Basics of Calculus: Numbers and Functions"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FCA)

# Fundamentals of Chemistry
class SessionFCHForm(forms.Form):
    SESSION_FCH = (
        ("Atoms and the Atomic Theory", "Atoms and the Atomic Theory"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FCH)

# Fundamentals of Heat Transfer
class SessionFHTForm(forms.Form):
    SESSION_FHT = (
        ("Introduction to Heat Transfer", "Introduction to Heat Transfer"),
    ) 

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FHT)

# Fundamentals of Mass Transfer
class SessionFMTForm(forms.Form):
    SESSION_FMT = (
        ("Mass Transfer and Diffusion", "Mass Transfer and Diffusion"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FMT)

# Fluid and Particles Mechanics
class SessionFPMForm(forms.Form):
    SESSION_FPM = (
        ("Properties of Fluid", "Properties of Fluid"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FPM)

# Fundamentals of Physics 1: Mechanics & Heats
class SessionFP1Form(forms.Form):
    SESSION_FP1 = (
        ("Kinematics", "Kinematics"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FP1)

# Fundamentals of Physics 2: Magnets, Electrics, Waves, Optics
class SessionFP2Form(forms.Form):
    SESSION_FP2 = (
        ("Electrostatics", "Electrostatics"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FP2)

# Mass and Energy Balances
class SessionMEBForm(forms.Form):
    SESSION_MEB = (
        ("Introduction to Material and Energy Balances", "Introduction to Material and Energy Balances"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_MEB)

# Numerical Computation for Engineers
class SessionNCEForm(forms.Form):
    SESSION_NCE = (
        ("Numerical Solutions of Nonlinear Equations", "Numerical Solutions of Nonlinear Equations"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_NCE)

# Organic Chemistry for Engineers
class SessionOCEForm(forms.Form):
    SESSION_OCE = (
        ("Atoms and Molecules", "Atoms and Molecules"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_OCE)

# Process Control and Dynamics
class SessionPCDForm(forms.Form):
    SESSION_PCD = (
        ("Theoretical Models of Chemical Processes", "Theoretical Models of Chemical Processes"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_PCD)

# Physical Chemistry
class SessionPCHForm(forms.Form):
    SESSION_PCH = (
        ("Physical and Chemical Properties of Solutions", "Physical and Chemical Properties of Solutions"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_PCH)

# Product Design and Development
class SessionPDDForm(forms.Form):
    SESSION_PDD = (
        ("Development Processes and Organizations", "Development Processes and Organizations"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_PDD)

# Process Equipment Design
class SessionPEDForm(forms.Form):
    SESSION_PED = (
        ("Fluid Transport Equipment: Piping Systems", "Fluid Transport Equipment: Piping Systems"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_PED)

# Process Plant Design
class SessionPPDForm(forms.Form):
    SESSION_PPD = (
        ("Process Synthesis", "Process Synthesis"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_PPD)

# Statistics and Probability
class SessionSPRForm(forms.Form):
    SESSION_SPR = (
        ("Introduction to Statistics", "Introduction to Statistics"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_SPR)

# Transport Phenomena
class SessionTPHForm(forms.Form):
    SESSION_TPH = (
        ("Introduction to Transport Phenomena", "Introduction to Transport Phenomena"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_TPH)

class JadwalBelajarForm(forms.Form):
    SESI_HARI = (
        ("Senin", "Senin"),
        ("Selasa", "Selasa"),
        ("Rabu", "Rabu"),
        ("Kamis", "Kamis"),
        ("Jumat", "Jumat"),
        ("Sabtu", "Sabtu"),
        ("Minggu", "Minggu")
    )

    SESI_JAM = (
        ("Session 1 (08:00 - 10:00)", "Session 1 (08:00 - 10:00)"),
        ("Session 2 (10:00 - 12:00)", "Session 2 (10:00 - 12:00)"),
        ("Session 3 (14:00 - 16:00)", "Session 3 (14:00 - 16:00)"),
        ("Session 4 (16:00 - 18:00)", "Session 4 (16:00 - 18:00)"),
        ("Session 5 (19:00 - 21:00)", "Session 5 (19:00 - 21:00)"),
        ("Session 6 (21:00 - 23:00)", "Session 6 (21:00 - 23:00)")
    )
    sesi_hari = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESI_HARI)
    sesi_jam = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESI_JAM)
    notes_for_tutor = forms.CharField(widget=forms.Textarea(), required=False)
    referral_code = forms.CharField(max_length=254, required=False)
    lampiran = forms.FileField(required=False)

class LampiranFileForm(forms.Form):
    lampiran = forms.FileField()