from django import forms
from django.db.models import fields
from .models import RegistrationData
from django.core.validators import RegexValidator

class CourseRegistrationForm(forms.Form):
    """PROGRAM_STUDI = (
        ("S1 Teknik Kimia", "S1 Teknik Kimia"),
        ("S1 Teknologi Bioproses", "S1 Teknologi Bioproses"),
        ("S2 Teknik Kimia", "S2 Teknik Kimia"),
        ("S3 Teknik Kimia", "S3 Teknik Kimia"),
        ("Other", "Other")
    )"""

    """UNIVERSITAS = (
        ("Universitas Indonesia", "Universitas Indonesia"),
        ("Universitas Muhammadiyah Surakarta", "Universitas Muhammadiyah Surakarta"),
        ("Universitas Sriwijaya", "Universitas Sriwijaya"),
        ("Institut Teknologi Bandung", "Institut Teknologi Bandung"),
        ("Institut Teknologi Sepuluh Nopember", "Institut Teknologi Sepuluh Nopember")
    )"""

    email = forms.EmailField(max_length=254)
    nama_lengkap = forms.CharField(max_length=254)
    nomor_telefon = forms.CharField(max_length=254)
    #program_studi = forms.ChoiceField(widget=forms.RadioSelect, choices=PROGRAM_STUDI)
    #universitas = forms.ChoiceField(widget=forms.RadioSelect, choices=UNIVERSITAS)

class MetodePembelajaranForm(forms.Form):
    METODE_PEMBELAJARAN = (
        ("Kelas Konsultasi", "Kelas Konsultasi"),
        ("Kelas Materi", "Kelas Materi"),
        ("Persiapan Ujian", "Persiapan Ujian"),
        ("Konsultasi Perlombaan", "Konsultasi Perlombaan"),
        ("Konsultasi Skripsi atau Tesis", "Konsultasi Skripsi atau Tesis"),
    )

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

    metode_pembelajaran = forms.ChoiceField(widget=forms.RadioSelect, choices=METODE_PEMBELAJARAN)
    mata_kuliah = forms.ChoiceField(widget=forms.RadioSelect, choices=NAMA_MATA_KULIAH)
    jumlah_sesi_yang_ingin_diikuti = forms.CharField(max_length=254)

# Cell Culture for Engineers
class SessionCSEForm(forms.Form):
    SESSION_CSE = (
        ("Tissue Culture", "Tissue Culture"),
        ("Animal Cell Culture", "Animal Cell Culture"),
        ("Cell Culture Contamination", "Cell Culture Contamination"),
        ("Bioprocess Cell Culture", "Bioprocess Cell Culture")
    )
    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_CSE)

# Chemical Engineering Mathematics
class SessionCEMForm(forms.Form):
    SESSION_CEM = (
        ("Ordinary Differential Equations: First Order Equations", "Ordinary Differential Equations: First Order Equations"),
        ("Ordinary Differential Equations: Second Order Nonlinear Equations", "Ordinary Differential Equations: Second Order Nonlinear Equations"),
        ("Ordinary Differential Equations: Linear Equations of Higher Order", "Ordinary Differential Equations: Linear Equations of Higher Order"),
        ("Coupled Simultaneous Ordinary Differential Equations", "Coupled Simultaneous Ordinary Differential Equations"),
        ("Series Solution Methods", "Series Solution Methods"),
        ("Solution Techniques for Models Producing Partial Differential Equations (PDEs)", "Solution Techniques for Models Producing Partial Differential Equations (PDEs)")
    )
    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_CEM)

# Chemical Engineering Thermodynamics
class SessionCETForm(forms.Form):
    SESSION_CET = (
        ("PVT of A Pure Substance and Steam Table", "PVT of A Pure Substance and Steam Table"),
        ("1st Law of Thermodynamics", "1st Law of Thermodynamics"),
        ("2nd Law of Thermodynamics", "2nd Law of Thermodynamics"),
        ("Applications of Thermodynamics to The Process Engineering", "Applications of Thermodynamics to The Process Engineering"),
        ("Vapor-Liquid Equilibrium for Ideal Solution", "Vapor-Liquid Equilibrium for Ideal Solution"),
        ("Solution Thermodynamics", "Solution Thermodynamics"),
        ("Vapor-Liquid Equilibrium for Non-Ideal Solution", "Vapor-Liquid Equilibrium for Non-Ideal Solution"),
        ("Chemical Reaction Equilibria", "Chemical Reaction Equilibria")
    )
    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_CET)

