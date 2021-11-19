#Libraries
import openpyxl
import pandas as pd
#fonction de la solution hybride qui classifie les sinistres en trois classes
def classifier(file):
  df=pd.read_excel(file ,engine='openpyxl')
  df_Recherche_V = Recherche_V(df)
  df_lstm = predict_lstm(df)
  for i in range (len(df)):
    if df_Recherche_V.loc[i, 'Recherche_V_class']=='non grele':
      df.loc[i, 'Class']='non grele'
    elif df_Recherche_V.loc[i, 'Recherche_V_class']=='grele' and df_lstm.loc[i, 'lstm_class']=='grele':
      df.loc[i, 'Class']='grele'
    elif df_Recherche_V.loc[i, 'Recherche_V_class']=='grele' and df_lstm.loc[i, 'lstm_class']=='non grele':
      df.loc[i, 'Class']='sinistre à vérifier'
  return(df.loc[:, (df.columns != 'Recherche_V_class')&(df.columns != 'lstm_class')&(df.columns != 'Comment_RV')&(df.columns != 'Comment_lstm')])

