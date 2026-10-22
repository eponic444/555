from django.db import models

# Create your models here.



class category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    nomi = models.CharField(max_length=120)
    img = models.ImageField(upload_to='media/')




class Jobs(models.Model):
    name = models.CharField(max_length=120)
    price = models.CharField(max_length=120)

class Person(models.Model):
    name = models.CharField(max_length=120)
    age = models.CharField(max_length=120)
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE)



class computers(models.Model):
    name = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    cpu = models.CharField(max_length=120)
    gpu = models.CharField(max_length=120)
    ssd = models.IntegerField()
    price = models.IntegerField()
 
class custumer(models.Model):
    name = models.CharField(max_length=120)

    computer = models.ForeignKey(computers,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class joymee(models.Model):
    name = models.CharField(max_length=120)
    opisaniy = models.CharField(max_length=1200)
    tipkvr = models.CharField(max_length=120)
    hona = models.IntegerField()
    etaj = models.IntegerField()
    ploshad = models.IntegerField()
    remony = models.CharField()
    locatsiya =  models.CharField(max_length=1200)
    price = models.IntegerField()
    nomer = models.IntegerField()
    image = models.ImageField(upload_to='media/')

class client(models.Model):
    name = models.CharField(max_length=120)
    joymee = models.ForeignKey(joymee,on_delete=models.CASCADE)


class avtor(models.Model):
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    folowers = models.IntegerField()
    vidios = models.IntegerField()
    descrution = models.CharField(max_length=1200)
    link = models.CharField(max_length=130)
    Registrationdate = models.DateField()
    Country = models.CharField(max_length=120)
    views = models.IntegerField()

class vidio (models.Model):
    name =models.CharField(max_length=120)
    descrution = models.CharField(max_length=120)
    vidio = models.CharField(max_length=120)
    time = models.IntegerField()
    like = models.IntegerField()
    dislike = models.IntegerField()
    date = models.DateField()
    views = models.IntegerField()
    link = models.CharField(max_length=120)
    coments = models.IntegerField()
    prevyu = models.ImageField(upload_to='media/')
    avtor = models.ForeignKey(avtor,on_delete=models.CASCADE)

class musiq(models.Model):
    avtor = models.CharField(max_length=120)
    history = models.CharField(max_length=5000)
    live = models.IntegerField()
    yers = models.IntegerField()
    slushateli = models.IntegerField()
    popularmusic = models.CharField(max_length=120)
    newmusic = models.CharField(max_length=120)


class lisen(models.Model):
    avtor = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    musiq = models.ForeignKey(musiq,on_delete=models.CASCADE)

class film(models.Model):
    name = models.CharField(max_length=120)
    avtor = models.CharField(max_length=120)
    operator = models.CharField(max_length=120)
    voulme = models.CharField(max_length=120)
    roli = models.CharField(max_length=1200)
    views = models.IntegerField()
    like = models.IntegerField()
    dislike = models.IntegerField()
    date  = models.DateField()
    coments = models.IntegerField()
    

class  spectator (models.Model):
    name = models.CharField(max_length=120)
    views = models.IntegerField()
    like = models.IntegerField()
    dislike = models.IntegerField()
    film = models.ForeignKey(film,on_delete=models.CASCADE)

class car (models.Model):
    name = models.CharField(max_length=120)
    komplekt = models.CharField(max_length=120)
    kuzov = models.CharField(max_length=120)
    vupusk = models.DateField()
    probeg = models.IntegerField()
    karobka = models.CharField(max_length=120)
    rang = models.CharField(max_length=120)
    dvigatl = models.CharField(max_length=120)
    toplivo = models.CharField(max_length=120)
    kuch = models.IntegerField()
    narh = models.IntegerField()


class costumer (models.Model):
    name = models.CharField(max_length=120)
    car = models.ForeignKey(car,on_delete=models.CASCADE)


class bank (models.Model):
    kurs = models.IntegerField()
    mikrozaym = models.CharField(max_length=120)
    avtokredit = models.IntegerField()
    avtosugurta = models.IntegerField() 
    ipoteka = models.IntegerField()
    cardvisa = models.CharField(max_length=120)
    perevod = models.CharField()
    goldprice = models.IntegerField() 


class bankclient (models.Model):

    name = models.CharField(max_length=120)
    surename = models.CharField(max_length=120)
    bank = models.ForeignKey(bank,on_delete=models.CASCADE)


class uzum (models.Model):
    name = models.CharField(max_length=120)
    size = models.CharField(max_length=120)
    color = models.CharField(max_length=120)
    rewievs = models.CharField(max_length=120)
    orders = models.IntegerField()
    bought = models.IntegerField()
    canbeordert = models.IntegerField()
    dilevery = models.DateField()
    garant = models.IntegerField()
    marcet = models.CharField(max_length=120)
    description = models.CharField(max_length=1200)

class clientuzum (models.Model):
    name = models.CharField(max_length=120)
    surename = models.CharField(max_length=120)
    uzum = models.ForeignKey(uzum,on_delete=models.CASCADE)
    


class work (models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    staj = models.IntegerField()
    oldwork = models.CharField(max_length=120)

class worker (models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()

    work = models.ForeignKey(work,on_delete=models.CASCADE)

    