# Chemical Process Simulation
class SessionCPSForm(forms.Form):
    SESSION_CPS = (
        ("HYSYS Thermodynamics and Streams", "HYSYS Thermodynamics and Streams"),
        ("Heat Tranfer Operations", "Heat Tranfer Operations"),
        ("Piping Operations", "Piping Operations"),
        ("Rotating Equipment", "Rotating Equipment"),
        ("Separation Operations", "Separation Operations"),
        ("Column Operations", "Column Operations"),
        ("Solid Separation Operations", "Solid Separation Operations"),
        ("Reactor Operations", "Reactor Operations"),
        ("Logical Operations", "Logical Operations"),
        ("Case Study 01: Synthesis Gas Production Plant", "Case Study 01: Synthesis Gas Production Plant"),
        ("Case Study 02: Acid Gas Sweetening with DEA Plant", "Case Study 02: Acid Gas Sweetening with DEA Plant"),
        ("Case Study 03: Gas Processing Plant", "Case Study 03: Gas Processing Plant"),
        ("Case Study 04: Dynamic Gas Processing Plant", "Case Study 04: Dynamic Gas Processing Plant"),
        ("Case Study 05: NGL Fractination Train", "Case Study 05: NGL Fractination Train")
    )

    SIMULATION_SOFTWARE = (
        ("UniSim Design", "UniSim Design"),
        ("Aspen HYSYS", "Aspen HYSYS"),
        ("Aspen Plus", "Aspen Plus"),
        ("SuperPro Designer", "SuperPro Designer")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_CPS)
    simulasi = forms.ChoiceField(widget=forms.RadioSelect, choices=SIMULATION_SOFTWARE)

# Chemical Reaction Engineering
class SessionCREForm(forms.Form):
    SESSION_CRE = (
        ("Mole Balances and Rate Law", "Mole Balances and Rate Law"),
        ("Collection and Analysis of Rate Data", "Collection and Analysis of Rate Data"),
        ("Reaction Mechanism, Pathways, Bioreactions, and Bioreactors", "Reaction Mechanism, Pathways, Bioreactions, and Bioreactors"),
        ("Catalysis and Catalytic Reactors", "Catalysis and Catalytic Reactors"),
        ("External Diffusion Effects on Heterogeneous Reactions", "External Diffusion Effects on Heterogeneous Reactions"),
        ("Diffusion and Reaction", "Diffusion and Reaction"),
        ("Conversion and Reactor Sizing", "Conversion and Reactor Sizing"),
        ("Steady-State Isothermal Reactor Design", "Steady-State Isothermal Reactor Design"),
        ("Multiple Reactions", "Multiple Reactions"),
        ("Steady-State Nonisothermal Reactor Design", "Steady-State Nonisothermal Reactor Design"),
        ("Distribution of Residence Times for Chemical Reactors", "Distribution of Residence Times for Chemical Reactors"),
        ("Models for Nonideal Reactors", "Models for Nonideal Reactors")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_CRE)

# Engineering Economy
class SessionEECForm(forms.Form):
    SESSION_EEC = (
        ("Time Value of Money", "Time Value of Money"),
        ("Interest Rates", "Interest Rates"),
        ("Present Worth and Annual Worth Analysis", "Present Worth and Annual Worth Analysis"),
        ("Rate of Return Analysis", "Rate of Return Analysis"),
        ("Benefit/Cost Analysis", "Benefit/Cost Analysis"),
        ("Project Financing and Noneconomic Attributes", "Project Financing and Noneconomic Attributes"),
        ("Effect of Inflation", "Effect of Inflation"),
        ("Cost Estimation and Indirect Cost Allocation", "Cost Estimation and Indirect Cost Allocation"),
        ("Depreciation Method", "Depreciation Method"),
        ("After-Tax Economic Analysis", "After-Tax Economic Analysis"),
        ("Sensitivity Analysis", "Sensitivity Analysis")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_EEC)

