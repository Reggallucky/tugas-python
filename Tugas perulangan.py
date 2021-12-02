
nama="Ari";
nim="1234";
nilai_tugas="70";
nilai_uts="65";
nilai_uas="80";
nilai_akhir="71.75";

nama2="Bambang";
nim2="2345";
nilai_tugas2="65";
nilai_uts2="80";
nilai_uas2="90";
nilai_akhir2="79.00";
b = int(input("Masukan Banyaknaya Looping\t=\t"));
a=1;
c=1;
t="t";
y="y";
for a in range (a,b):
    print("=========================================================================");
    print("|\tNO\t|\tNama\t|\tNIM\t|\tTugas\t|\tUts\t|\tUas\t|\tAkhir\t|");
    print("|\t",a," |",nama,"      |",nim," |",nilai_tugas,"       |",nilai_uts," \t|",nilai_uas," \t|\t",nilai_akhir," |");
    print("=========================================================================");
    c=str(input("Lanjutkan atau tidal pilih t atau y\t=\t"));
    if(c==t):
        break;
    else :
        if(c==y):
            c=str(input("Lanjutkan atau tidal pilih t atau y\t=\t"));
        print("=========================================================================");
        print("|\tNO\t|\tNama\t|\tNIM\t|\tTugas\t|\tUts\t|\tUas\t|\tAkhir\t|");
        print("|\t",a," |",nama2,"     |",nim2," |",nilai_tugas2,"       |",nilai_uts2," \t|",nilai_uas2," \t|\t",nilai_akhir2," |");
        print("=========================================================================");
   