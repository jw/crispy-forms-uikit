"""
Forms crispies items
"""
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms_uikit.layout import (
    Layout, Row, Column
)
# from crispy_forms_uikit.layout import (
#     Layout, Fieldset, HTML, Row, Column, Panel, Callout,
#     ButtonHolder, ButtonHolderPanel, ButtonGroup,
#     Button, Submit, Reset,
#     ButtonElement, ButtonSubmit, ButtonReset,
#     InlineField, InlineJustifiedField,
#     SwitchField, InlineSwitchField
# )
from crispy_forms_uikit.layout.base import HTML
from crispy_forms_uikit.layout.buttons import ButtonGroup, Submit, Reset, Button, ButtonSubmit, ButtonReset, \
    ButtonElement
from crispy_forms_uikit.layout.fields import Field


def part_0_crispies(pack=None):
    return Field()


def part_1_crispies(pack=None):
    return [
        Row(
            Column('full_input'),
        ),
                Row(
                    Column(
                        'column_input_1',
                        css_class='uk-width-1-3'
                    ),
                    Column(
                        'column_input_2',
                        css_class='uk-width-1-3'
                    ),
                    Column(
                        'column_input_3',
                        css_class='uk-width-1-3'
                    ),
        ),
    ]

# def part_2_crispies(pack=None):
#     return [
#         Row(
#             Column(
#                 'select_input',
#                 css_class='uk-width-1-1'
#             ),
#         ),
#         Row(
#             Column(
#                 'radio_input',
#                 css_class='uk-width-1-3'
#             ),
#             Column(
#                 'checkbox_input',
#                 css_class='uk-width-1-3'
#             ),
#             Column(
#                 Row(
#                     Column(
#                         SwitchField('checkbox_switch_input_1', switch_class="round tiny"),
#                         css_class='small-3'
#                     ),
#                     Column(
#                         HTML('<label>Checkbox with a switch field</label>'),
#                         css_class='small-9'
#                     ),
#                 ),
#                 Row(
#                     Column(
#                         InlineSwitchField('checkbox_switch_input_2'),
#                     ),
#                 ),
#                 css_class='large-4'
#             ),
#         ),
#     ]


def part_3_crispies(pack=None):
    return [
        Row(
            Column('textarea_input'),
        ),
    ]
#
#
# def part_4_crispies(pack=None):
#     return [
#         InlineField('inlinefield_input'),
#         InlineJustifiedField('inlinejustifiedfield_input'),
#     ]


def buttons_crispies(pack=None):
    return [
        Row(
            Column(
                ButtonGroup(
                    Submit('submit', _('Submit'), css_class='success'),
                    Reset('cancel', _('Cancel')),
                    Button('dummy', _('Delete'), css_class='alert'),
                    css_class='uk-align-right'
                ),
                css_class='uk-margin uk-width-1-1'
            ),
        ),
        # Row(
        #     Column(
        #         HTML("""<p>As &lt;input/&gt;</p>"""),
        #         ButtonGroup(
        #             Submit('submit', _('Submit'), css_class='success'),
        #             Reset('cancel', _('Cancel')),
        #             Button('dummy', _('Delete'), css_class='alert'),
        #             css_class='radius right'
        #         ),
        #         css_class='clearfix'
        #     ),
        # ),
        # Row(
        #     Column(
        #         HTML("""<p>As &lt;button/&gt;</p>"""),
        #         ButtonGroup(
        #             ButtonSubmit('submit', _('Submit'),
        #                          css_class='success'),
        #             ButtonReset('cancel', _('Cancel')),
        #             ButtonElement('button-label', 'button-value',
        #                           css_class='alert',
        #                           content="""<span>&lt;Doh/&gt;</span>"""),
        #             css_class='radius right'
        #         ),
        #         css_class='clearfix'
        #     ),
        # ),
    ]
