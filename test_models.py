    class PtsPhy(models.Model):
    name= models.CharField(max_length=30)
    TYPE_LIAISON = [
        ('MB', 'modbus'),
        ('FL', 'filaire'),
        ('BN', 'bacnet')
    ]
    type_liaison = models.CharField(max_length=2, choices=TYPE_LIAISON)
    blocAF = models.ManyToManyField(BlocAF, on_delete=models.CASCADE)




class TechnicalObject(models.Model):
    name= models.CharField(max_length=30)
    description= models.CharField(max_length=30)
    blocs = models.ForeignKey(BlocsAF, on_delete=models.CASCADE)
    release_date = models.DateField()

class BlocsAF(models.Model):
    name= models.CharField(max_length=30)
    description= models.CharField(max_length=30)

class PtsPhy(models.Model):
    name= models.CharField(max_length=30)
    type= models.ForeignKey('TypePoints')

class TypePoints(models.Model):
    content = models.TextField()
