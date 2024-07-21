import pandas as pd

################### Prepare Function ######################
# check missing values 
# module Check missing value 
def missing_value(df):
    '''
    Documentation :
    --------------
    * df : Dataframe Name
    '''
    #count the number of missing value 
    total = df.isnull().sum().sort_values(ascending = False)
    percent = round(df.isnull().sum()/len(df)*100,2).sort_values(ascending = False)
    missing  = pd.concat([total, percent], axis=1, keys=['Total_Missing', 'Percent(%)'])
    
    return missing.head(20)


#check list data types 
def list_dtypes(df):
    categorical_list = []
    numerical_list = []
    for col in df.columns.tolist():
        if df[col].dtype=='object':
            categorical_list.append(col)
        else:
            numerical_list.append(col)
    print('Number of categorical features:', str(len(categorical_list)))
    print('Number of numerical features:', str(len(numerical_list)))

    return categorical_list, numerical_list

## filling missing values 
def fill_missing(df, feature_list = None , vartype = None ):
    '''
    Documentation :
    ---------------
    df              : object, dataframe
    feature_list    : feature list is the set of numerical or categorical features 
                      that have been seperated before
    vartype         : variable type : continuos or categorical, default (numerical)
                        (0) numerical   : variable type continuos/numerical
                        (1) categorical : variable type categorical
    Note :
    ------
    > if numerical variable will be filled by median 
    > if categorical variabe will filled by modus
    > if have been made variebles based on the dtypes list before, 
      insert it into feature list in the function.     

    Example :
    ---------
    # 1. Define feature that will be filled in 
      num_feature = numeric_list
      
    # 2. Input Dataframe
      dataframe = df
      
    # 3. Vartype
      var_type = 0
      
    # 4. Filling Value
      Fill_missing(dataframe, num_feature, var_type)
    '''
    #default vartype 
    if vartype == None :
        vartype = 'numerical'

    # filling numerical data with median 
    if vartype == 'numerical' :
        for col in feature_list:
            df[col] = df[col].fillna(df[col].median())
    
    # filling categorical data with modus  
    if vartype == 'categorical' :
        for col in feature_list:
            df[col] = df[col].fillna(df[col].mode().iloc[0])