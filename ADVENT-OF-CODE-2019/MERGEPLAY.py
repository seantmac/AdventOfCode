#Play with ideas to do FAST 3-Way Merge via Pandas   #2020-05-11

import pandas as pd
import dask.dataframe as dd
import time

#PYTHON DOESN'T SUPPORT GOTO.  what?!?


#def f ( x ):
#    """ function that computes and returns x * x """
#    return x * x
#
#    print ( " Main program starts here " )
#    print ( " 4 * 4 = % s " % f (4))
#    print ( " In last line of program -- bye " )





start = time.time()

# SPOT YOU THE MASTER LIST OF DIMENSIONS  --  THESE SHOULD BE PASSED INTO THE CALL
# col:  R  C  MACH  TRIMSET  PATN
# row:  R     MACH  TRIMSET  W
# qry:        MACH  TRIMSET  PATN  W
#      {R  C  MACH  TRIMSET  PATN  W}   # AND THE FIELDNAME IN Q THAT IS THE COEF:  'PctYield'

# Create a dataframe FOR THE COLUMN ELEMENT
#col_data = pd.read_csv('C:/OPTMODELS/D-OPT/BLOCK1c.CSV')
#col_data = pd.read_csv('C:/OPTMODELS/D-OPT/I75CSVHUGE/V_06_TRIMPROD.CSV')
col_data = pd.read_csv('C:/OPTMODELS/D-OPT/I75CSVHUGE/Col06_TRIMPROD.CSV')
colcol_list = ['TRIMPRODID', 'TRIMPRODKey', 'TRIMPRODCode', 'R','C','MACH','TRIMSET','PATN']
#colcol_list = [                                              'R','C','MACH','TRIMSET','PATN']   #Note:  for vfile with no id, key or code
col_data = col_data[colcol_list]

# Create a second dataframe FOR THE ROW ELEMENT
#row_data = pd.read_csv('C:/OPTMODELS/D-OPT/BLOCK1r.CSV')
#row_data = pd.read_csv('C:/OPTMODELS/D-OPT/I75CSVHUGE/R_02_ROLLBAL.CSV')
row_data = pd.read_csv('C:/OPTMODELS/D-OPT/I75CSVHUGE/Row02_ROLLBAL.CSV')
rowcol_list = ['ROLLBALID', 'ROLLBALKey', 'ROLLBALCode', 'R','MACH','TRIMSET','W']
#rowcol_list = [                                           'R','MACH','TRIMSET','W']  #Note:  no id, key or code
row_data = row_data[rowcol_list]

# Create a third dataframe FOR THE QRY WITH THE COEFFICIENT VALUES IN IT ("COEF QUERY")
#qry_data = pd.read_csv('C:/OPTMODELS/D-OPT/BLOCK1q.CSV')
qry_data = pd.read_csv('C:/OPTMODELS/D-OPT/I75CSVHUGE/qlkPatternYield.CSV')
qrycol_list = ['MACH','TRIMSET','PATN', 'W', 'PctYield']
qry_data = qry_data[qrycol_list]

# MERGE THEM ALL UP
dfcolrow = dd.merge(col_data, row_data, how='inner', on=['R','MACH','TRIMSET'])
coef_block = dd.merge(qry_data, dfcolrow, how='inner', on=['MACH','TRIMSET','PATN', 'W'])

# REORDER COLUMNS AND RENAME SO #ColID	RowID	COL	ROW	COEF
coef_block = coef_block[['TRIMPRODID', 'ROLLBALID', 'TRIMPRODCode', 'ROLLBALCode', 'PctYield']]  #*&* this errors because no ID ID CODE CODE
coef_block.columns = ['ColID', 'RowID', 'COL', 'ROW', 'COEF']

# Write the output.
coef_block.to_csv('C:/OPTMODELS/D-OPT/BLOCK1RESULT.CSV', index=False)

end = time.time()
elapsed = end - start
print("Simple Merge put in to test small trimprod matrix block.  Elapsed Time =  ", round(elapsed,4), " SECONDS")
#c-opt took 90 seconds or so to do MatGen: 11 TRIMPROD ROLLBAL  (SQLExpress)
#the biggest I75HUGE block took  #Simple Merge put in to test small trimprod matrix block.  Elapsed Time =   473.8598  SECONDS