from flask_sqlalchemy import SQLAlchemy # 导入扩展类
from flask import Flask 
app1 = Flask(__name__)
db = SQLAlchemy(app1) # 初始化扩展，传入程序实例 app
class User(db.Model): # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True) # 主键
    name = db.Column(db.String(20)) # 名字
class Movie(db.Model): # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True) # 主键
    title = db.Column(db.String(60)) # 电影标题
    year = db.Column(db.String(4)) # 电影年份
with app1.app_context():
   db.create_all()