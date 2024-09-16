from tkinter import Tk, Label, Button, Canvas,Entry,Frame, Checkbutton, IntVar, Radiobutton,messagebox
from PIL import Image, ImageTk
import psycopg2

baglanti = psycopg2.connect(
    dbname="postgres",
    user="soz",
    password="soz1234",
    host="localhost",
    port="5432"
)

form = Tk()
cursor=baglanti.cursor()
def remove_widgets():
    for widget in form.winfo_children():
        widget.destroy()
def ayni():
    
    global canvas
    form.geometry("800x600")
    form.configure(bg='white') 
    form.resizable(False,False)
    
    canvas = Canvas(form, bg='#444FEA', width=250, height=600, highlightthickness=0)
    canvas.place(x=0, y=0)

def login():
    def on_entry_click(event):
        username_label.place_forget()
    
    def on_focusout(event):
        if username_entry.get() == '':
            username_label.place(x=420, y=240, anchor="center") 
       
    
    def on_password_entry_click(event):
        password_label.place_forget()
    
    def on_password_focusout(event):
        if password_entry.get() == '':
            password_label.place(x=420, y=330, anchor="center") 
    
    def kullanici_dogrula():
        global username
        username = username_entry.get()
        password = password_entry.get()
        
        cursor.execute('SELECT username,password,role FROM kullanicilar WHERE username=%s AND password=%s', (username, password))
        kullanici = cursor.fetchone()
        
        if kullanici:
            role = kullanici[2]
            messagebox.showinfo("Başarılı", "Giriş başarılı!")
            
            if role=="Yönetici":
                yönetci_ekran(username)
            else:
                personel_ekran(username)
        else:
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")
        
    remove_widgets()
    
    form.title("Giriş Ekranı")
    
    ayni()
    welcome_label = Label(canvas, text="WELCOME", font=("Helvetica", 30, "italic bold"),padx=0, pady=0, bg='#444FEA', fg='white',)
    welcome_label.place(relx=0.5, rely=0.46, anchor='center')
    welcome_label2 = Label(canvas, text="BACK!", font=("Helvetica", 30, "italic bold"),padx=0, pady=0, bg='#444FEA', fg='white',)
    welcome_label2.place(x=87, rely=0.54, anchor='center')
    
    login_label = Label(form, text="LOGIN", font=("Helvetica", 24, "italic bold"), bg='white', fg='#676767')
    login_label.place(x=440, rely=0.23, anchor="center")
    
    username_entry = Entry(form, font=("Arial", 12), width=30,bd=0, highlightthickness=0)
    username_entry.place(x=525,y=240, anchor="center")
    username_label = Label(form, text="Username", font=("Helvetica", 12), bg='white')
    username_label.place(x=420,y=240, anchor="center")
    line = Frame(form, bg='#676767', height=0, width=250)
    line.place(x=380,y=256)
    username_entry.bind('<FocusIn>', on_entry_click)
    username_entry.bind('<FocusOut>', on_focusout)
    
    password_entry = Entry(form, font=("Arial", 12), width=30, bd=0, highlightthickness=0, show='*')
    password_entry.place(x=525, y=330, anchor="center")
    password_label = Label(form, text="Password", font=("Helvetica", 12), bg='white')
    password_label.place(x=420, y=330, anchor="center")
    password_line = Frame(form, bg='#676767', height=0, width=250)
    password_line.place(x=380, y=346)
    password_entry.bind('<FocusIn>', on_password_entry_click)
    password_entry.bind('<FocusOut>', on_password_focusout)
    
    x=IntVar()
    remember=Checkbutton(form,text="Remember me?",variable=x,bg="white",fg='#676767',font=("Arial", 7))
    remember.place(x=380,y=370)
    
    login_btn = Button(form, text="LOGIN", font=("Arial", 12), bg='#444FEA', fg='white',width=17,command=kullanici_dogrula)
    login_btn.place(x=520, rely=0.75, anchor="center")
    
    new_user=Label(form,text="New user?",font=("Arial", 7),bg="white",fg='#676767')
    new_user.place(x=380,rely=0.838)
    
    sign_btn1 = Button(form, text="Sign Up", font=("Arial", 7), bg='#444FEA', fg='white', width=9,command=signup)
    sign_btn1.place(x=470, rely=0.85, anchor="center")
    
    
    form.mainloop()
        
