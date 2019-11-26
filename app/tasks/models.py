from .. import db
from datetime import datetime, date
class Task(db.Model):
    __tablename__ = 'tasks'
    taskid = db.Column(db.Integer, primary_key=True)
    tasktitle = db.Column(db.String(100), nullable = False)
    taskdescription = db.Column(db.Text(), nullable = True)
    createdate = db.Column(db.DateTime(), default=datetime.now)
    enddate = db.Column(db.Date(),nullable = True)
    endtime = db.Column(db.Time(),nullable = True)
    status = db.Column(db.Integer, default=1)
   
    def __repr__(self):
        return '%s-%s' % (self.taskid,self.tasktitle)