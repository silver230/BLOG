from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Blog title',validators=[Required()])
    content = StringField('lets talk about it',validators=[Required()])
    category = SelectField('Category', choices=[('Choose Category', 'Choose Category'),('Love', 'Love'),('business', 'business '),('Interview ', 'Interview'),('Politics', 'Politics')])
    review = TextAreaField('Blog review', validators=[Required()])
    submit = SubmitField('Submit')
 
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please, tell us something about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')