def kullanici_kaydet():
    
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_entry.get()
    if password != confirm_password:
        print("Şifreler uyuşmuyor!")
        return
    if x.get()==1 :
        role=("Yönetici")
        
    else:
        role=("Personel")
        
    cursor.execute('INSERT INTO kullanicilar (username, password, role) VALUES (%s, %s, %s)',
                   (username, password, role))
    baglanti.commit()
    messagebox.showinfo("Başarılı", "Kullanıcı Kaydedildi!")    
    
def signup():
    global username_entry, password_entry, confirm_entry, username_label, password_label, confirm_label, x

    remove_widgets()
    form.title("Kayıt Ekranı")
    ayni()
    welcome_label = Label(canvas, text="CREAT", font=("Helvetica", 30, "italic bold"), padx=0, pady=0, bg='#444FEA', fg='white')
    welcome_label.place(x=89, rely=0.46, anchor='center')
    welcome_label2 = Label(canvas, text="ACCOUNT!", font=("Helvetica", 30, "italic bold"), padx=0, pady=0, bg='#444FEA', fg='white')
    welcome_label2.place(relx=0.5, rely=0.54, anchor='center')
    
    login_label = Label(form, text="SIGN UP", font=("Helvetica", 24, "italic bold"), bg='white', fg='#676767')
    login_label.place(x=440, rely=0.15, anchor="center")
    def on_entry_click(event):
        username_label.place_forget()
    
    def on_focusout(event):
        if username_entry.get() == '':
            username_label.place(x=420, y=190, anchor="center") 
    def on_password_entry_click(event):
        password_label.place_forget()
    
    def on_password_focusout(event):
        if password_entry.get() == '':
            password_label.place(x=420, y=270, anchor="center") 
            
    def on_confirm_entry_click(event):
        confirm_label.place_forget()
    
    def on_confirm_focusout(event):
        if confirm_entry.get() == '':
            confirm_label.place(x=420, y=350, anchor="center")
    username_entry = Entry(form, font=("Arial", 12), width=35, bd=0, highlightthickness=0)
    username_entry.place(x=535, y=190, anchor="center")
    username_label = Label(form, text="Username", font=("Helvetica", 12), bg='white')
    username_label.place(x=420, y=190, anchor="center")
    line = Frame(form, bg='#676767', height=0, width=250)
    line.place(x=380, y=206)
    username_entry.bind('<FocusIn>', on_entry_click)
    username_entry.bind('<FocusOut>', on_focusout)
    
    password_entry = Entry(form, font=("Arial", 12), width=35, bd=0, highlightthickness=0, show='*')
    password_entry.place(x=535, y=270, anchor="center")
    password_label = Label(form, text="Password", font=("Helvetica", 12), bg='white')
    password_label.place(x=420, y=270, anchor="center")
    password_line = Frame(form, bg='#676767', height=0, width=250)
    password_line.place(x=380, y=286)
    password_entry.bind('<FocusIn>', on_password_entry_click)
    password_entry.bind('<FocusOut>', on_password_focusout)
    
    confirm_entry = Entry(form, font=("Arial", 12), width=35, bd=0, highlightthickness=0, show='*')
    confirm_entry.place(x=535, y=350, anchor="center")
    confirm_label = Label(form, text="Password", font=("Helvetica", 12), bg='white')
    confirm_label.place(x=420, y=350, anchor="center")
    confirm_line = Frame(form, bg='#676767', height=0, width=250)
    confirm_line.place(x=380, y=366)
    confirm_entry.bind('<FocusIn>', on_confirm_entry_click)
    confirm_entry.bind('<FocusOut>', on_confirm_focusout)
    
    user = Label(form, text="  Already have\nan account?", font=("Arial", 6), bg="white", fg='#676767')
    user.place(x=380, rely=0.838)
    
    x = IntVar()
    x.set(0)
    rd1 = Radiobutton(form, text="Yönetici", font=("Arial", 8), bg="white", value=1, variable=x)
    rd1.place(x=440, rely=0.65)
    
    rd2 = Radiobutton(form, text="Personel", font=("Arial", 8), bg="white", value=2, variable=x)
    rd2.place(x=530, rely=0.65)
            
    login_btn2 = Button(form, text="Login", font=("Arial", 7), bg='#444FEA', fg='white',width=9,command=login)
    login_btn2.place(x=470, rely=0.86, anchor="center")
    
    signup_btn = Button(form, text="SIGN UP", font=("Arial", 12), bg='#444FEA', fg='white', width=17,command=kullanici_kaydet)
    signup_btn.place(x=520, rely=0.75, anchor="center")
    
