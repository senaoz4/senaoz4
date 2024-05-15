import turtle
import time
import datetime

turtle.setup(600,600)
turtle.title("Analog Saat")

turtle.speed(0)
turtle.penup()
turtle.goto(0,-300)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("pink")
turtle.circle(300)
turtle.tracer(0)
turtle.end_fill()
saniye=turtle.Turtle()
dakika=turtle.Turtle()
saat=turtle.Turtle()

def analog_saat_ayarla(s,d,sn):
    turtle.speed(0)
    turtle.pencolor("black")
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(90)
    for i in range(12):
        turtle.right(30)
        turtle.forward(270)
        turtle.pendown()
        turtle.forward(30)
        turtle.penup()
        turtle.write(f"{i+1}",font=("italic", 15))
        turtle.goto(0,0)
        
    turtle.hideturtle()
        
    saniye.speed(0)
    saniye.pencolor("red")
    saniye.penup()
    saniye.goto(0,0)
    saniye.setheading(90)
    saniye.right(saniye_bilgisi/60*360)
    saniye.pendown()
    saniye.shape("turtle")
    saniye.fillcolor("red")
    saniye.pensize(3)
    saniye.forward(250)
    
    dakika.speed(0)
    dakika.pencolor("blue")
    dakika.penup()
    dakika.goto(0,0)
    dakika.setheading(90)
    dakika.right(dakika_bilgisi/60*360)
    dakika.pendown()
    dakika.shape("turtle")
    dakika.fillcolor("blue")
    dakika.pensize(3)
    dakika.forward(200)
    
    saat.speed(0)
    saat.pencolor("green")
    saat.penup()
    saat.goto(0,0)
    saat.setheading(90)
    saat.right(saat_bilgisi/12*360)
    saat.pendown()
    saat.shape("turtle")
    saat.fillcolor("green")
    saat.pensize(3)
    saat.forward(150)

def main():
    an=datetime.datetime.now()
    gün=an.day
    ay=an.month
    yıl=an.year
    tarih(gün,ay,yıl)
    
çiz=turtle.Turtle()
def tarih(gün,ay,yıl):
    çiz.speed(0)
    çiz.pencolor("white")
    çiz.pensize(3)
    çiz.begin_fill()
    çiz.fillcolor("black")
    çiz.end_fill()
    çiz.penup()
    çiz.goto(300,-200)
    çiz.pendown()
    for i in range(3):
        çiz.begin_fill()
        çiz.fillcolor("black")
        for j in range(4):
            çiz.forward(100)
            çiz.right(90)
        çiz.penup()
        çiz.goto(300+100*(i+1),-200)
        çiz.pendown()
        çiz.end_fill()
        
        
    çiz.penup()
    çiz.goto(300,-230)
    çiz.pendown()
    çiz.forward(300)
    
       
    çiz.penup()
    çiz.goto(340,-225)
    çiz.pendown()
    çiz.write("Gün",font=("italic", 15))
    
    çiz.penup()
    çiz.goto(440,-225)
    çiz.pendown()
    çiz.write("Ay",font=("italic", 15))
    
    çiz.penup()
    çiz.goto(540,-225)
    çiz.pendown()
    çiz.write("Yıl",font=("italic", 15))
    
    çiz.penup()
    çiz.goto(340,-270)
    çiz.pendown()
    çiz.write(gün,font=("italic", 20))
    
    çiz.penup()
    çiz.goto(442,-270)
    çiz.pendown()
    çiz.write(ay,font=("italic", 20))
    
    çiz.penup()
    çiz.goto(527,-270)
    çiz.pendown()
    çiz.write(yıl,font=("italic", 20))
    
    çiz.hideturtle()
main()


while True:
    saniye_bilgisi=int(time.strftime('%S'))
    dakika_bilgisi=int(time.strftime("%M"))
    saat_bilgisi=int(time.strftime("%I"))
    analog_saat_ayarla(saniye_bilgisi,dakika_bilgisi,saat_bilgisi)
    turtle.update()
    saniye.clear()
    dakika.clear()
    saat.clear()
    
    
    

    
"""
Saatin Kullanım Klavuzu:
    Pürüzsüz hareketi,estetik görüntüsü ve diğer saatlerden fark yaratmak amacı ile 
    tasarlanmış "turtle" ibre şekli ile dikkat çeken saatimizin çalışam prensibi şu şekildedir:
        Kodumuzuz çalıştırıldığı andaki saat,dakika,saniye bilgilerini alarak ayarlandıktan sonra
        döngüsünü başlatır. Analog saatimizin yanında bulunan gösterge o ana ait gün,ay,yıla ait
        bilgileri bize sunar.
"""
