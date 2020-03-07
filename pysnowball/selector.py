import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls


def select(size,add_par):
    params = {
            "category": "CN",
            "exchange": "sh_sz",
            "areacode": "",
            "indcode": "",
            "order_by": "symbol",
            "order": "desc",
            "page": "1",
            "size": "%s"%size,
            "only_count": "0",
            "current": "",
            "pct": "",
            #"roediluted.20181231": "20_30",
            "_": "1583502027211"
            }

    for dic in add_par:
        params.update(dic)
    url = api_ref.sel_url
    return utls.fetch_with_params(url = url,host = 'xueqiu.com',params = params)