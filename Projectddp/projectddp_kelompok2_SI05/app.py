import streamlit as st
import math
import requests



page_bg_img = """
<style>
    .stApp{
        background-image: url('https://plus.unsplash.com/premium_photo-1724800663787-094f67f76f82?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
    }

    [data-testid="stSidebar"]{
    background-size:cover;
    background-color:#979c97;
    }

        [data-testid="stHeader"]{
        background-color: rgba(0, 0, 0, 0);
        }

        [data-testid="stTollbar"]{
        rigth: 2rem;
        }

        .title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            margin-top: -50px; 
        }

        .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.2s;
        cursor: pointer;
        border-radius: 5px;
        }
        .stButton button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
        }

        body {
            color: green;
            font-size: 18px;
        }
</style>
<h1 class="title">🧮KALKULATOR BANGUN RUANG</h1>
"""



st.markdown(page_bg_img, unsafe_allow_html=True)


# Fungsi untuk menghitung volume dan luas permukaan kubus
def hitung_volume_kubus(sisi):
    return sisi ** 3

def hitung_luas_permukaan_kubus(sisi):
    return 6 * (sisi ** 2)

# Fungsi untuk menghitung volume dan luas permukaan balok
def hitung_volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def hitung_luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Fungsi untuk menghitung volume dan luas permukaan tabung
def hitung_volume_tabung(jari_jari, tinggi):
    return math.pi * (jari_jari ** 2) * tinggi

def hitung_luas_permukaan_tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

# Fungsi untuk menghitung volume dan luas permukaan kerucut
def hitung_volume_kerucut(jari_jari, tinggi):
    return (1/3) * math.pi * (jari_jari ** 2) * tinggi

def hitung_luas_permukaan_kerucut(jari_jari, tinggi):
    sisi_miring = math.sqrt(jari_jari**2 + tinggi**2)
    return math.pi * jari_jari * (jari_jari + sisi_miring)

# Fungsi untuk menghitung volume dan luas permukaan prisma segitiga
def hitung_volume_prisma_segitiga(panjang, lebar, tinggi):
    return 0.5 * panjang * lebar * tinggi

def hitung_luas_permukaan_prisma_segitiga(panjang, lebar, tinggi):
    alas = panjang
    tinggi_segitiga = lebar
    tinggi_prisma = tinggi
    sisi_miring = math.sqrt((alas / 2) ** 2 + tinggi_segitiga ** 2)
    return 2 * (0.5 * alas * tinggi_segitiga) + (alas * tinggi_prisma) + (2 * sisi_miring * tinggi_prisma)

