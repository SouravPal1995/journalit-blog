from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])
    post = TextAreaField("Enter the post", validators = [DataRequired()])
    submit = SubmitField("Post")
    
class PostEditForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])
    post = TextAreaField("Enter the post", validators = [DataRequired()])
    submit = SubmitField("Update Post")
    
