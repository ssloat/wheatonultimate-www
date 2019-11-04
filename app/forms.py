from flask_wtf import FlaskForm

from wtforms import RadioField

class GoogleGroups(FlaskForm):
    group = RadioField(
        'Which emails do you want:',
        choices = [
            ('wheaton-ultimate', 'Ultimate frisbee games and social events'),
            ('wheaton-ultimate-abridged', 'Ultimate frisbee games'),
            ('wheaton-soccer', 'Soccer games'),
            ('wheaton-housing', 'Housing roommates/tenants'),
        ],
        default = 'wheaton-ultimate',
    )
