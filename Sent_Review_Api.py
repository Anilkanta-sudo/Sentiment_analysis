from flask import Flask, jsonify, request

app = Flask(__name__)
from flask_mysqldb import MySQL
import SentimentAnal
app.config['SECRET_KEY']="this is secret key"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_DB'] = 'db_name'
mysql = MySQL(app)

@app.route('/sentiment', methods=['POST'])
def sentiment_anyalisis():
    """
    Sentiment analysis API
    """
    data = request.get_json()
    data = data['text']
    res = SentimentAnal.sentiment_analyse(data)
    return jsonify({"message": res})


@app.route('/review', methods=['POST'])
def reviws():
    """
    Reviews based on color,size,text,and title
    """
    data = request.get_json()
    try:
        text= data.get("text","")
        col = data.get('color',"")
        siz=data.get('size',"")
        title=data.get('title',"")
    except Exception as e:
        return {"message":f"Please Pass any of these Params color/text/title/size"}

    cur = mysql.connection.cursor()
    sql = f"select review_text from reviews where review_title='{title}' or color='{col}' or size='{siz}' or review_text='{text}'"
    cur.execute(sql)
    data = cur.fetchall()
    return jsonify({"message": data})


if __name__ == '__main__':
    app.run(debug=True)
