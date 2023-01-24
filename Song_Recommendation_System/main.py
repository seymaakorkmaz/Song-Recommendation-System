from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import numpy as np

import Recommender

window = Tk()
window.title("EXPERT SYSTEMS TERM PROJECT")
window.geometry('1500x730+200+100')
window.configure(bg='#313131')
window.resizable(height=False, width=False)
window.iconbitmap('spotify.ico')
window.attributes('-alpha')


# window üzerine yerleştirilen frame'ler
frame1 = Frame(window, height=70, width=400, bg='#FFFFFF')
frame1.place(x=30, y=110)
frame2 = Frame(window, height=70, width=10, bg='#313131')
frame2.place(x=400, y=110)
frame3 = Frame(window, height=70, width=10, bg='#313131', pady=20)
frame3.place(x=1250, y=90)

Label(window, text="SONG RECOMMENDER SYSTEM", font=('Comic Sans MS', 24, 'bold'), justify='center', bg='#313131',
      fg='#2ECF36', padx=30, pady=30).pack()
song = Entry(frame1, font=('Comic Sans MS', 20), bg='#FFFFFF', fg='#313131',width = 30)
song.pack()

beyda = Label(window, text="      BEYDA GÜLER - 19011010 ", font=('Comic Sans MS', 12, 'bold'), justify='center',
              bg='#313131',
              fg='#81D686', cursor='heart')
beyda.place(x=35, y=670)

seyma = Label(window, text=" ŞEYMANUR KORKMAZ - 20011055 ", font=('Comic Sans MS', 12, 'bold'), justify='center',
              bg='#313131',
              fg='#81D686', cursor='heart')
seyma.place(x=35, y=695)

name = Label(frame2, text="  NAME ", font=('Comic Sans MS', 18, 'bold'), justify='center',
             bg='#313131',
             fg='#000000')
name.grid(row=0, column=0)

artist = Label(frame2, text="  ARTIST  ", font=('Comic Sans MS', 18, 'bold'), justify='center',
               bg='#313131',
               fg='#000000')
artist.grid(row=0, column=1)

similarity = Label(frame2, text="  SIMILARITY  ", font=('Comic Sans MS', 18, 'bold'), justify='center',
                   bg='#313131',
                   fg='#000000')
similarity.grid(row=0, column=2)

