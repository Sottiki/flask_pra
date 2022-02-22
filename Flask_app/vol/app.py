from flask import Flask, render_template,request
import codecs
import os 
import datetime

app = Flask(__name__)


@app.route("/")
def index():
  return render_template('index.html')

#メモを追加する
#ここでは送信された文字列を記録して更新。名前を消してメモのタイムスタンプを表示したい
@app.route("/add",methods=['GET','POST'])
def add_log():
  values = "add the log"
  log = request.form["log"]     #各フォームタグから値を取得
  name = request.form["name"]

#タイムスタンプの取得
  dt_now = datetime.datetime.now()
  str_dt_now = dt_now.strftime('%Y–%m–%d/%H:%M:%S')
#メモを書き込み
  file = codecs.open("logfile.txt",'a',"utf-8")
  file.write(str_dt_now + "," + log + "," + name + "\n")
  file.close()

  return render_template('index.html',massage=values)

#テキストファイルを全て表示する
@app.route("/all")
def all_log():
  values = "全てのメモを表示する"
  file = codecs.open("logfile.txt", "r", "utf-8")
  lines = file.readlines()
  file.close()
  return render_template('show.html',massage=values,lines = lines)

#最新のメモを削除する。Linuxコマンドを直接実行してテキストファイルに変更を加える。
@app.route("/delete")
def delete_log():
  values = "削除"
  file_path = 'logfile.txt'
  os.system('sed -i "$ d" {0}'.format(file_path))

  return render_template('delete.html',massage=values)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5001)
