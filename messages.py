from db import db
from flask import session
import accounts

def send(topic, content):
    account_id = accounts.account_id()
    posted_by = session.get("username",0)
    if account_id == 0:
        return False
    sql = "INSERT INTO messages (account_id, topic, content, posted_at, posted_by) VALUES (:account_id, :topic, :content, NOW(), :posted_by);"
    db.session.execute(sql, {"account_id":account_id, "topic":topic, "content":content, "posted_by":posted_by})
    db.session.commit()
    return True
       
def get_list():
    sql = "SELECT * FROM messages;"
    result = db.session.execute(sql)
    return result.fetchall()
    
def mes_id(id):
    sql = "SELECT * FROM messages WHERE id=:id;"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()