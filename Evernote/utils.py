#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
This module defines:

    + Application utils methods

.. modeule: utils.py

    :synopsis: Application utils methods

------

"""
import os
import json

STATIC_FILE_ROOT_PAHT = "/usr/share/evernote"

yinxiang_login_url = "https://app.yinxiang.com/Login.action"
evernote_login_url = "https://www.evernote.com/Login.action"


def get_url_by_region():
    """
    Get Evernote / Yinxiang server by current location
    Servers can be Evernote International or Yinxiang Biji (China)
    :return: Server Url
    :rtype: string
    """
    current_country = get_os_country()
    return yinxiang_login_url if current_country == 'CN' else evernote_login_url


def get_os_country():
    """
    Get current OS country according to current timezone
    Note: return 'US' as default country / Rest of the world,
          if country not found or any exception occrued
    :return: Country code of current location
    :rtype: string
    """
    country_code = 'US'
    try:
        # get Geo id
        with open(os.path.join(STATIC_FILE_ROOT_PAHT, 'TZ_L2W.json')) as f:
            json_data = f.read()
            U2W = json.loads(json_data)
            timezone_file = '/etc/timezone'
            with open(timezone_file, 'rb') as tf:
                timezone = tf.read().strip()
                geo_id = U2W.get(timezone.decode(), None)

        # parse geoid to country name struct, and get short name
        with open(os.path.join(STATIC_FILE_ROOT_PAHT, 'Geo2CY.json')) as f:
            json_data = f.read()
            json_country = json.loads(json_data)
            country_detail = json_country[str(geo_id)]
            country_short_name = country_detail['short_name']

        # mapping country short name to country Two letter ISO code
        with open(os.path.join(STATIC_FILE_ROOT_PAHT, 'CountryName.json'), encoding="ISO-8859-1") as f:
            json_data = f.read()
            json_country_code = json.loads(json_data)
            for country_item in json_country_code:
                if country_short_name == country_item.get('Name'):
                    # will get None if short name not match
                    country_code = country_item.get('TwoLetterIsoCode')

        # if no matching country ISO code found, return default code
        if not country_code:
            country_code = 'US'
        return country_code

    except Exception as e:
        return country_code
