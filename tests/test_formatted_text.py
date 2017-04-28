from __future__ import unicode_literals
from prompt_toolkit.layout.formatted_text import HTML, to_formatted_text


def test_basic_html():
    html = HTML('<i>hello</i>')
    assert to_formatted_text(html) == [('class:i', 'hello')]

    html = HTML('<i><b>hello</b></i>')
    assert to_formatted_text(html) == [('class:i,b', 'hello')]

    html = HTML('<i><b>hello</b>world<strong>test</strong></i>after')
    assert to_formatted_text(html) == [
        ('class:i,b', 'hello'),
        ('class:i', 'world'),
        ('class:i,strong', 'test'),
        ('', 'after'),
    ]

def test_html_with_fg_bg():
    html = HTML('<style bg="ansired">hello</style>')
    assert to_formatted_text(html) == [
        ('bg:ansired', 'hello'),
    ]

    html = HTML('<style bg="ansired" fg="#ff0000">hello</style>')
    assert to_formatted_text(html) == [
        ('fg:#ff0000 bg:ansired', 'hello'),
    ]

    html = HTML('<style bg="ansired" fg="#ff0000">hello <world fg="ansiblue">world</world></style>')
    assert to_formatted_text(html) == [
        ('fg:#ff0000 bg:ansired', 'hello '),
        ('class:world fg:ansiblue bg:ansired', 'world'),
    ]