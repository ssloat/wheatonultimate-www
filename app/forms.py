from flask_wtf import FlaskForm

from wtforms import RadioField, SelectMultipleField, widgets

class MultiCheckBoxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class GoogleGroups(FlaskForm):
    action = RadioField(
        'Are you signing up or leaving?',
        choices = [
            ('+subscribe', 'Subscribe'),
            ('+unsubscribe', 'Unsubscribe'),
        ],
        default='+subscribe'
    )

    group = MultiCheckBoxField(
        'Which emails are you signing up for or leaving?',
        choices = [
            ('wheaton-ultimate', 'Social events'),
            ('wheaton-ultimate-frisbee', 'Ultimate frisbee games'),
            ('wheaton-soccer', 'Soccer games'),
            ('wheaton-housing', 'Housing roommates/tenants'),
        ],
    )
