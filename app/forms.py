from flask_wtf import FlaskForm

from wtforms import RadioField

class GoogleGroups(FlaskForm):
    group = RadioField(
        'Which emails do you want:',
        choices = [
            ('wheaton-ultimate', 'Social events'),
            ('wheaton-ultimate-frisbee', 'Ultimate frisbee games'),
            ('wheaton-soccer', 'Soccer games'),
            ('wheaton-housing', 'Housing roommates/tenants'),
        ],
        default = 'wheaton-ultimate',
    )
