

dbutils.fs.mkdirs("/Volumes/workspace/default/project_vol/bronze")
dbutils.fs.mkdirs("/Volumes/workspace/default/project_vol/silver")
dbutils.fs.mkdirs("/Volumes/workspace/default/project_vol/gold")
     

display(dbutils.fs.ls("/Volumes/workspace/default/project_vol"))
     
