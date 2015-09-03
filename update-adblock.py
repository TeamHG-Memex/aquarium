#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib2


FILTERS = {
    "easylist": "https://easylist-downloads.adblockplus.org/easylist.txt",
    "easyprivacy": "https://easylist-downloads.adblockplus.org/easyprivacy.txt",
    # "easyprivacy_nointernational": "https://easylist-downloads.adblockplus.org/easyprivacy_nointernational.txt",
    "easylist_noadult": "https://easylist-downloads.adblockplus.org/easylist_noadult.txt",
    # "antiadblockfilters": "https://easylist-downloads.adblockplus.org/antiadblockfilters.txt",
    "fanboy-annoyance": "https://easylist-downloads.adblockplus.org/fanboy-annoyance.txt",
    "fanboy-social": "https://easylist-downloads.adblockplus.org/fanboy-social.txt",
    # "easylistgermany": "https://easylist-downloads.adblockplus.org/easylistgermany.txt",
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
            data = urllib2.urlopen(url, timeout=10).read()
        except Exception as e:
            print(e)
        else:
            fn = os.path.join(path, name+".txt")
            with open(fn, 'wb') as f:
                f.write(data)


if __name__ == '__main__':
    update(os.path.join("{{cookiecutter.folder_name}}", "filters"))
