# use this to inspect and see the code of 
# the module you are importing

# import inspect library
import inspect
import pandas
  
  
source_DF = inspect.getsource(pandas.DataFrame)
print(source_DF)