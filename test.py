from Archive.SqlOp import SqlOp

DB = SqlOp()
# sql = '''insert into Good(GoodCode,BrandCode,ClassCode,GoodName,ScaleCode,GoodType,GoodJLDW,GoodSCJG,GoodXSJ,GoodCBJ,GoodNum)
# #  values (1,1,1,'1',1,'1','1',0.1,0.1,0.1,10)'''
#
#
# sql = 'select GoodNum from Good where GoodCode = 1'
# print(DB.runSql(sql)[0][0])
# # print(DB.select('Good'))
a = DB.select('Order')
print(a)
print(type(a))
