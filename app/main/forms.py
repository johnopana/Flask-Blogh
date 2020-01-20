from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
class PostForm(FlaskForm):
    title = StringField('post  title',validators=[Required()])
    content = TextAreaField('post body', validators=[Required()])
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
    title = StringField('comment title',validators=[Required()])
    content = TextAreaField('comment body', validators=[Required()])
    submit = SubmitField('Add Comment')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')