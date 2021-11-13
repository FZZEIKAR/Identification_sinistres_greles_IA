#fonction permettant de construire la table finale à télécharger après l'intervention de l'utilisateur
#fonction qui classifie les sinistres en deux classes
def table_finale(df,df_verifier,df_grele):
  a=df_verifier.empty
  b=df_grele.empty
  if ((a==False) and (b==False)):
    df_non_grele = df_verifier.merge(df_grele['ID_ADS'], how = 'left' ,indicator=True).loc[lambda x : x['_merge']=='left_only'].drop('_merge', 1).reset_index(drop=True)
    df_non_grele.loc[:,'Class']='non grele'
    for i in range (0,len(df_verifier)):
      for j in range (0,len(df_grele)):
        if df_verifier.loc[i,'ID_ADS']==df_grele.loc[j, 'ID_ADS']:
          df_verifier.loc[i, 'Class']=df_grele.loc[j, 'Class']
      for j in range (0,len(df_non_grele)):
        if df_verifier.loc[i,'ID_ADS']==df_non_grele.loc[j, 'ID_ADS']:
          df_verifier.loc[i, 'Class']=df_non_grele.loc[j, 'Class']
    for k in range (0, len(df)):
      for j in range (0, len(df_verifier)):
        if df.loc[k,'ID_ADS']==df_verifier.loc[j, 'ID_ADS']:
          df.loc[k, 'Class']=df_verifier.loc[j, 'Class']
  elif ((a==False) and (b==True)):
    for k in range (0, len(df)):
      for j in range (0, len(df_verifier)):
        if df.loc[k,'ID_ADS']==df_verifier.loc[j, 'ID_ADS']:
          df.loc[k, 'Class']='non grele'
  return(df)
