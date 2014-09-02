# Pipe pipe_e519dd393f943315f7e4128d19db2eac generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipetextinput import pipe_textinput
from pipe2py.modules.pipeurlbuilder import pipe_urlbuilder
from pipe2py.modules.pipefetch import pipe_fetch
from pipe2py.modules.pipeoutput import pipe_output

def pipe_e519dd393f943315f7e4128d19db2eac(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context.describe_input:
        return [(u'', u'q', u'Search term:', u'text', u'enterprise mashup')]

    forever = pipe_forever()


    sw_552 = pipe_textinput(
        context, forever, conf=dict(default=dict(type='text', value='enterprise mashup'), position=dict(type='number', value=''), prompt=dict(type='text', value='Search term:'), name=dict(type='text', value='q'), debug=dict(type='text', value='')))

    sw_492 = pipe_urlbuilder(
        context, forever, PARAM_5_value=sw_552, conf=dict(PATH=dict(type='text', value=''), BASE=dict(type='text', value='http://news.google.com/news'), PARAM=[dict(key=dict(type='text', value='pz'), value=dict(type='text', value='1')), dict(key=dict(type='text', value='cf'), value=dict(type='text', value='all')), dict(key=dict(type='text', value='ned'), value=dict(type='text', value='uk')), dict(key=dict(type='text', value='hl'), value=dict(type='text', value='en')), dict(key=dict(type='text', value='q'), value=dict(terminal='PARAM_5_value', type='text')), dict(key=dict(type='text', value='output'), value=dict(type='text', value='rss'))]))

    sw_481 = pipe_fetch(
        context, forever, _1_URL=sw_492, conf=dict(URL=dict(terminal='1_URL', type='url')))

    _OUTPUT = pipe_output(
        context, sw_481, conf=dict())

    return _OUTPUT


if __name__ == "__main__":
    context = Context()
    pipeline = pipe_e519dd393f943315f7e4128d19db2eac(context, None)

    for i in pipeline:
        print i