def ekran():
    global canvas
    form.geometry("800x600")
    form.configure(bg="white")
    form.resizable(False, False)
    
    canvas = Canvas(form, bg='#D7D7D7', width=150, height=600, highlightthickness=0)
    canvas.place(x=0, y=0)
    
    pdks_label=Label(canvas,text="PDKS",font=("Helvetica", 10, "italic bold"),bg='#D7D7D7')
    pdks_label.place(relx=0.36,y=20)
    
    photo1 = Image.open("C:\\Users\\User\\Desktop\\s.png")
    newphoto = photo1.resize((25, 25)) 
    photo1 = ImageTk.PhotoImage(newphoto)
    photo_button =Button(form, image=photo1,borderwidth=0)
    photo_button.place(x=30,y=152)
    form.photo1 = photo1
    
    photo2 = Image.open("C:\\Users\\User\\Desktop\\n.png")
    newphoto2 = photo2.resize((25, 25)) 
    photo2 = ImageTk.PhotoImage(newphoto2)
    photo_button =Button(form, image=photo2,borderwidth=0)
    photo_button.place(x=30,y=92)
    form.photo2 = photo2
    
    photo3 = Image.open("C:\\Users\\User\\Desktop\\e.png")
    newphoto3 = photo3.resize((25, 25)) 
    photo3 = ImageTk.PhotoImage(newphoto3)
    photo_button =Button(form, image=photo3,borderwidth=0)
    photo_button.place(x=30,y=212)
    form.photo3 = photo3  
    
    çıkış_buton=Label(canvas, text="ÇIKIŞ",font=("Helvetica", 10,"italic bold"),bg='#D7D7D7', fg="black",borderwidth=0,padx=8)
    çıkış_buton.place(x=55,y=541)
    
    photo4 = Image.open("C:\\Users\\User\\Desktop\\a.png")
    newphoto4 = photo4.resize((20, 20)) 
    photo4 = ImageTk.PhotoImage(newphoto4)
    photo_button =Button(form, image=photo4,borderwidth=0,command= login)
    photo_button.place(x=35,y=540)
    form.photo4 = photo4
    
    
    