# Fungsi untuk menghitung volume dan luas permukaan prisma segiempat
def hitung_volume_prisma_segiempat(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def hitung_luas_permukaan_prisma_segiempat(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Fungsi untuk menghitung volume dan luas permukaan limas segitiga
def hitung_volume_limas_segitiga(panjang_alas, tinggi_alas, tinggi_limas):
    return (1/3) * (0.5 * panjang_alas * tinggi_alas) * tinggi_limas

def hitung_luas_permukaan_limas_segitiga(panjang_alas, tinggi_alas, tinggi_limas):
    luas_alas = 0.5 * panjang_alas * tinggi_alas
    sisi_miring = math.sqrt((panjang_alas / 2) ** 2 + tinggi_alas ** 2)
    luas_sisi_samping = 3 * (0.5 * panjang_alas * sisi_miring)
    return luas_alas + luas_sisi_samping

# Fungsi untuk menghitung volume dan luas permukaan limas segiempat
def hitung_volume_limas_segiempat(panjang, lebar, tinggi):
    return (1/3) * panjang * lebar * tinggi

def hitung_luas_permukaan_limas_segiempat(panjang, lebar, tinggi):
    luas_alas = panjang * lebar
    tinggi_sisi = math.sqrt((panjang / 2) ** 2 + tinggi ** 2)
    luas_sisi_1 = panjang * tinggi_sisi
    luas_sisi_2 = lebar * tinggi_sisi
    return luas_alas + 2 * luas_sisi_1 + 2 * luas_sisi_2

# sidebar
def main():
    st.sidebar.title("NAVIGASI")
    pilihmenu = st.sidebar.selectbox("PILIH MENU UTAMA:", ["PROFIL TEAM", "LATAR BELAKANG", "PERHITUNGAN"],)

    if pilihmenu == "LATAR BELAKANG":
        st.title("LATAR BELAKANG")
        st.write("Menghitung volume dan luas permukaan bangun ruang merupakan mata pelajaran penting dalam matematika, khususnya geometri. Namun, banyak pelajar dan pengguna merasa kesulitan untuk menghitungnya secara manual, terutama untuk bentuk geometri yang rumit. Selain itu, proses perhitungan  manual dapat memakan waktu dan rawan kesalahan.Untuk mengatasi permasalahan tersebut, diperlukan suatu aplikasi yang dapat mempermudah dan mempercepat perhitungan volume ruangan dan luas permukaan. ")
        st.write("Aplikasi ini bertujuan untuk membantu pengguna  menghitung  lebih akurat dan praktis tanpa harus menghafal banyak rumus. Aplikasi ini memungkinkan Anda memperoleh hasil perhitungan yang cepat dan akurat hanya dengan memasukkan  data dasar bentuk geometris yang akan dihitung.")
    
    elif pilihmenu == "PROFIL TEAM":
        st.title("Profil")
        st.subheader("Kelompok 2")
        col1, col2,col3 = st.columns(3)  # Membuat tiga kolom
        col2.image("foto/Mahendra.jpg", width=250, caption="Mahendra")
        col1, col2,col3 = st.columns(3)  # Membuat tiga kolom
        col1.image("foto/dila.jpg", width=150, caption="Fadhilah Maharani")
        col2.image("foto/harum.jpg", width=200, caption="Harum Hoirunisa")
        col3.image("foto/lia.jpg", width=150, caption="Rizki Tri Amelia")

    else:
        # menu bangun ruang
        
        Menu = st.sidebar.selectbox("PILIH BANGUN RUANG: ", ["Kubus" , "Balok", "Tabung", "Kerucut","Prisma", "Limas"]) 
        st.subheader(f"Kamu Memilih {Menu} Untuk Dihitung")
        st.markdown(
        """Selamat datang di Kalkulator Bangun Ruang. Masukkan nilai-nilai untuk mendapatkan hasil perhitungan.""")

        #pilih rumus
        Rumus = st.selectbox("Pilih Rumus Yang Ingin Dihitung: " ,("Volume", "Luas Permukaan"))
        
        if Menu == "Kubus":
            st.image("foto/kubus.jpg", width=400)
            sisi = st.number_input("Masukkan panjang sisi kubus:", min_value=0.0, step=0.1)
            if st.button("Hitung"):
                if sisi > 0:
                    if Rumus == "Volume":
                        st.success(f"Volume Kubus: {hitung_volume_kubus(sisi):.2f} cm³")
                    else:
                        st.success(f"Luas Permukaan Kubus: {hitung_luas_permukaan_kubus(sisi):.2f} cm²")
                else:
                    st.warning("Masukkan nilai sisi lebih besar dari 0.")
            
        elif Menu == "Balok":
            st.image("foto/balok.jpg", width=250)
            panjang = st.number_input("Masukkan panjang balok:", min_value=0.0, step=0.1)
            lebar = st.number_input("Masukkan lebar balok:", min_value=0.0, step=0.1)
            tinggi = st.number_input("Masukkan tinggi balok:", min_value=0.0, step=0.1)
            if st.button("Hitung"):
                if panjang > 0 and lebar > 0 and tinggi > 0:
                    if Rumus == "Volume":
                        st.success(f"Volume Balok: {hitung_volume_balok(panjang, lebar, tinggi):.2f} cm³")
                    else:
                        st.success(f"Luas Permukaan Balok: {hitung_luas_permukaan_balok(panjang, lebar, tinggi):.2f} cm²")
                else:
                    st.warning("Masukkan semua nilai dimensi lebih besar dari 0.")

        elif Menu == "Tabung":
            st.image("foto/tabung.jpg", width=150)
            jari_jari = st.number_input("Masukkan jari-jari tabung:", min_value=0.0, step=0.1)
            tinggi = st.number_input("Masukkan tinggi tabung:", min_value=0.0, step=0.1)
            if st.button("Hitung"):
                if jari_jari > 0 and tinggi > 0:
                    if Rumus == "Volume":
                        st.success(f"Volume Tabung: {hitung_volume_tabung(jari_jari, tinggi):.2f} cm³")
                    else:
                        st.success(f"Luas Permukaan Tabung: {hitung_luas_permukaan_tabung(jari_jari, tinggi):.2f} cm²")
                else:
                    st.warning("Masukkan nilai jari-jari dan tinggi lebih besar dari 0.")

        elif Menu == "Kerucut":
            st.image("foto/kerucut.png", width=200)
            jari_jari = st.number_input("Masukkan jari-jari kerucut:", min_value=0.0, step=0.1)
            tinggi = st.number_input("Masukkan tinggi kerucut:", min_value=0.0, step=0.1)
            if st.button("Hitung"):
                if jari_jari > 0 and tinggi > 0:
                    if Rumus == "Volume":
                        st.success(f"Volume Kerucut: {hitung_volume_kerucut(jari_jari, tinggi):.2f} cm³")
                    else:
                        st.success(f"Luas Permukaan Kerucut: {hitung_luas_permukaan_kerucut(jari_jari, tinggi):.2f} cm²")
                else:
                    st.warning("Masukkan nilai jari-jari dan tinggi lebih besar dari 0.")


        elif Menu == "Prisma":  # Prisma
            
            pilihan_prisma = st.selectbox("Pilih Prisma : ", ("Prisma Segitiga", "Prisma Segiempat"))
            if pilihan_prisma == "Prisma Segitiga":  # Prisma Segitiga  
                st.image("foto/prisma segitiga.jpg", width= 300)
                panjang = st.number_input("Masukkan panjang alas segitiga: ", min_value=0.0, step=0.1)
                lebar = st.number_input("Masukkan tinggi segitiga: ", min_value=0.0, step=0.1)
                tinggi = st.number_input("Masukkan tinggi prisma: ", min_value=0.0, step=0.1)
                if st.button("Hitung"):
                    if panjang > 0 and lebar > 0 and tinggi > 0:
                        if Rumus == "Volume":
                            st.success(f"Volume Prisma Segitiga: {hitung_volume_prisma_segitiga(panjang, lebar, tinggi)} cm³")
                        else:
                            st.success(f"Luas Permukaan Prisma Segitiga: {hitung_luas_permukaan_prisma_segitiga(panjang, lebar, tinggi)} cm²")
                    else:
                        st.warning("Masukkan nilai lebih besar dari 0.")



            elif pilihan_prisma == "Prisma Segiempat":  # Prisma Segiempat
                st.image("foto/prisma segiempat.png", width= 200)
                panjang = st.number_input("Masukkan panjang segiempat: ", min_value=0.0, step=0.1)
                lebar = st.number_input("Masukkan lebar segiempat: ", min_value=0.0, step=0.1)
                tinggi = st.number_input("Masukkan tinggi prisma: ", min_value=0.0, step=0.1)
                if st.button("Hitung"):
                    if panjang > 0 and lebar > 0 and tinggi > 0:
                        if Rumus == "Volume":
                            st.success(f"Volume Prisma Segiempat: {hitung_volume_prisma_segiempat(panjang, lebar, tinggi)} cm³ ")
                        else:
                            st.success(f"Luas Permukaan Prisma Segiempat: {hitung_luas_permukaan_prisma_segiempat(panjang, lebar, tinggi)} cm²")
                    else:
                        st.warning("Masukkan nilai lebih besar dari 0..")

        elif Menu == "Limas":  # Limas
            pilihan_limas = st.selectbox("Pilih Limas : ", ("Limas Segitiga", "Limas Segiempat"))

            if pilihan_limas == "Limas Segitiga":  # Limas Segitiga
                st.image("foto/limas segitiga.jpg", width= 200)
                panjang_alas = st.number_input("Masukkan panjang alas segitiga: ", min_value=0.0, step=0.1)
                tinggi_alas = st.number_input("Masukkan tinggi alas segitiga: ", min_value=0.0, step=0.1)
                tinggi_limas = st.number_input("Masukkan tinggi limas: ", min_value=0.0, step=0.1)
                if st.button("Hitung"):
                    if panjang_alas > 0 and tinggi_alas > 0 and tinggi_limas > 0:
                        if Rumus == "Volume":
                            st.success(f"Volume Limas Segitiga: {hitung_volume_limas_segitiga(panjang_alas, tinggi_alas, tinggi_limas)} cm³")
                        else:
                            st.success(f"Luas Permukaan Limas Segitiga: {hitung_luas_permukaan_limas_segitiga(panjang_alas, tinggi_alas, tinggi_limas)} cm²")
                    else:
                        st.warning("Masukkan nilai lebih besar dari 0.")
            

            elif pilihan_limas == "Limas Segiempat":  # Limas Segiempat
                st.image("foto/limas segiempat.png", width= 200)
                panjang = st.number_input("Masukkan panjang alas segiempat: ", min_value=0.0, step=0.1)
                lebar = st.number_input("Masukkan lebar alas segiempat: ", min_value=0.0, step=0.1)
                tinggi = st.number_input("Masukkan tinggi limas: ", min_value=0.0, step=0.1)
                if st.button("Hitung"):
                    if panjang_alas > 0 and tinggi_alas > 0 and tinggi_limas > 0:
                        if Rumus == "Volume":
                            st.success(f"Volume Limas Segiempat: {hitung_volume_limas_segiempat(panjang, lebar, tinggi)} cm³")
                        else:
                            st.write(f"Luas Permukaan Limas Segiempat: {hitung_luas_permukaan_limas_segiempat(panjang, lebar, tinggi)} cm²")
                else:
                    st.warning("Masukkan nilai lebih besar dari 0.")
  
# Memanggil fungsi utama
main()  