# Aşağıdaki satırlarda önerilen şarkılarının isimlerinin yazılacağı labellar oluşturulmuştur.
lbl_sng1 = Label(frame2, text="              ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_sng1.grid(row=1, column=0)

lbl_sng2 = Label(frame2, text="             ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_sng2.grid(row=2, column=0)

lbl_sng3 = Label(frame2, text="             ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_sng3.grid(row=3, column=0)

lbl_sng4 = Label(frame2, text="             ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_sng4.grid(row=4, column=0)

lbl_sng5 = Label(frame2, text="             ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_sng5.grid(row=5, column=0)

lbl_sng6 = Label(frame2, text="              ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_sng6.grid(row=6, column=0)

lbl_sng7 = Label(frame2, text="              ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_sng7.grid(row=7, column=0)




# Aşağıdaki satırlarda önerilen şarkıları söyleyen kişilerin isimlerinin yazılacağı labellar oluşturulmuştur.
lbl_artist1 = Label(frame2, text="             ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                    bg='#313131',
                    fg='#FFFFFF', padx=20, pady=20)
lbl_artist1.grid(row=1, column=1)

lbl_artist2 = Label(frame2, text="             ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                    bg='#313131',
                    fg='#FFFFFF', padx=20, pady=20)
lbl_artist2.grid(row=2, column=1)

lbl_artist3 = Label(frame2, text="             ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                    bg='#313131',
                    fg='#FFFFFF', padx=20, pady=20)
lbl_artist3.grid(row=3, column=1)

lbl_artist4 = Label(frame2, text="             ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                    bg='#313131',
                    fg='#FFFFFF', padx=20, pady=20)
lbl_artist4.grid(row=4, column=1)

lbl_artist5 = Label(frame2, text="             ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                    bg='#313131',
                    fg='#FFFFFF', padx=20, pady=20)
lbl_artist5.grid(row=5, column=1)


lbl_artist6 = Label(frame2, text="             ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                    bg='#313131',
                    fg='#FFFFFF', padx=20, pady=20)
lbl_artist6.grid(row=6, column=1)

lbl_artist7 = Label(frame2, text="             ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                    bg='#313131',
                    fg='#FFFFFF', padx=20, pady=20)
lbl_artist7.grid(row=7, column=1)


rate = Label(window, text="  RATE ", font=('Comic Sans MS', 18, 'bold'), justify='center',
             bg='#313131',
             fg='#000000')


#Aşağıdaki satırlarda önerilen şarkıların cosine similarity bilgilerini içeren labellar oluşturulmuştur.
lbl_cos1 = Label(frame2, text="     ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_cos1.grid(row=1, column=2)

lbl_cos2 = Label(frame2, text="     ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_cos2.grid(row=2, column=2)

lbl_cos3 = Label(frame2, text="     ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_cos3.grid(row=3, column=2)

lbl_cos4 = Label(frame2, text="     ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_cos4.grid(row=4, column=2)


lbl_cos5 = Label(frame2, text="     ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_cos5.grid(row=5, column=2)

lbl_cos6 = Label(frame2, text="     ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_cos6.grid(row=6, column=2)

lbl_cos7 = Label(frame2, text="     ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                 bg='#313131',
                 fg='#FFFFFF', padx=20, pady=20)
lbl_cos7.grid(row=7, column=2)


#Oluşturulan labellar dizilere atılmıştır.
sng = [lbl_sng1, lbl_sng2, lbl_sng3, lbl_sng4, lbl_sng5, lbl_sng6, lbl_sng7]

artist = [lbl_artist1, lbl_artist2, lbl_artist3, lbl_artist4, lbl_artist5, lbl_artist6, lbl_artist7]

cosine = [lbl_cos1, lbl_cos2, lbl_cos3, lbl_cos4, lbl_cos5, lbl_cos6, lbl_cos7]


#Kullanıcının girdiği şarkının name, album, artist bilgilerinin ekrana yazılmasını sağlayan labellar oluşturulmuştur.
songNameLabel = Label(window, text='SONG NAME :', font=('Comic Sans MS', 13, 'bold'), justify='center',
              bg='#313131',
              fg='#2ECF36')
songName = Label(window, text=' ', font=('Comic Sans MS', 13, 'bold'), justify='center',
              bg='#313131',
              fg='#81D686')

albumNameLabel = Label(window, text='ALBUM NAME :', font=('Comic Sans MS', 13, 'bold'), justify='center',
              bg='#313131',
              fg='#2ECF36')
albumName = Label(window, text=' ', font=('Comic Sans MS', 13, 'bold'), justify='center',
              bg='#313131',
              fg='#81D686')

artistNameLabel = Label(window, text='ARTIST NAME :', font=('Comic Sans MS', 13, 'bold'), justify='center',
              bg='#313131',
              fg='#2ECF36')
artistName = Label(window, text=' ', font=('Comic Sans MS', 13, 'bold'), justify='center',
              bg='#313131',
              fg='#81D686')


# btn1 şarkı ismi girildikten sonra sistemin 7 adet şarkı önermesini sağlayan butondur.
btn1 = Button(window, text="RECOMMEND", font=('Comic Sans MS', 15, 'bold'), bg='#000000', fg='#2ECF36',
              command=lambda: recommend(),width=14)
btn1.place(x=30, y=175)

# btn2 önerilerin ve verilen puanların ekrandan temizlenmesini ve sistemin yeni bir öneriye hazır hale gelmesini sağlar.
btn2 = Button(window, text="     CLEAR    ", font=('Comic Sans MS', 15, 'bold'), bg='#000000', fg='#2ECF36',
              command=lambda: clear(), width=14)
btn2.place(x=221, y=175)

score = Label(window, text='Rate This Song!', font=('Comic Sans MS', 13, 'bold'), justify='center',
              cursor='star',
              bg='#313131',
              fg='#2ECF36')

slider1 = Scale(window, from_=0, to=5, cursor='star', orient='horizontal', bg='#313131', fg='#FFFFFF',
                resolution=0.01, borderwidth=0.5, highlightthickness=0)  #Kullanıcının girdiği şarkıyı puanlamasını sağlar.

slider = []  #Kullanıcın önerilen şarkıları puanlar.
for i in range(0, 7):
    temp = Scale(window, from_=0, to=5, cursor='star', orient='horizontal', bg='#313131', fg='#FFFFFF',
                 resolution=0.01, borderwidth=0.5, highlightthickness=0)
    slider.append(temp)

finish = Button(window, text="OK", font=('Comic Sans MS', 15, 'bold'), bg='#000000', fg='#2ECF36', width=3, height=-1,
                command=lambda: finishRating1()) #Kullanıcının girdiği şarkıya verdiği puanı kaydetmesini sağlar.

scores = []
finish2 = Button(window, text="OK", font=('Comic Sans MS', 15, 'bold'), bg='#000000', fg='#2ECF36', width=3, height=0,
                 command=lambda: scores == finishRatings()) #Kullanıcının önerilen şarkılara verdiği puanları kaydetmesini sağlar.


#calculate butonuna basıldığında yapılan tahminin hata oranı ekrana yazdırılır.
calculate = Button(window, text="CALCULATE ERROR RATE", font=('Comic Sans MS', 13, 'bold'), bg='#000000', fg='#2ECF36',
                   width=25, height=0,
                   command=lambda: Calculate())

# Mean Square Error'un sonucunun yazıldığı label
scoreLabel = Label(window, text="       ", font=('Comic Sans MS', 15, 'bold'), justify='center',
                   bg='#313131',
                   fg='#FFFFFF',
                   padx=20, pady=20)


# Recommend butonuna basıldığında çağırılan ve tahmin yapılmasını sağlayan fonksiyon
def recommend():
    text = song.get()  # Kullanıcının girdiği şarkı
    text = text.encode('utf-8').decode('utf-8').upper() # Türkçe harf duyarlılığı sağlanarak girilen textin tamamı büyük harfe çevrilmiştir
    song.delete(0, END)  #Şarkı girme çubuğunun içi temizlenir

    # Veri seti girilen şarkıyı içeriyor mu diye kontrol edilir.
    if Recommender.isThereinDataSet(text) == 1:
        # Recommender classından generate_Recommendation fonksiyonu çağrılarak dönüş değerleri dizilere atılır
        top7songs, artists, similarity_score = Recommender.generate_recommendation(text)
        # top7songs benzerliği en yüksek 7 şarkıyı, artists şarkıların sanatçılarını, similarity score ise şarkıların benzerliklerini tutar.
        top7songs = top7songs.array
        artists = artists.array

        # Fonksiyondan dönen değerler ekrana yazdırılır.
        for i in range(0, 7):
            sng[i]["text"] = top7songs[i]
            artist[i]["text"] = artists[i]
            cosine[i]["text"] = "%" + str(round(100 * similarity_score[i][1], 5))

        # Girilen şarkının diğer bilgileri Recommender classındaki SongInfo fonksiyonu çağrılarak alınmış ve ekrana yazdırılmıştır.
        songName['text'], artistName['text'],  albumName['text'] = Recommender.SongInfo(text)

        # Recommend butonuna basıldıktan sonra ekrana gelmesi gereken widgetlar burada place edilmiştir.
        score.place(x=35, y=390)
        slider1.place(x=230, y=380, relwidth=0.1, relheight=0.1)
        finish.place(x=185, y=435)
        songNameLabel.place(x=35,y=230)
        songName.place(x=210, y=230)
        albumNameLabel.place(x=35,y=280)
        albumName.place(x=210, y=280)
        artistNameLabel.place(x=35,y=330)
        artistName.place(x=210, y=330)
        rate.place(x=1250, y=106)
        finish2.place(x=1310, y=660)

       # similarities = []
        for i in range(0, 7):
            slider[i].place(x=1250, y=160 + (i * 73),relwidth=0.1, relheight=0.1)
            #similarities.append(similarity_score[i][1])
        return

    else:   # Girilen Şarkı dataset'te bulunmuyorsa uyarı verilir.
        messagebox.showwarning("WARNING", "This song doesn't exist in my dataset. Please try again.")
        # Girilen şarkı veri setinde bulunmuyorsa warning verilir

def clear():   # Bu fonksiyon CLEAR butonuna basıldığında çağrılan fonksiyondur. Bir önceki önerinin ekrandan silinmesini sağlar.

    finish['state'] = 'normal'  # finish butonu enable edilir.
    finish2['state'] = 'normal'   # finish2 butonu enable edilir.
    slider1.set(0)
    slider1['state'] = 'normal'   # slider1 enable edilir ve işaret ettiği değer initial durumu olan 0'a çekilir.

    # Öneriler ve öneriden sonra ekranda oluşan widgetlar place_forget()  fonksiyonu ile kaldırılmıştır.
    finish.place_forget()
    finish2.place_forget()
    albumNameLabel.place_forget()
    albumName.place_forget()
    songName.place_forget()
    songNameLabel.place_forget()
    artistName.place_forget()
    artistNameLabel.place_forget()
    calculate.place_forget()
    scoreLabel.place_forget()
    slider1.place_forget()
    score.place_forget()
    rate.place_forget()
    for i in range(0, 7):
        sng[i]["text"] = "                "
        artist[i]["text"] = "               "
        cosine[i]["text"] = "  "
        slider[i]['state'] = 'normal'
        slider[i].set(0)
        slider[i].place_forget()
    return


def finishRating1():  # Kullanıcı girdiği şarkıyı puanlayıp finish1 butonuna bastıktan sonra çağrılan fonksiyon.
    msg = messagebox.askyesno("Warning", "You cannot change your score after saving. Do you want to continue?")
    if msg:
        slider1['state'] = 'disabled'  # Puanlama yapıldıktan sonra puanın değiştirilmesi engellenir.
        finish['state'] = 'disabled'
    return


def finishRatings(): # Kullanıcı tahmin edilen şarkıları puanlayıp finish2 butonuna bastıktan sonra çağrılan fonksiyon
    msg = messagebox.askyesno("Warning", "You cannot change your score after saving. Do you want to continue?")
    if msg:
        calculate.place(x=85, y=515)
        for i in range(0, 7):
            scores.append(slider[i].get())
            slider[i]['state'] = 'disabled'  # Puanlama yapıldıktan sonra puanların değiştirilmesi engellenir.

        finish2['state'] = 'disabled'
    return scores


# Mean Square Error'un hesaplandığı fonksiyon
def Calculate():
    similarities = []
    for i in range(0, 7):
        similarities.append(cosine[i]['text'])  # Önerilen şarkıların cosine similarity değerleri similarities isimli dizide toplanır.

    # Recommender classındaki scoreCalculator fonksiyonu çağrılarak dönüş değeri scoreLabel'a yazılmıştır.
    scoreLabel['text'] = round(Recommender.scoreCalculator(similarities, scores, slider1.get()), 5)
    scoreLabel.place(x=150, y=560)

window.mainloop()