def yönetci_ekran(username):
    remove_widgets()
    
    form.title("Çalışan Liste")
    ekran()
    
    çalışan_button=Button(canvas, text="Çalışan Listesi",font=("Helvetica", 9,"italic"),bg='#444FEA', fg="black", width=20, height=2,borderwidth=0,padx=30)
    çalışan_button.place(y=150)
    
    profil_buton = Button(canvas, text="Profil", font=("Helvetica", 9, "italic"), bg='#D7D7D7', fg="black", width=20, height=2, borderwidth=0,padx=10,command=lambda: yönetici_bilgi(username))
    profil_buton.place(y=90)
    
    baslik_label=Label(form,text="ÇALIŞAN LİSTESİ",font=("Helvetica", 15, "italic bold"),bg="white")
    baslik_label.place(x=200,y=40)
    
    canvas2=Canvas(form,width=200, height=100, bg="#444FEA")
    canvas2.place(x=510,y=38)
    canvas2_label=Label(form,text="ALT BİRİMİNDE ÇALIŞAN İŞÇİ SAYISI",font=("medium",7, "italic bold"),bg="#444FEA",fg="white")
    canvas2_label.place(x=520,y=55)
    
    canvas3=Canvas(form,width=90,height=25,bg="#444FEA")
    canvas3.place(x=620,y=200)
    
    ekle_btn=Label(form,text="Ekle",font=("Helvetica", 11,"italic "),bg="#444FEA", fg="white",height=1)
    ekle_btn.place(x=636,y=203)
    
    istt_buton=Button(canvas,text="İstatistikleri",font=("Helvetica", 9,"italic"),bg='#D7D7D7',fg="black", width=20, height=0, borderwidth=0,padx=17)
    istt_buton.place(y=230)
    ist_buton=Button(canvas,text="Çalışan",font=("Helvetica", 9,"italic"),bg='#D7D7D7',fg="black", width=20,borderwidth=0,height=0,padx=10)
    ist_buton.place(y=210)  
    
    photo5 = Image.open("C:\\Users\\User\\Desktop\\ö.png")
    newphoto5 = photo5.resize((15, 15)) 
    photo5 = ImageTk.PhotoImage(newphoto5)
    photo_button =Button(form,image=photo5,borderwidth=0,command=ekle)
    photo_button.place(x=678,y=207)
    form.photo5 = photo5
    
    bölüm=Canvas(form,width=513,height=30,bg='#D7D7D7')
    bölüm.place(x=200,y=250)
    
    kullanıcı_adı=Label(form,text="Kullanıcı Adı",font=("Helvetica", 9, "italic"),bg='#D7D7D7')
    kullanıcı_adı.place(x=258,y=255)
    
    kullanıcı_adı=Label(form,text="E-Posta",font=("Helvetica", 9, "italic"),bg='#D7D7D7')
    kullanıcı_adı.place(x=428,y=255)
    
    kullanıcı_adı=Label(form,text="İşlemler",font=("Helvetica", 9, "italic"),bg='#D7D7D7')
    kullanıcı_adı.place(x=598,y=255)
    
    canvas4=Canvas(form,width=513,height=270,bg="white")
    canvas4.place(x=200,y=290)
    
    def departmanlari_say(username):
        
        cursor.execute("SELECT COUNT(*) FROM kullanicilar WHERE depart = (SELECT depart FROM kullanicilar WHERE username=%s)", (username,))
        departman_sayilari = cursor.fetchone()[0]
        baglanti.commit()
        return departman_sayilari
    
    departman_sayilari = departmanlari_say(username)
    alt_personel=departman_sayilari-1
    if alt_personel:
        sayı = Label(form, text=alt_personel, font=("Helvetica", 35, "italic bold"), fg="white", bg="#444FEA")
        sayı.place(x=512, y=78)   
    
    def kullanici_depart_getir(username):
        cursor.execute("SELECT depart FROM kullanicilar WHERE username=%s", (username,))
        depart = cursor.fetchone()
        baglanti.commit()
        if depart:
            return depart[0]
      
    depart=kullanici_depart_getir(username)
    dep_label=Label(form,text=depart,font=("Helvetica", 9, "italic bold"),bg="white")
    dep_label.place(x=200,y=100)
    
    for i in range(7):
        detay=Button(form,text="Detay",font=("Helvetica", 9,"italic "),bg="#444FEA", fg="white",height=1)
        detay.place(x=596,y=295+i*35)
        canvas4.create_line(0,35+i*35,515,35+i*35,fill="#D7D7D7",width=1)
    
    def kullaıcı_bilgilerini_getir(depart):
        
        cursor.execute("SELECT username,eposta FROM kullanicilar WHERE depart=%s",(depart,))
        kullanıcı_bilgileri = cursor.fetchall()
        baglanti.commit()
        
        return kullanıcı_bilgileri
    
    kullanıcı_bilgileri=kullaıcı_bilgilerini_getir(depart)
    if kullanıcı_bilgileri:
        
        for i, (ad, eposta) in enumerate(kullanıcı_bilgileri):
            if ad!=username:
                ad_label = Label(form, text=ad, font=("Helvetica", 9, "italic"), bg="white")
                ad_label.place(x=258, y=295+i*35)
                
                eposta_label = Label(form, text=eposta, font=("Helvetica", 9, "italic"), bg="white")
                eposta_label.place(x=428, y=295+i*35)
                
                detay_button = Button(form, text="Detay", font=("Helvetica", 9, "italic"), bg="#444FEA", fg="white", height=1,command=lambda ad=ad: personel_ekran1(ad))
                detay_button.place(x=596, y=295+i*35)
                
    def sil_günc(i):
        for btn in sil_buttons:
            btn.place_forget()
        
        for btn in guncelle_buttons:
            btn.place_forget()
            
        sil_buttons[i].place(x=664, y=280+i*35)
        guncelle_buttons[i].place(x=664, y=310+i*35)    

        
    sil_buttons = []
    guncelle_buttons= []
    photo_references = []
    for i in range(7):
        photo6 = Image.open("C:\\Users\\User\\Desktop\\z.png")
        newphoto6 = photo6.resize((15, 15)) 
        photo6 = ImageTk.PhotoImage(newphoto6)
        photo_references.append(photo6)
        photo_button =Button(form,image=photo6,borderwidth=0,command=lambda i=i:sil_günc(i))
        photo_button.place(x=645,y=299+i*35)
        form.photo = photo6  
        sil_button = Button(form, text="SİL", font=("Helvetica", 9, "italic"), bg="red", fg="white", height=1, width=4,command=lambda i=i:onayla_ve_sil(i))
        sil_buttons.append(sil_button)
        guncelle_button = Button(form, text="GÜNCELLE", font=("Helvetica", 9, "italic"), bg="blue", fg="white", height=1, width=8)
        guncelle_buttons.append(guncelle_button) 
    form.photo_references = photo_references             
    
    def kullanıcıyı_sil(username):
    
        cursor.execute("DELETE FROM kullanicilar WHERE username=%s", (username,))
        baglanti.commit()
        
    def onayla_ve_sil(i):
        username = kullanıcı_bilgileri[i][0]
        cevap = messagebox.askyesno("Onay", f"{username} adlı kullanıcıyı silmek istediğinize emin misiniz?")
        if cevap:
            kullanıcıyı_sil(username)
            messagebox.showinfo("Başarılı", "Kullanıcı silindi!")  
    
