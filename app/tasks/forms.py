from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextField,\
                    DateField, TimeField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, Optional

class createTodo(FlaskForm):
    tasktitle = StringField('Title', validators=[DataRequired(),Length(min=4,max=100,message='Length from 4 to 100 characters!')])
    taskdescription = TextField('Note')
    enddate = DateField('End Date',validators=[Optional()])
    endtime = TimeField('End Time',validators=[Optional()])
    submit = SubmitField('Create Todo')



