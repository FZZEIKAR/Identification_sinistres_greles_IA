#libraries
import tensorflow
import os
import numpy as np
import keras
#fonction de prédiction avec le modèle lstm
def predict_lstm(df):
  #charger le modèle LSTM déjà entrainé et sauvegardé
  my_model= tensorflow.keras.models.load_model('My_model.h5')
  #préparer les données en appliquant la fonction preparation
  x = preparation(df)
  #prédire la classe de chaque sinistre en utilisant le modèle LSTM
  predictions=my_model.predict(x)
  pred = np.array(list(map(lambda x : 'grele' if x > 0.5 else 'non grele',predictions)))
  pred.tolist()
  df['lstm_class'] = pred
  return(df)