def ekle():
    global entries
    form=Tk()
    
    form.title("Çalışan Ekle")
    form.geometry("600x400")
    form.configure(bg="#D7D7D7")
    form.resizable(False, False)
    entries = []
    
    bilgiler_kişisel=["AD:","SOYAD:","DOĞUM TARİHİ:","CİNSİYET:","MEDENİ HAL:","USERNAME","PASSWORD"]
    y_baslangic=60
    
    for kiş in bilgiler_kişisel:
        label=Label(form,text=kiş,bg="#D7D7D7",fg="black",font=("Helvetica", 8, "italic bold"))
        label.place(x=40,y=y_baslangic)
        entry = Entry(form, font=("Helvetica", 8, "italic bold"), width=20,bd=0, highlightthickness=0)
        entry.place(x=150,y=y_baslangic)
        entries.append(entry) 
        y_baslangic+=40
        
    bilgiler_iş=["ROL:","DEPARTMAN:","POZİSYON:","İŞE BAŞLAMA TARİHİ:","AYLIK MAAŞI:","NUMARA:","E_POSTA:","ADRES:"]
    y_baslangic=60
    for iş in bilgiler_iş:
        label=Label(form,text=iş,bg="#D7D7D7",fg="black",font=("Helvetica", 8, "italic bold"))
        label.place(x=330,y=y_baslangic)
        entry = Entry(form, font=("Helvetica", 8, "italic bold"), width=20,bd=0, highlightthickness=0)
        entry.place(x=455,y=y_baslangic)
        entries.append(entry) 
        y_baslangic+=40
    kaydet_button = Button(form, text="Kaydet", command=kaydet)
    kaydet_button.place(x=270, y=350)

def kaydet():
    
    for entry in entries:
        degerler = [entry.get()]
    cursor.execute('''
           INSERT INTO kullanicilar (ad, soyad, doğumtarihi, cinsiyet, medenihal, username, password,role,
           depart, pozisyon, işebaşlama,maaş, numara, eposta, adres)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
    ''', degerler)
    baglanti.commit()
    
    messagebox.showinfo("Başarılı", "Kullanıcı başarıyla eklendi!")
  
    
