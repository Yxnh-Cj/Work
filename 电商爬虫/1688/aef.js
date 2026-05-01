u = function(e) {
                                    function t(e, t) {
                                        return e << t | e >>> 32 - t
                                    }
                                    function n(e, t) {
                                        var n, o, r, i, a;
                                        return r = 2147483648 & e,
                                        i = 2147483648 & t,
                                        n = 1073741824 & e,
                                        o = 1073741824 & t,
                                        a = (1073741823 & e) + (1073741823 & t),
                                        n & o ? 2147483648 ^ a ^ r ^ i : n | o ? 1073741824 & a ? 3221225472 ^ a ^ r ^ i : 1073741824 ^ a ^ r ^ i : a ^ r ^ i
                                    }
                                    function o(e, o, r, i, a, s, c) {
                                        return e = n(e, n(n(o & r | ~o & i, a), c)),
                                        n(t(e, s), o)
                                    }
                                    function r(e, o, r, i, a, s, c) {
                                        return e = n(e, n(n(o & i | r & ~i, a), c)),
                                        n(t(e, s), o)
                                    }
                                    function i(e, o, r, i, a, s, c) {
                                        return e = n(e, n(n(o ^ r ^ i, a), c)),
                                        n(t(e, s), o)
                                    }
                                    function a(e, o, r, i, a, s, c) {
                                        return e = n(e, n(n(r ^ (o | ~i), a), c)),
                                        n(t(e, s), o)
                                    }
                                    function s(e) {
                                        var t, n = "", o = "";
                                        for (t = 0; 3 >= t; t++)
                                            n += (o = "0" + (e >>> 8 * t & 255).toString(16)).substr(o.length - 2, 2);
                                        return n
                                    }
                                    var c, u, l, d, p, f, m, g, h, _ = [];
                                    for (_ = function(e) {
                                        for (var t, n = e.length, o = n + 8, r = 16 * ((o - o % 64) / 64 + 1), i = Array(r - 1), a = 0, s = 0; n > s; )
                                            t = (s - s % 4) / 4,
                                            a = s % 4 * 8,
                                            i[t] = i[t] | e.charCodeAt(s) << a,
                                            s++;
                                        return t = (s - s % 4) / 4,
                                        a = s % 4 * 8,
                                        i[t] = i[t] | 128 << a,
                                        i[r - 2] = n << 3,
                                        i[r - 1] = n >>> 29,
                                        i
                                    }(e = function(e) {
                                        e = e.replace(/\r\n/g, "\n");
                                        for (var t = "", n = 0; n < e.length; n++) {
                                            var o = e.charCodeAt(n);
                                            128 > o ? t += String.fromCharCode(o) : o > 127 && 2048 > o ? t += String.fromCharCode(o >> 6 | 192) + String.fromCharCode(63 & o | 128) : t += String.fromCharCode(o >> 12 | 224) + String.fromCharCode(o >> 6 & 63 | 128) + String.fromCharCode(63 & o | 128)
                                        }
                                        return t
                                    }(e)),
                                    f = 1732584193,
                                    m = 4023233417,
                                    g = 2562383102,
                                    h = 271733878,
                                    c = 0; c < _.length; c += 16)
                                        u = f,
                                        l = m,
                                        d = g,
                                        p = h,
                                        f = o(f, m, g, h, _[c + 0], 7, 3614090360),
                                        h = o(h, f, m, g, _[c + 1], 12, 3905402710),
                                        g = o(g, h, f, m, _[c + 2], 17, 606105819),
                                        m = o(m, g, h, f, _[c + 3], 22, 3250441966),
                                        f = o(f, m, g, h, _[c + 4], 7, 4118548399),
                                        h = o(h, f, m, g, _[c + 5], 12, 1200080426),
                                        g = o(g, h, f, m, _[c + 6], 17, 2821735955),
                                        m = o(m, g, h, f, _[c + 7], 22, 4249261313),
                                        f = o(f, m, g, h, _[c + 8], 7, 1770035416),
                                        h = o(h, f, m, g, _[c + 9], 12, 2336552879),
                                        g = o(g, h, f, m, _[c + 10], 17, 4294925233),
                                        m = o(m, g, h, f, _[c + 11], 22, 2304563134),
                                        f = o(f, m, g, h, _[c + 12], 7, 1804603682),
                                        h = o(h, f, m, g, _[c + 13], 12, 4254626195),
                                        g = o(g, h, f, m, _[c + 14], 17, 2792965006),
                                        m = o(m, g, h, f, _[c + 15], 22, 1236535329),
                                        f = r(f, m, g, h, _[c + 1], 5, 4129170786),
                                        h = r(h, f, m, g, _[c + 6], 9, 3225465664),
                                        g = r(g, h, f, m, _[c + 11], 14, 643717713),
                                        m = r(m, g, h, f, _[c + 0], 20, 3921069994),
                                        f = r(f, m, g, h, _[c + 5], 5, 3593408605),
                                        h = r(h, f, m, g, _[c + 10], 9, 38016083),
                                        g = r(g, h, f, m, _[c + 15], 14, 3634488961),
                                        m = r(m, g, h, f, _[c + 4], 20, 3889429448),
                                        f = r(f, m, g, h, _[c + 9], 5, 568446438),
                                        h = r(h, f, m, g, _[c + 14], 9, 3275163606),
                                        g = r(g, h, f, m, _[c + 3], 14, 4107603335),
                                        m = r(m, g, h, f, _[c + 8], 20, 1163531501),
                                        f = r(f, m, g, h, _[c + 13], 5, 2850285829),
                                        h = r(h, f, m, g, _[c + 2], 9, 4243563512),
                                        g = r(g, h, f, m, _[c + 7], 14, 1735328473),
                                        m = r(m, g, h, f, _[c + 12], 20, 2368359562),
                                        f = i(f, m, g, h, _[c + 5], 4, 4294588738),
                                        h = i(h, f, m, g, _[c + 8], 11, 2272392833),
                                        g = i(g, h, f, m, _[c + 11], 16, 1839030562),
                                        m = i(m, g, h, f, _[c + 14], 23, 4259657740),
                                        f = i(f, m, g, h, _[c + 1], 4, 2763975236),
                                        h = i(h, f, m, g, _[c + 4], 11, 1272893353),
                                        g = i(g, h, f, m, _[c + 7], 16, 4139469664),
                                        m = i(m, g, h, f, _[c + 10], 23, 3200236656),
                                        f = i(f, m, g, h, _[c + 13], 4, 681279174),
                                        h = i(h, f, m, g, _[c + 0], 11, 3936430074),
                                        g = i(g, h, f, m, _[c + 3], 16, 3572445317),
                                        m = i(m, g, h, f, _[c + 6], 23, 76029189),
                                        f = i(f, m, g, h, _[c + 9], 4, 3654602809),
                                        h = i(h, f, m, g, _[c + 12], 11, 3873151461),
                                        g = i(g, h, f, m, _[c + 15], 16, 530742520),
                                        m = i(m, g, h, f, _[c + 2], 23, 3299628645),
                                        f = a(f, m, g, h, _[c + 0], 6, 4096336452),
                                        h = a(h, f, m, g, _[c + 7], 10, 1126891415),
                                        g = a(g, h, f, m, _[c + 14], 15, 2878612391),
                                        m = a(m, g, h, f, _[c + 5], 21, 4237533241),
                                        f = a(f, m, g, h, _[c + 12], 6, 1700485571),
                                        h = a(h, f, m, g, _[c + 3], 10, 2399980690),
                                        g = a(g, h, f, m, _[c + 10], 15, 4293915773),
                                        m = a(m, g, h, f, _[c + 1], 21, 2240044497),
                                        f = a(f, m, g, h, _[c + 8], 6, 1873313359),
                                        h = a(h, f, m, g, _[c + 15], 10, 4264355552),
                                        g = a(g, h, f, m, _[c + 6], 15, 2734768916),
                                        m = a(m, g, h, f, _[c + 13], 21, 1309151649),
                                        f = a(f, m, g, h, _[c + 4], 6, 4149444226),
                                        h = a(h, f, m, g, _[c + 11], 10, 3174756917),
                                        g = a(g, h, f, m, _[c + 2], 15, 718787259),
                                        m = a(m, g, h, f, _[c + 9], 21, 3951481745),
                                        f = n(f, u),
                                        m = n(m, l),
                                        g = n(g, d),
                                        h = n(h, p);
                                    return (s(f) + s(m) + s(g) + s(h)).toLowerCase()
                                }  // 直接跟(s)

// s = e3c048c9cd1e59da1f2a3dfda21cf76e&1777525171499&12574478&{"appId":32517,"params":"{\"beginPage\":\"2\",\"pageSize\":60,\"method\":\"getOfferList\",\"pageId\":\"mqGUVmv2TegvE3J4kbpaAxnteOvZBQyzVaz1oHIOA98y4jzn\",\"verticalProductFlag\":\"pcmarket\",\"searchScene\":\"pcOfferSearch\",\"charset\":\"GBK\",\"spm\":\"a260k.home2025.searchbox.0\",\"keywords\":\"%B4%BF%BA%DA%D4%CB%B6%AF%D0%AC\"}"}