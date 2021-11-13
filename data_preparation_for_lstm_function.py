#libraries
import pickle
import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
#fonction pour préparer les données au traitement par le modèle LSTM
max_length = 10
def preparation(df):
  #convertir le type de la variable LI_DSC_ADS
  df['LI_DSC_ADS'] = df['LI_DSC_ADS'].astype(str)
  #convertir le type de la variable LI_DSC_SIGMA
  df['LI_DSC_SIGMA'] = df['LI_DSC_SIGMA'].astype(str)
  #concaténation des deux variables pour avoir une seule variable
  #(commentaires finaux pour le modèle LSTM)
  df['Comment_lstm'] = df.LI_DSC_SIGMA.str.cat(' '+df.LI_DSC_ADS)
  #appliquer la fonction clean_comment aux commentaires
  df['Comment_lstm'] = df['Comment_lstm'].apply(clean_comment)
  #stemming et vectorisation des commentaires finaux (10 premiers mots)
  for i in range (len(df)):
    df.loc[i, 'Comment_lstm']=stem_comment(df.loc[i, 'Comment_lstm'])
  with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
    X = tokenizer.texts_to_sequences(df["Comment_lstm"].to_numpy())
    X = pad_sequences(X, maxlen=max_length,truncating="post", padding="post")
  return(X)


