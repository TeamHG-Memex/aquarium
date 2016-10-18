#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests


FILTERS = {
    "easylist": "https://easylist.to/easylist/easylist.txt",
    "easyprivacy": "https://easylist.to/easylist/easyprivacy.txt",
    # "easyprivacy_nointernational": "https://easylist-downloads.adblockplus.org/easyprivacy_nointernational.txt",
    "easylist_noadult": "https://easylist-downloads.adblockplus.org/easylist_noadult.txt",
    # "antiadblockfilters": "https://easylist-downloads.adblockplus.org/antiadblockfilters.txt",
    "fanboy-annoyance": "https://easylist.to/easylist/fanboy-annoyance.txt",
    "fanboy-social": "https://easylist.to/easylist/fanboy-social.txt",
    # "easylistgermany": "https://easylist.to/easylistgermany/easylistgermany.txt",
    # "easylistitaly": "https://easylist-downloads.adblockplus.org/easylistitaly.txt",
    # "easylistdutch": "https://easylist-downloads.adblockplus.org/easylistdutch.txt",
    # "liste_fr": "https://easylist-downloads.adblockplus.org/liste_fr.txt",
    # "easylistchina": "https://easylist-downloads.adblockplus.org/easylistchina.txt",
    # "adblock_bg": "http://stanev.org/abp/adblock_bg.txt",
    # "abpindo": "https://indonesianadblockrules.googlecode.com/hg/subscriptions/abpindo.txt",
    # "liste_ar": "https://liste-ar-adblock.googlecode.com/hg/Liste_AR.txt",
    # "adblock_cz": "https://adblock-czechoslovaklist.googlecode.com/svn/filters.txt",
    # "latvian_list": "https://gitorious.org/adblock-latvian/adblock-latvian/raw/master:lists/latvian-list.txt",
    # "EasyListHebrew": "https://raw.github.com/AdBlockPlusIsrael/EasyListHebrew/master/EasyListHebrew.txt",
    # "easylistlithuania": "http://margevicius.lt/easylistlithuania.txt",
}


def update(path):
    if not os.path.exists(path):
        os.mkdir(path)

    for idx, (name, url) in enumerate(FILTERS.items(), start=1):
        print("[%d/%d] [%s] downloading %s" % (idx, len(FILTERS), name, url))
        try:
            resp = requests.get(url, timeout=10)
        except Exception as e:
            print(e)
        else:
            fn = os.path.join(path, name+".txt")
            with open(fn, 'wb') as f:
                f.write(resp.content)


if __name__ == '__main__':
    update(os.path.join("{{cookiecutter.folder_name}}", "filters"))
