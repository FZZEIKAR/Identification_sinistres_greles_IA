#fonction Recherche V
def Recherche_V(df):
  #convertir le type de la variable LI_DSC_ADS
    df['LI_DSC_ADS']=df['LI_DSC_ADS'].astype(str)
    #convertir le type de la variable LI_DSC_SIGMA
    df['LI_DSC_SIGMA']=df['LI_DSC_SIGMA'].astype(str)
    #convertir le type de la variable LI_CAUSE
    df['LI_CAUSE']=df['LI_CAUSE'].astype(str)
    #concaténation des trois variables pour avoir une seule variable
    #(commentaires finaux pour la fonction Recherche_V)
    df['Comment_RV']=df.LI_DSC_SIGMA.str.cat(' '+df.LI_DSC_ADS+' '+df.LI_CAUSE)
    #appliquer la fonction clean_comment aux commentaires finaux
    df['Comment_RV']=df['Comment_RV'].apply(clean_comment)
    #stemming et recherche du stem 'grel' dans les commentaires finaux
    for i in range (len(df)):
      df.loc[i,'Comment_RV']=stem_comment(df.loc[i,'Comment_RV'])
      if (df.loc[i,'Comment_RV'].find('grel') != -1):
        df.loc[i,'Recherche_V_class']='grele'
      else:
        df.loc[i,'Recherche_V_class']='non grele'
    return(df)