# Fundamentals of Analytical Chemistry
class SessionFACForm(forms.Form):
    SESSION_FAC = (
        ("Gravimetric Methods of Analysis", "Gravimetric Methods of Analysis"),
        ("Titrations in Analytical Chemistry", "Titrations in Analytical Chemistry"),
        ("Neutralization Titration", "Neutralization Titration"),
        ("Electrochemical Methods", "Electrochemical Methods"),
        ("Potentiometry", "Potentiometry"),
        ("Spectrochemical: Introduction", "Spectrochemical: Introduction"),
        ("Spectrochemical: Optical Spectrometry", "Spectrochemical: Optical Spectrometry"),
        ("Molecular Absorption Spectrometry", "Molecular Absorption Spectrometry"),
        ("Atomic Spectroscopy", "Atomic Spectroscopy"),
        ("Mass Spectroscopy", "Mass Spectroscopy"),
        ("Gas Chromatography", "Gas Chromatography"),
        ("High Performance Liquid Chromatography (HPLC)", "High Performance Liquid Chromatography (HPLC)")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FAC)

# Fundamentals of Calculus
class SessionFCAForm(forms.Form):
    SESSION_FCA = (
        ("Basics of Calculus: Numbers and Functions", "Basics of Calculus: Numbers and Functions"),
        ("Limits", "Limits"),
        ("Derivatives and its Application", "Derivatives and its Application"),
        ("Integral and its Application", "Integral and its Application"),
        ("Transcendental Function", "Transcendental Function"),
        ("Advanced Techniques of Integration", "Advanced Techniques of Integration"),
        ("Indeterminate Forms and Improper Integrals", "Indeterminate Forms and Improper Integrals"),
        ("Infinite Series", "Infinite Series"),
        ("Conics and Polar Coordinates", "Conics and Polar Coordinates"),
        ("Geometry in Space and Vectors", "Geometry in Space and Vectors"),
        ("Derivatives for Functions of Two or More Variables", "Derivatives for Functions of Two or More Variables"),
        ("Multiple Integrals", "Multiple Integrals")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FCA)

# Fundamentals of Chemistry
class SessionFCHForm(forms.Form):
    SESSION_FCH = (
        ("Atoms and the Atomic Theory", "Atoms and the Atomic Theory"),
        ("The Periodic Table and Some Atomic Properties", "The Periodic Table and Some Atomic Properties"),
        ("Chemical Reactions", "Chemical Reactions"),
        ("Chemical Reactions in Aqueous Solutions", "Chemical Reactions in Aqueous Solutions"),
        ("Gases", "Gases"),
        ("Thermochemistry", "Thermochemistry"),
        ("Principles of Chemical Equilibrium", "Principles of Chemical Equilibrium"),
        ("Acids and Bases", "Acids and Bases"),
        ("Acid-Base Equilibria", "Acid-Base Equilibria"),
        ("Solubility and Complex-Ion Equilibria", "Solubility and Complex-Ion Equilibria"),
        ("Electrochemistry", "Electrochemistry"),
        ("Chemical Kinetics", "Chemical Kinetics")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FCH)

# Fundamentals of Heat Transfer
class SessionFHTForm(forms.Form):
    SESSION_FHT = (
        ("Introduction to Heat Transfer", "Introduction to Heat Transfer"),
        ("One Dimensional Steady-State Conduction without Heat Generation", "One Dimensional Steady-State Conduction without Heat Generation"),
        ("One Dimensional Steady-State Conduction with Heat Generation", "One Dimensional Steady-State Conduction with Heat Generation"),
        ("Two Dimensional Steady-State Conduction", "Two Dimensional Steady-State Conduction"),
        ("Unsteady-State Conduction", "Unsteady-State Conduction"),
        ("Principles of Convection", "Principles of Convection"),
        ("Forced Convection Systems: External Flow", "Forced Convection Systems: External Flow"),
        ("Forced Convection Systems: Internal Flow", "Forced Convection Systems: Internal Flow"),
        ("Natural Convection Systems", "Natural Convection Systems"),
        ("Boiling and Condensation", "Boiling and Condensation"),
        ("Heat Exchangers", "Heat Exchangers"),
        ("Radiation: Processes and Properties", "Radiation: Processes and Properties"),
        ("Radiation: Exchange Between Surfaces", "Radiation: Exchange Between Surfaces")
    ) 

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FHT)