def yönetici_bilgi(username):
    global canvas
    
    remove_widgets()
    form.title("Yönetici Profil")
    ekran()
    
    çalışan_button = Button(canvas, text="Profil", font=("Helvetica", 9, "italic"), bg='#444FEA', fg="black", width=20, height=2, borderwidth=0,padx=10)
    çalışan_button.place(y=90)
    
    profil_buton=Button(canvas, text="Çalışan Listesi",font=("Helvetica", 9,"italic"),bg='#D7D7D7', fg="black", width=20, height=2,borderwidth=0,padx=30,command=lambda: yönetci_ekran(username))
    profil_buton.place(y=150)
    
    baslik_label=Label(form,text="PROFİL",font=("Helvetica", 15, "italic bold"),bg="white")
    baslik_label.place(x=200,y=40)
    
    
    istt_buton=Button(canvas,text="İstatistikleri",font=("Helvetica", 9,"italic"),bg='#D7D7D7',fg="black", width=20, height=0, borderwidth=0,padx=17)
    istt_buton.place(y=230)
    ist_buton=Button(canvas,text="Çalışan",font=("Helvetica", 9,"italic"),bg='#D7D7D7',fg="black", width=20,borderwidth=0,height=0,padx=10)
    ist_buton.place(y=210)  
    
    canvas=Canvas(form,bg="#D7D7D7",width=230,height=450,highlightthickness=0)
    canvas.place(x=200,y=100)
    
    canvas=Canvas(form,bg="#D7D7D7",width=230,height=250,highlightthickness=0)
    canvas.place(x=500,y=100)
    
    canvas=Canvas(form,bg="#D7D7D7",width=230,height=150,highlightthickness=0)
    canvas.place(x=500,y=400)
    
    canvas=Canvas(form,bg="white",width=100,height=130,highlightthickness=0)
    canvas.place(x=230,y=120)
    
    bilgileri_yaz(username)

def bilgileri_yaz(username):
    veriler = """
    SELECT ad,soyad,doğumtarihi,cinsiyet,medenihal,depart,pozisyon,işebaşlama,maaş,numara,eposta,adres
    FROM kullanicilar
    WHERE username = %s;
    """
    cursor.execute(veriler, (username,))
    kullanıcı_verileri = cursor.fetchone()
    
    
    
    kisisel_bilgiler=["AD:","SOYAD:","DOĞUM TARİHİ:","CİNSİYET:","MEDENİ HAL:"]
    
    y_baslangic=285
    for i,kis in enumerate(kisisel_bilgiler):
        label=Label(form, text=kis,bg="#D7D7D7",fg="black",font=("Helvetica", 8, "italic bold"))
        label.place(x=230,y=y_baslangic)
        value_label=Label(form, text=kullanıcı_verileri[i],bg="#D7D7D7",fg="black",font=("Helvetica", 8, "italic"))
        value_label.place(x=330,y=y_baslangic)
        y_baslangic+=50
        
    iş_bilgileri=["DEPARTMAN:","POZİSYON:","İŞE BAŞLAMA TARİHİ:","AYLIK MAAŞI:"]
    
    y_baslangic2=140
    for j,iş in enumerate(iş_bilgileri):
        label2=Label(form, text=iş,bg="#D7D7D7",fg="black",font=("Helvetica", 8, "italic bold"))
        label2.place(x=520,y=y_baslangic2)
        value_label2=Label(form,text=kullanıcı_verileri[j+5],bg="#D7D7D7",fg="black",font=("Helvetica", 8, "italic"))
        value_label2.place(x=650,y=y_baslangic2)
        y_baslangic2+=50
        
        
        
    iletişim_bilgileri=["NUMARA:","E_POSTA:","ADRES:"]
    
    y_baslangic3=410
    for k,il in enumerate(iletişim_bilgileri):
        label3=Label(form, text=il,bg="#D7D7D7",fg="black",font=("Helvetica", 8, "italic bold"))
        label3.place(x=520,y=y_baslangic3)
        value_label3=Label(form,text=kullanıcı_verileri[k+9],bg="#D7D7D7",fg="black",font=("Helvetica", 8, "italic"))
        value_label3.place(x=610,y=y_baslangic3)
        y_baslangic3+=50
        
