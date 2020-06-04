from flask import Flask, render_template, request
from datetime import timedelta

from Archive.SqlOp import SqlOp

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/checkMode')
def checkMode():
    return render_template('checkMode.html')

@app.route('/managerMode')
def managerMode():
    return render_template('managerMode.html')

@app.route('/userMode')
def userMode():
    return render_template('userMode.html')

@app.route('/showTable', methods=['post', 'get'])
def showTable():
    obj = (request.args.get('obj'))
    cond = (request.args.get('cond'))
    print(cond)
    DB = SqlOp()
    # print(obj,cond)
    try:
        data = DB.select(obj,condition=cond)
        cols = DB.getCol(obj)
    except:
        data = 'ERROR'
        cols = 'ERROR'
    return render_template('showTable.html',data=data,colnames = cols)

@app.route('/insertData', methods=['post', 'get'])
def insertData():
    obj = (request.args.get('obj'))
    data = eval((request.args.get('data')))
    DB = SqlOp()

    sql = '''
    insert into {} values ('''.format(obj)
    sql = sql+','.join(data.split(';'))[:-1]+')'
    #     sql=sql+i
    # sql = sql[:-2]+')'
    print(sql)
    try:
        # data = DB.select(obj,condition=cond)
        # cols = DB.getCol(obj)
        DB.runSql(sql)
        res = 1
    except:
        # data = 'ERROR'
        res = 0

    return str(res)


@app.route('/getCols', methods=['post', 'get'])
def getCols():
    data = False
    info=''
    obj = (request.args.get('obj'))
    try:
        data = eval((request.args.get('data')))
    except:
        print('no data')
    print(data)
    DB = SqlOp()
    if data == True:
        cond = (request.args.get('cond'))
        info = (DB.select(obj,condition=cond))
        print(info)
        info = list(info)
        print(info)
    try:
        # data = DB.select(obj,condition=cond)
        cols = DB.getCol(obj)
    except:
        # data = 'ERROR'
        cols = 'ERROR'
    print(str([cols,info]))
    if data == True:
        return str([cols,info])
    else:
        return str(cols)

@app.route('/delData', methods=['post', 'get'])
def delData():
    obj = (request.args.get('obj'))
    cond = (request.args.get('cond'))
    DB = SqlOp()
    try:
        # data = DB.select(obj,condition=cond)
        DB.delete(obj,cond)
        res = 1
    except:
        # data = 'ERROR'
        res =0
        print(str(res))
    return str(res)








if __name__ == '__main__':
    app.run()
