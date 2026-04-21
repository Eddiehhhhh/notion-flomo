import hashlib
import os


def _ksort(d):
    return dict(sorted(d.items()))


def getSign(e):
    """
    生成 flomo API 签名
    安全修复：从环境变量 FLOMO_SIGN_SALT 读取盐值，不再硬编码
    """
    salt = os.environ.get("FLOMO_SIGN_SALT", "")
    if not salt:
        raise ValueError("请设置环境变量 FLOMO_SIGN_SALT")
    e = _ksort(e)
    t = ""
    for i in e:
        o = e[i]
        if o is not None and (o or o == 0):
            if isinstance(o, list):
                o.sort(key=lambda x: x if x else '')
                for item in o:
                    t += f"{i}[]={item}&"
            else:
                t += f"{i}={o}&"
    t = t[:-1]
    return c(t + salt)


def c(t):
    return hashlib.md5(t.encode('utf-8')).hexdigest()
