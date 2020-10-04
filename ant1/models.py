from django.db import models

class Personne(models.Model):
    prenom= models.CharField(max_length=30)
    nom= models.CharField(max_length=30)
    email = models.EmailField(blank=False, default='DEFAULT VALUE')
    motdepasse= models.CharField(max_length=30)

    def __str__(self):
        return self.prenom + " " + self.nom

class ObjetTechnique(models.Model):
    name= models.CharField(max_length=30)
    description= models.CharField(max_length=30)
    release_date = models.DateField()

    def __str__(self):
        return self.name

class PtPhy(models.Model):
    name= models.CharField(max_length=30)
    TYPE_LIAISON = [
        ('MB', 'modbus'),
        ('FL', 'filaire'),
        ('BN', 'bacnet')
    ]
    type_liaison = models.CharField(max_length=2, choices=TYPE_LIAISON)

    def __str__(self):
        return self.name

#    bloc = models.ForeignKey(BlocsAF, on_delete=models.CASCADE)
