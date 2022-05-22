from django.db import models
from sklearn.tree import  DecisionTreeClassifier
from tensorflow import keras
import tensorflow as tf
from ProcessData import *

# Create your models here.


class Data(models.Model):
    comments = models.CharField(max_length=200 , null=True)
    predictions = models.IntegerField(blank=True)
    # comment_length = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        mL_model = tf.keras.models.load_model('mL_model/model.h5', compile=True)
        self.predictions = (mL_model.predict(preprocess_data(self.comments)) > 0.5).astype("int")[0][0]
        return super().save(*args, **kwargs)

    # class Meta:
    #     ordering = ['comment']

    def  __str__(self):
        return self.comments