def personel_ekran(username):
    
    remove_widgets()
    form.title("Personel Profil")
    form.geometry("800x600")
    form.configure(bg="white")
    form.resizable(False, False)
    
    canvas = Canvas(form, bg='#D7D7D7', width=150, height=600, highlightthickness=0)
    canvas.place(x=0, y=0)
    
    pdks_label=Label(canvas,text="PDKS",font=("Helvetica", 10, "italic bold"),bg='#D7D7D7')
    pdks_label.place(relx=0.36,y=20)
    
    çalışan_button = Button(canvas, text="Profil", font=("Helvetica", 9, "italic"), bg='#444FEA', fg="black", width=20, height=2, borderwidth=0,padx=10)
    çalışan_button.place(y=90)
     
    çıkış_buton=Label(canvas, text="ÇIKIŞ",font=("Helvetica", 10,"italic bold"),bg='#D7D7D7', fg="black",borderwidth=0,padx=8)
    çıkış_buton.place(x=55,y=541)
    
    baslik_label=Label(form,text="PROFİL",font=("Helvetica", 15, "italic bold"),bg="white")
    baslik_label.place(x=200,y=40)
    
    canvas=Canvas(form,bg="#D7D7D7",width=230,height=450,highlightthickness=0)
    canvas.place(x=200,y=100)
    
    canvas=Canvas(form,bg="#D7D7D7",width=230,height=250,highlightthickness=0)
    canvas.place(x=500,y=100)
    
    canvas=Canvas(form,bg="#D7D7D7",width=230,height=150,highlightthickness=0)
    canvas.place(x=500,y=400)
    
    canvas=Canvas(form,bg="white",width=100,height=130,highlightthickness=0)
    canvas.place(x=230,y=120)
    
    photo4 = Image.open("C:\\Users\\User\\Desktop\\a.png")
    newphoto4 = photo4.resize((20, 20)) 
    photo4 = ImageTk.PhotoImage(newphoto4)
    photo_button =Button(form, image=photo4,borderwidth=0,command= lambda:yönetci_ekran(username))
    photo_button.place(x=35,y=540)
    form.photo4 = photo4 
     
    photo1 = Image.open("C:\\Users\\User\\Desktop\\n.png")
    newphoto1 = photo1.resize((25, 25)) 
    photo1 = ImageTk.PhotoImage(newphoto1)
    photo_button1 =Button(form, image=photo1,borderwidth=0)
    photo_button1.place(x=30,y=92)    
    form.photo = photo1
    
    bilgileri_yaz(username)
    
def personel_ekran1(ad):
    global username
    remove_widgets()
    form.title("Personel Profil")
    form.geometry("800x600")
    form.configure(bg="white")
    form.resizable(False, False)
    
    canvas = Canvas(form, bg='#D7D7D7', width=150, height=600, highlightthickness=0)
    canvas.place(x=0, y=0)
    
    pdks_label=Label(canvas,text="PDKS",font=("Helvetica", 10, "italic bold"),bg='#D7D7D7')
    pdks_label.place(relx=0.36,y=20)
    
    çalışan_button = Button(canvas, text="Profil", font=("Helvetica", 9, "italic"), bg='#444FEA', fg="black", width=20, height=2, borderwidth=0,padx=10)
    çalışan_button.place(y=90)
     
    çıkış_buton=Label(canvas, text="ÇIKIŞ",font=("Helvetica", 10,"italic bold"),bg='#D7D7D7', fg="black",borderwidth=0,padx=8)
    çıkış_buton.place(x=55,y=541)
    
    baslik_label=Label(form,text="PROFİL",font=("Helvetica", 15, "italic bold"),bg="white")
    baslik_label.place(x=200,y=40)
    
    canvas=Canvas(form,bg="#D7D7D7",width=230,height=450,highlightthickness=0)
    canvas.place(x=200,y=100)
    
    canvas=Canvas(form,bg="#D7D7D7",width=230,height=250,highlightthickness=0)
    canvas.place(x=500,y=100)
    
    canvas=Canvas(form,bg="#D7D7D7",width=230,height=150,highlightthickness=0)
    canvas.place(x=500,y=400)
    
    canvas=Canvas(form,bg="white",width=100,height=130,highlightthickness=0)
    canvas.place(x=230,y=120)
    
    photo4 = Image.open("C:\\Users\\User\\Desktop\\a.png")
    newphoto4 = photo4.resize((20, 20)) 
    photo4 = ImageTk.PhotoImage(newphoto4)
    photo_button =Button(form, image=photo4,borderwidth=0,command= lambda:yönetci_ekran(username))
    photo_button.place(x=35,y=540)
    form.photo4 = photo4 
     
    photo1 = Image.open("C:\\Users\\User\\Desktop\\n.png")
    newphoto1 = photo1.resize((25, 25)) 
    photo1 = ImageTk.PhotoImage(newphoto1)
    photo_button1 =Button(form, image=photo1,borderwidth=0)
    photo_button1.place(x=30,y=92)    
    form.photo = photo1
    
    bilgileri_yaz(ad)


login()
