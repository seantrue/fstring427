# Copyright (c) 2017 Smartvid.io
import time
from fstring427.fstring import Fmt

ntests = 10000
simple_format = "{a} {b} {c} {d} {e} {f} {g} {h} {i} {j} {k} {l} {m} {n} {o} {p} {q} {r} {s} {t} {u} {v} {w} {x} {y} {z}"
complex_format = "{a*97} {b*98} {c*99} {d*100} {e*101} {f*102} {g*103} {h*104} {i*105} {j*106} {k*107} {l*108} {m*109} {n*110} {o*111} {p*112} {q*113} {r*114} {s*115} {t*116} {u*117} {v*118} {w*119} {x*120} {y*121} {z*122}"
simple_result = "97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122"
complex_result = "9409 9604 9801 10000 10201 10404 10609 10816 11025 11236 11449 11664 11881 12100 12321 12544 12769 12996 13225 13456 13689 13924 14161 14400 14641 14884"


def test_test():
    Fmt._reset()
    a = 97
    c = 99
    b = 98
    e = 101
    d = 100
    g = 103
    f = 102
    i = 105
    h = 104
    k = 107
    j = 106
    m = 109
    l = 108
    o = 111
    n = 110
    q = 113
    p = 112
    s = 115
    r = 114
    u = 117
    t = 116
    w = 119
    v = 118
    y = 121
    x = 120
    z = 122
    for caching in [False, True]:
        for compile_caching in [False, True]:
            Fmt._reset(caching, compile_caching)
            assert str(Fmt(simple_format)) == simple_result
            assert str(Fmt(complex_format)) == complex_result


def test_caching():
    def time_test(label, format, ntests):
        a = 97
        c = 99
        b = 98
        e = 101
        d = 100
        g = 103
        f = 102
        i = 105
        h = 104
        k = 107
        j = 106
        m = 109
        l = 108
        o = 111
        n = 110
        q = 113
        p = 112
        s = 115
        r = 114
        u = 117
        t = 116
        w = 119
        v = 118
        y = 121
        x = 120
        z = 122
        # Warm up the caches, if any
        _ = str(Fmt(format))
        _t = time.time()
        for i in range(ntests):
            _ = str(Fmt(format))
        _t = time.time() - _t
        return _t

    # print
    for label, format in [("simple format", simple_format), ("complex format", complex_format)]:
        times = []
        for caching in [False, True]:
            for compile_caching in [False, True]:
                Fmt._reset(caching, compile_caching)
                t = time_test(label, format, ntests)
                times.append((t, (label, caching, compile_caching)))
        if "simple" in label:
            # print "simple %.3f/%.3f" % (times[3][0] /times[1][0],times[2][0] /times[0][0])
            assert times[3][0] < times[1][0]
            assert times[2][0] < times[0][0]
        if "complex" in label:
            # print "complex %.3f/%.3f" % (times[1][0] /times[0][0],times[3][0] /times[2][0])
            assert times[1][0] < times[0][0]
            assert times[3][0] < times[2][0]
