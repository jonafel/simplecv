import streamlit as st
import pandas as pd

st.set_page_config(page_title="Jonathan Felix P. K. Aji CV")
image_path = 'assets/Images/mamas.jpg'
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image(image_path, width=200)

st.markdown("""
<style>
.title {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>Jonathan Felix P. K. Aji CV</h1>", unsafe_allow_html=True)


st.header('Personal Details')
st.write('''
Jonathan Felix Prabowo Kusuma Aji ||
Laki-laki ||
Kristen Protestan ||
24 April 1993 ||
0812-9664-2060 ||
jonathanfelixaji@gmail.com ||
Tambun Selatan, Kabupaten Bekasi, Indonesia

''')
st.subheader('Summary')
st.write('''
Detail-oriented dan jujur dengan pengalaman lebih dari 8 tahun di berbagai bidang pekerjaan serta mampu bekerja (individual maupun tim) untuk melaksanakan pekerjaan baik di dalam dan diluar area kerja.
Menganalisa serta menjadi manajemen yang baik untuk produktivitas tim dan organisasi. Bertanggung jawab dan tekun dalam mengerjakan segala sesuatu serta dapat membangun tim dari berbagai latar belakang untuk memiliki visi yang sama.
''')

st.header("Work & Organization Experience Details")
st.subheader('Freelance Admin, Deliveree Indonesia | May 2024-Present')
st.write('''
* Menghubungi serta mengarahkan leads Driver untuk mendaftarkan diri mereka ke Deliveree
* Menghubungi serta mengurus dan memeriksa data driver yang mendaftar hingga dapat diterima sebagai Mitra Driver Deliveree
''')

st.subheader('Customer Sales, Dalmet Sofa | April 2023- May 2024')
st.write('''
* Mempersiapkan tools untuk penjualan sofa serta menjual sofa tersebut langsung kepada pelanggan
* Menangani langsung pesanan khusus sesuai keinginan pelanggan
* Mengambil foto atau video untuk kebutuhan penjualan sofa via E-commerce
''')

st.subheader('Anggota dan Ketua Komisi Inforkom, GPIB Anugerah Bekasi K-102 | May 2017 - Present')
st.write('''
* Mengatur penugasan tim dan persiapan peralatan yang dibutuhkan untuk setiap jam ibadah dan event gerejawi.
* Penanggung jawab Audio Visual setiap ibadah serta event gerejawi serta Live Streaming via Youtube gereja.
* Ketua Tim Program Kerja dan Anggaran 2024-2025.
* Menopang kekurangan tim dan memastikan setiap event dan ibadah gereja tetap berjalan  lancar dengan peralatan dan tim yang ada.
* Menjadi penghubung antara komisi lain dengan Inforkom untuk kolaborasi dan mensupport seluruh kegiatan gereja hingga berjalan dengan efektif.
''')

st.header("Education Details")
df_pendidikan = pd.DataFrame({
    "Tahun": ['2012-2015', '2017-2023'],
    "Institusi": ["Institut Pertanian Bogor", "Universitas Paramadina"],
    "Gelar": ["Ahli Madya Ilmu Komunikasi", "Sarjana Ilmu Komunikasi"],
    "Jurusan": ["Ilmu Komunikasi", "Komunikasi Strategis"],
    "Final GPA": ["2.86", "3.26"]
})
st.table(df_pendidikan)

st.header("Certifications Details")
st.write('''
1. Certified in Google Digital Enterpreneurship by DEA (Digital Enterpreneurship Academy)
2. Certified in Search Engine Optimization by Tokopedia
3. Certified in TOEFL (score 556) by L.A. Language Academy
''')

st.header("Key Skills")
col_1, col_2 = st.columns([1,2])

with col_1:
    st.write('''
    * Microsoft Office
    * Google Workspace
    * Data Entry
    * Jujur
    * Komunikasi
    * Manajemen
    ''')

with col_2:
    st.write('''
    * Pemecahan Masalah
    * Customer Services
    * Detail saat dibutuhkan
    * Corversational English
    * Mudah Berbaur
    * Bertanggung Jawab
    ''')

