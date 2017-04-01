import pytest
from fstring427.fstring import f

def test_simple():
    y="class"
    assert str(f('{y}')) == format(y)
    assert str(f('{y}')) == 'class'
    assert str(f('{{')) == '{'
    assert str(f('a{{')) == 'a{'
    assert str(f('{{b')) == '{b'
    assert str(f('a{{b')) == 'a{b'
    assert str(f('}}')) == '}'
    assert str(f('a}}')) == 'a}'
    assert str(f('}}b')) == '}b'
    assert str(f('a}}b')) == 'a}b'
    assert str(f('{{}}')) == '{}'
    assert str(f('a{{}}')) == 'a{}'
    assert str(f('{{b}}')) == '{b}'
    assert str(f('{{}}c')) == '{}c'
    assert str(f('a{{b}}')) == 'a{b}'
    assert str(f('a{{}}c')) == 'a{}c'
    assert str(f('{{b}}c')) == '{b}c'
    assert str(f('a{{b}}c')) == 'a{b}c'

def test_constant():
    assert str(f('{{{10}')) == '{10'
    assert str(f('}}{10}')) == '}10'
    assert str(f('}}{{{10}')) == '}{10'
    assert str(f('}}a{{{10}')) == '}a{10'
    assert str(f('{10}{{')) == '10{'
    assert str(f('{10}}}')) == '10}'
    assert str(f('{10}}}{{')) == '10}{'
    assert str(f('{10}}}a{{'))+ '}' == '10}a{}'

def test_braces():
    assert str(f('{"{{}}"}')) == '{{}}'

def test_concat():
    x = 'def'
    assert 'abc' +  str(f('## {x}ghi')) == 'abc## defghi'

import string
a_global = "really a local"
def test_complex_eval():
    assert str(f('{3,}')) == '(3,)'
    assert "module 'string' from" in str(f('{string}'))
    assert str(f('g:{a_global}')) == 'g:really a local'
    assert str(f('g:{a_global!r}')) == "g:'really a local'"
    assert str(f('{[x for x in range(5)]}')) == '[0, 1, 2, 3, 4]'
    assert str(f('{3.14:!<10.10}')) == '3.14!!!!!!'

def test_lookups():
    a = 0
    d = {"#":"hash",0:'integer',"a":"string","'":"squote","foo":"bar"}
    assert str(f('{"#"}')) == '#'
    assert str(f('{d["#"]}')) == 'hash'
    assert str(f('{d[0]}')) == 'integer'
    assert str(f('{d["a"]}')) == 'string'
    assert str(f('''{d["'"]}''')) == 'squote'
    assert str(f('{d["foo"]}')) == 'bar'
    # This one does not pass because it's not really 3.6
    with pytest.raises(AssertionError):
        assert str(f('{d[a]}')) == 'integer'
    assert str(f('{d[a]}')) == 'string'

def test_variable_formatting():
    value = 12.35
    width = 10
    precision=2
    # Needs the trailing }f on 2.7
    assert str(f('result: {value:{width}.{precision}f}')) == 'result:      12.35'
    assert str(f('result: {value:{width!r}.{precision}f}')) == 'result:      12.35'
    assert str(f('result: {value:{width:0}.{precision:1}f}')) == 'result:      12.35'