# Fundamentals of Mass Transfer
class SessionFMTForm(forms.Form):
    SESSION_FMT = (
        ("Mass Transfer and Diffusion", "Mass Transfer and Diffusion"),
        ("Single Equilibrium Stages and Flash Calculations", "Single Equilibrium Stages and Flash Calculations"),
        ("Multistage Cascades", "Multistage Cascades"),
        ("Batch Distillation", "Batch Distillation"),
        ("Binary Mixtures Distillation: McCabe-Thiele Method", "Binary Mixtures Distillation: McCabe-Thiele Method"),
        ("Multicomponent Distillation: Fenske-Underwood-Gilliland Method", "Multicomponent Distillation: Fenske-Underwood-Gilliland Method"),
        ("Absorption and Stripping", "Absorption and Stripping"),
        ("Liquid-Liquid Extraction", "Liquid-Liquid Extraction"),
        ("Humidification Operations", "Humidification Operations"),
        ("Drying of Solids", "Drying of Solids"),
        ("Adsorption Operations", "Adsorption Operations"),
        ("Membrane Separations", "Membrane Separations")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FMT)

# Fluid and Particles Mechanics
class SessionFPMForm(forms.Form):
    SESSION_FPM = (
        ("Properties of Fluid", "Properties of Fluid"),
        ("Basic Equation of Fluid Flow", "Basic Equation of Fluid Flow"),
        ("Fluid Statics", "Fluid Statics"),
        ("Flow of Incompressible Fluid in Pipes", "Flow of Incompressible Fluid in Pipes"),
        ("Pumps", "Pumps"),
        ("Flow of Compressible Fluid", "Flow of Compressible Fluid"),
        ("Blowers and Compressors", "Blowers and Compressors"),
        ("Agitation and Mixing of Liquids", "Agitation and Mixing of Liquids"),
        ("Rheological Properties of Fluids", "Rheological Properties of Fluids"),
        ("Boundary Layer", "Boundary Layer"),
        ("Motion of Particles in a Fluid", "Motion of Particles in a Fluid"),
        ("Fixed Beds and Fluidized Beds", "Fixed Beds and Fluidized Beds"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FPM)

# Fundamentals of Physics 1: Mechanics & Heats
class SessionFP1Form(forms.Form):
    SESSION_FP1 = (
        ("Kinematics", "Kinematics"),
        ("Dynamics of Particle", "Dynamics of Particle"),
        ("Work and Energy", "Work and Energy"),
        ("Dynamics of Rotational Motion", "Dynamics of Rotational Motion"),
        ("Elasticity and Oscillation", "Elasticity and Oscillation"),
        ("Waves", "Waves"),
        ("Fluid Statics and Dynamics", "Fluid Statics and Dynamics"),
        ("The Kinetic Theory of Gases", "The Kinetic Theory of Gases"),
        ("Thermodynamics", "Thermodynamics"),
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FP1)

# Fundamentals of Physics 2: Magnets, Electrics, Waves, Optics
class SessionFP2Form(forms.Form):
    SESSION_FP2 = (
        ("Electrostatics", "Electrostatics"),
        ("Magnetostatics", "Magnetostatics"),
        ("Induction and Inductance", "Induction and Inductance"),
        ("Electromagnetic Waves", "Electromagnetic Waves"),
        ("Interference and Diffraction of Light Waves", "Interference and Diffraction of Light Waves"),
        ("Modern Physics", "Modern Physics")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_FP2)

# Mass and Energy Balances
class SessionMEBForm(forms.Form):
    SESSION_MEB = (
        ("Introduction to Material and Energy Balances", "Introduction to Material and Energy Balances"),
        ("Material Balances for Single Unit without Chemical Reaction", "Material Balances for Single Unit without Chemical Reaction"),
        ("Material Balances for Multiple Unit without Chemical Reaction", "Material Balances for Multiple Unit without Chemical Reaction"),
        ("Material Balances for Processes Involving Chemical Reaction: Species and Elements Balances", "Material Balances for Processes Involving Chemical Reaction: Species and Elements Balances"),
        ("Material Balances for Processes Involving Chemical Reaction: Application", "Material Balances for Processes Involving Chemical Reaction: Application"),
        ("Single-Phase Systems", "Single-Phase Systems"),
        ("Multiphase Systems", "Multiphase Systems"),
        ("Energy Balances for Processes without Chemical Reaction: Introduction", "Energy Balances for Processes without Chemical Reaction: Introduction"),
        ("Energy Balances for Processes without Chemical Reaction: Enthalpy and Phase Changes", "Energy Balances for Processes without Chemical Reaction: Enthalpy and Phase Changes"),
        ("Energy Balances for Processes Involving Chemical Reaction: Heat of Reaction", "Energy Balances for Processes Involving Chemical Reaction: Heat of Reaction"),
        ("Energy Balances for Processes Involving Chemical Reaction: Application", "Energy Balances for Processes Involving Chemical Reaction: Application"),
        ("Material and Energy on Transient Processes", "Material and Energy on Transient Processes")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_MEB)

# Numerical Computation for Engineers
class SessionNCEForm(forms.Form):
    SESSION_NCE = (
        ("Numerical Solutions of Nonlinear Equations", "Numerical Solutions of Nonlinear Equations"),
        ("Simultaneous Linear Algebraic Equations", "Simultaneous Linear Algebraic Equations"),
        ("Finite Differences Methods", "Finite Differences Methods"),
        ("Numerical Differentiation", "Numerical Differentiation"),
        ("Numerical Integration", "Numerical Integration"),
        ("Numerical Solution of Ordinary Differential Equations: Initial-Value Problems", "Numerical Solution of Ordinary Differential Equations: Initial-Value Problems"),
        ("Numerical Solution of Ordinary Differential Equations: Boundary-Value Problems", "Numerical Solution of Ordinary Differential Equations: Boundary-Value Problems"),
        ("Numerical Solution of Partial Differentual Equations", "Numerical Solution of Partial Differentual Equations")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_NCE)

# Organic Chemistry for Engineers
class SessionOCEForm(forms.Form):
    SESSION_OCE = (
        ("Atoms and Molecules", "Atoms and Molecules"),
        ("Orbitals", "Orbitals"),
        ("Isomers, Nomenclature, and Alkanes", "Isomers, Nomenclature, and Alkanes"),
        ("Stereochemistry", "Stereochemistry"),
        ("Alkyl Halides", "Alkyl Halides"),
        ("Alkenes and Alkynes: Part 1", "Alkenes and Alkynes: Part 1"),
        ("Alkenes and Alkynes: Part 2", "Alkenes and Alkynes: Part 2"),
        ("Alcohols, Ethers, and Related Compounds: Part 1", "Alcohols, Ethers, and Related Compounds: Part 1"),
        ("Alcohols, Ethers, and Related Compounds: Part 2", "Alcohols, Ethers, and Related Compounds: Part 2"),
        ("Aromaticity, Benzene, and Substituted Benzenes: Part 1", "Aromaticity, Benzene, and Substituted Benzenes: Part 1"),
        ("Aromaticity, Benzene, and Substituted Benzenes: Part 2", "Aromaticity, Benzene, and Substituted Benzenes: Part 2"),
        ("Aldehydes and Ketones: Part 1", "Aldehydes and Ketones: Part 1"),
        ("Aldehydes and Ketones: Part 2", "Aldehydes and Ketones: Part 2"),
        ("Carboxylic Acids", "Carboxylic Acids"),
        ("Derivatives of Carboxylic Acids", "Derivatives of Carboxylic Acids"),
        ("Amines", "Amines")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_OCE)

# Process Control and Dynamics
class SessionPCDForm(forms.Form):
    SESSION_PCD = (
        ("Theoretical Models of Chemical Processes", "Theoretical Models of Chemical Processes"),
        ("Modelling and Analysis for Process Control", "Modelling and Analysis for Process Control"),
        ("Dynamic Behaviour", "Dynamic Behaviour"),
        ("Feedback Loop", "Feedback Loop"),
        ("PID Algorithm", "PID Algorithm"),
        ("PID Controller Tuning", "PID Controller Tuning"),
        ("Control System Instrumentation", "Control System Instrumentation"),
        ("Stability Analysis and Controller Tuning", "Stability Analysis and Controller Tuning"),
        ("Process Control Design: Definition and Decisions", "Process Control Design: Definition and Decisions"),
        ("Process Control Design: Managing the Design Procedure", "Process Control Design: Managing the Design Procedure")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_PCD)

# Product Design and Development
class SessionPDDForm(forms.Form):
    SESSION_PDD = (
        ("Development Processes and Organizations", "Development Processes and Organizations"),
        ("Identifying Customer Needs", "Identifying Customer Needs"),
        ("Product Specifications", "Product Specifications"),
        ("Concept Generation, Selection, and Testing", "Concept Generation, Selection, and Testing"),
        ("Manufacturing Process", "Manufacturing Process"),
        ("Supply Chain and Distribution", "Supply Chain and Distribution"),
        ("Economic Evaluation", "Economic Evaluation")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_PDD)

# Process Equipment Design
class SessionPEDForm(forms.Form):
    SESSION_PED = (
        ("Fluid Transport Equipment: Piping Systems", "Fluid Transport Equipment: Piping Systems"),
        ("Fluid Transport Equipment: Pumps and Compressors", "Fluid Transport Equipment: Pumps and Compressors"),
        ("Heat Exchangers: Single Phase Process", "Heat Exchangers: Single Phase Process"),
        ("Heat Exchangers: Process Involving Phase Change", "Heat Exchangers: Process Involving Phase Change"),
        ("Separation Towers: Distillation and Gas Absorption", "Separation Towers: Distillation and Gas Absorption"),
        ("Separation Towers: Mechanical Design", "Separation Towers: Mechanical Design"),
        ("Separation Towers: Liquid-Liquid Extraction", "Separation Towers: Liquid-Liquid Extraction"),
        ("Pressure Vessel: Design Considerations", "Pressure Vessel: Design Considerations"),
        ("Pressure Vessels: Design Subject to Combined Loading", "Pressure Vessels: Design Subject to Combined Loading"),
        ("Pressure Vessel: Process Vessels Design", "Pressure Vessel: Process Vessels Design"),
        ("Dryers and Cooling Towers", "Dryers and Cooling Towers"),
        ("Mixing and Agitation", "Mixing and Agitation"),
        ("Transfer of Solids", "Transfer of Solids")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_PED)

# Process Plant Design
class SessionPPDForm(forms.Form):
    SESSION_PPD = (
        ("Process Synthesis", "Process Synthesis"),
        ("Technical Analysis", "Technical Analysis"),
        ("Heat Exchangers Network", "Heat Exchangers Network"),
        ("Utilities and Waste Treatment", "Utilities and Waste Treatment"),
        ("P&ID and Plant Layout", "P&ID and Plant Layout"),
        ("Economic Analysis", "Economic Analysis")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_PPD)

# Transport Phenomena
class SessionTPHForm(forms.Form):
    SESSION_TPH = (
        ("Introduction to Transport Phenomena", "Introduction to Transport Phenomena"),
        ("Shell Momentum Balances and Velocity Distributions in Laminar Flow", "Shell Momentum Balances and Velocity Distributions in Laminar Flow"),
        ("Shell Energy Balances and Temperature Distributions in Solids and Laminar Flow", "Shell Energy Balances and Temperature Distributions in Solids and Laminar Flow"),
        ("Shell Mass Balances and Concentration Distributions in Solids and in Laminar Flow", "Shell Mass Balances and Concentration Distributions in Solids and in Laminar Flow"),
        ("Equation of Change", "Equation of Change"),
        ("Introduction to Turbulent Flow", "Introduction to Turbulent Flow"),
        ("Interphase Transport for Isothermal Systems", "Interphase Transport for Isothermal Systems"),
        ("Interphase Transport in Nonisothermal Systems", "Interphase Transport in Nonisothermal Systems"),
        ("Interphase Transport in Nonisothermal Mixtures", "Interphase Transport in Nonisothermal Mixtures"),
        ("Macroscopic Balances for Isothermal Flow Systems", "Macroscopic Balances for Isothermal Flow Systems"),
        ("Macroscopic Balances for Nonisothermal Systems", "Macroscopic Balances for Nonisothermal Systems"),
        ("Macroscopic Balances for Multicomponent Systems", "Macroscopic Balances for Multicomponent Systems")
    )

    materi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SESSION_TPH)

class JumlahPeserta(forms.Form):
    JUMLAH_PESERTA = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("Lebih dari 10", "Lebih dari 10")
    )

    #jumlah_peserta = forms.ChoiceField(choices=JUMLAH_PESERTA)
    nama_anggota_kelompok_bagi_yang_kelompok = forms.CharField(max_length=1000)
    alamat_email_anggota_kelompok = forms.CharField(max_length=1000)
    sesi_dan_jadwal = forms.CharField(widget=forms.Textarea())
    notes_for_tutor = forms.CharField(max_length=2000, required=False)
    referral_code = forms.CharField(max_length=254, required=False)
    mohon_lampirkan_file_terkait_project_atau_tugas_yang_akan_dibahas = forms.FileField()

class AnggotaKelompokForm(forms.Form):
    nama_anggota_kelompok_bagi_yang_kelompok = forms.CharField(max_length=1000)
    alamat_email_anggota_kelompok = forms.CharField(max_length=1000)