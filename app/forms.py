from flask_wtf import FlaskForm

from wtforms import RadioField, SelectMultipleField, widgets

class MultiCheckBoxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class GoogleGroupsSubscribe(FlaskForm):
    group = MultiCheckBoxField(
        'Which emails are you signing up for?',
        choices = [
            ('wheaton-ultimate-events', 'Social events'),
            ('wheaton-ultimate-frisbee', 'Ultimate frisbee games'),
            ('wheaton-soccer', 'Soccer games'),
            ('wheaton-housing', 'Housing roommates/tenants'),
        ],
    )

class GoogleGroupsUnsubscribe(FlaskForm):
    group = MultiCheckBoxField(
        'Which emails are you unsubscribing from?',
        choices = [
            ('wheaton-ultimate-events', 'Social events'),
            ('wheaton-ultimate-frisbee', 'Ultimate frisbee games'),
            ('wheaton-soccer', 'Soccer games'),
            ('wheaton-housing', 'Housing roommates/tenants'),
        ],
    )
