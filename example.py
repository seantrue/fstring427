# From https://www.python.org/dev/peps/pep-0498/#examples-from-python-s-source-code
from fstring427.fstring import f, printf
import fstring427.flogging as logging

def examples_from_python():
    class Extra(object):
        def __init__(self):
            self._waiters = [1,2]
        def test(self, extra):
            extra1 = '{},waiters:{}'.format(extra, len(self._waiters))
            extra2 = str(f('{extra},waiters:{len(self._waiters)}'))
            assert extra1 == extra2
    e = Extra()
    e.test("x")

    lineno = 123
    m1 = " [line {0:2d}]".format(lineno)
    m2 = str(f(" [line {lineno:2d}]"))
    assert m1 == m2

    c_basename = "some_class_name"
    m1 = methoddef_name = "{}_METHODDEF".format(c_basename.upper())
    m2 = methoddef_name = str(f("{c_basename.upper()}_METHODDEF"))
    assert m1 == m2

    class Sys(object):
        def __init__(self, *args):
            self.argv = list(args)
    xsys = Sys("someprogram.py","arg0")
    valid_opts=["option"]

    print "Usage: {0} [{1}]".format(xsys.argv[0], '|'.join('--'+opt for opt in valid_opts))
    print f("Usage: {xsys.argv[0]} [{'|'.join('--'+opt for opt in valid_opts)}]")
    printf("Usage: {xsys.argv[0]} [{'|'.join('--'+opt for opt in valid_opts)}]")
    printf("Usage: {xsys.argv[0]} [{opts}]", opts = '|'.join('--'+opt for opt in valid_opts))
    for i in range(10):
        s = str(f("{i*10}"))

def logging_examples():
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    for i in range(10):
        logger.warning("i={i*10}")

    class Bar(object):
        def __init__(self, *args, **kwargs):
            super(Bar, self).__init__()
        def test(self,a,b,c):
            self.error("a={a} {b}*{c}={b*c}")

    class Foo(Bar, logging.Flogging):
        pass
    
    foo = Foo()
    foo.test("alpha", 10, 20)
if __name__ == "__main__":
    import sys
    examples_from_python()
    logging_examples()
    f.showstat(stream=sys.stdout)
