from time import time #line:3
from hashlib import md5 #line:4
from copy import deepcopy #line:5
from urllib .parse import urlparse #line:6
from urllib .parse import parse_qs #line:7
from urllib .parse import urlencode #line:8
import requests #line:9
import json #line:10
from flask import Flask #line:11
from flask import request #line:12
import base64 #line:13
app =Flask (__name__ )#line:15
class XGorgon0404 :#line:18
    def encryption (en_input ):#line:19
        non_first =''#line:20
        list =[]#line:21
        for inlist in range (0 ,256 ):#line:22
            list .append (inlist )#line:23
        for inlist in range (0 ,256 ):#line:24
            if inlist ==0 :#line:25
                e0 =0 #line:26
            elif non_first :#line:27
                e0 =non_first #line:28
            else :#line:29
                e0 =list [inlist -1 ]#line:30
            hex_var =en_input .hex_str [inlist %8 ]#line:31
            if e0 ==85 :#line:32
                if inlist !=1 :#line:33
                    if non_first !=85 :#line:34
                        e0 =0 #line:35
            namberinw =e0 +inlist +hex_var #line:36
            while namberinw >=256 :#line:37
                namberinw =namberinw -256 #line:38
            if namberinw <inlist :#line:39
                non_first =namberinw #line:40
            else :#line:41
                non_first =''#line:42
            workwlist =list [namberinw ]#line:43
            list [inlist ]=workwlist #line:44
        return list #line:45
    def initialize (initinput1 ,initinput2 ,initinput3 ):#line:47
        anthor_list =[]#line:48
        non_sec =deepcopy (initinput3 )#line:49
        for xvarfor in range (initinput1 .length ):#line:50
            non_therd =initinput2 [xvarfor ]#line:51
            if not anthor_list :#line:52
                e02 =0 #line:53
            else :#line:54
                e02 =anthor_list [-1 ]#line:55
            workwx =initinput3 [xvarfor +1 ]+e02 #line:56
            while workwx >=256 :#line:57
                workwx =workwx -256 #line:58
            anthor_list .append (workwx )#line:59
            workvar1 =non_sec [workwx ]#line:60
            non_sec [xvarfor +1 ]=workvar1 #line:61
            workw256 =workvar1 +workvar1 #line:62
            while workw256 >=256 :#line:63
                workw256 =workw256 -256 #line:64
            varindef =non_sec [workw256 ]#line:65
            varindef2 =non_therd ^varindef #line:66
            initinput2 [xvarfor ]=varindef2 #line:67
        return initinput2 #line:68
    def handle (hainput1 ,hainput2 ):#line:70
        for varinforindefha in range (hainput1 .length ):#line:71
            varinha1 =hainput2 [varinforindefha ]#line:72
            varinha2 =choice (varinha1 )#line:73
            varinha3 =hainput2 [(varinforindefha +1 )%hainput1 .length ]#line:74
            varinha4 =varinha2 ^varinha3 #line:75
            varinha5 =rbpt (varinha4 )#line:76
            varinha6 =varinha5 ^hainput1 .length #line:77
            workinwha =~varinha6 #line:78
            while workinwha <0 :#line:79
                workinwha +=4294967296 #line:80
            varinha8 =int (hex (workinwha )[-2 :],16 )#line:81
            hainput2 [varinforindefha ]=varinha8 #line:82
        return hainput2 #line:83
    def main (inputinma ):#line:85
        e0inma =''#line:86
        for workinforinma in inputinma .handle (inputinma .initialize (inputinma .debug ,inputinma .encryption ())):#line:87
            e0inma =e0inma +hex2string (workinforinma )#line:88
        varinma1 =hex2string (inputinma .hex_str [7 ])#line:90
        varinma2 =hex2string (inputinma .hex_str [3 ])#line:91
        return '0404{}{}0001{}'.format (varinma1 ,varinma2 ,e0inma )#line:92
    def __init__ (inputin__ ,inputin__2 ):#line:94
        inputin__ .length =20 #line:95
        inputin__ .debug =inputin__2 #line:96
        inputin__ .hex_str =[30 ,0 ,224 ,228 ,147 ,69 ,1 ,208 ]#line:97
def choice (inputinch1 ):#line:100
    varinch1 =hex (inputinch1 )[2 :]#line:101
    if len (varinch1 )<2 :#line:102
        varinch1 ='0'+varinch1 #line:103
    return int (varinch1 [1 :]+varinch1 [:1 ],16 )#line:104
def rbpt (inputinrb ):#line:107
    varinrb =''#line:108
    varinrb2 =bin (inputinrb )[2 :]#line:109
    while len (varinrb2 )<8 :#line:110
        varinrb2 ='0'+varinrb2 #line:111
    for workinrbfor in range (0 ,8 ):#line:112
        varinrb =varinrb +varinrb2 [7 -workinrbfor ]#line:113
    return int (varinrb ,2 )#line:114
def hex2string (inputinhex2 ):#line:117
    varinhexs1 =hex (inputinhex2 )[2 :]#line:118
    if len (varinhexs1 )<2 :#line:119
        varinhexs1 ='0'+varinhexs1 #line:120
    return varinhexs1 #line:121
@app .route ('/sign')#line:123
def X_Gorgon0404 ():#line:124
    decode_url =str (base64 .b64decode ("url=residence=IQ&device_id=7092527186544330246&os_version=15.3&iid=7092527941028710149&app_name=musical_ly&locale=en&ac=WIFI&sys_region=US&js_sdk_version=1.77.0.2&version_code=19.3.0&vid=C6A977A1-AC7C-4D0E-9533-1FCD3972CE85&channel=App%20Store&op_region=US&tma_jssdk_version=1.77.0.2&os_api=18&idfa=00000000-0000-0000-0000-000000000000&device_platform=ipad&device_type=iPad8,9&openudid=c920d54dabfbf4123671b88bb1c0b142e7ea4d6a&account_region=&tz_name=Asia/Baghdad&tz_offset=10800&app_language=en&current_region=IQ&build_number=193021&aid=1233&mcc_mnc=&screen_width=1668&uoo=1&content_language=&language=en&cdid=05581917-5ED8-4DB2-BDA1-00AB5F200527&app_version=19.3.0&unique_id=user6"),"utf-8"))#line:125
    print (decode_url )#line:126
    decode_url =splitParams (decode_url )#line:127
    data =""#line:128
    print (data )#line:129
    e0inx_g ='' #str (base64 .b64decode (request .args .get ('cookie')),"utf-8")#line:130
    print (e0inx_g )#line:131
    utf_8 ='utf-8'#line:132
    list_in_X_G =[]#line:134
    var1_Xg =hex (int (time ()))[2 :]#line:135
    var2_Xg =md5 (bytearray (decode_url ,'utf-8')).hexdigest ()#line:136
    for workinxgfor in range (0 ,4 ):#line:137
        list_in_X_G .append (int (var2_Xg [2 *workinxgfor :2 *workinxgfor +2 ],16 ))#line:138
    if OO00OO00O0OOOOO00 :#line:139
        if utf_8 =='utf-8':#line:140
            OOO0OO00O0OO0000O =md5 (bytearray (OO00OO00O0OOOOO00 ,'utf-8')).hexdigest ()#line:141
            for workinxgfor in range (0 ,4 ):#line:142
                list_in_X_G .append (int (OOO0OO00O0OO0000O [2 *workinxgfor :2 *workinxgfor +2 ],16 ))#line:143
        elif O0O0OO000OOOOO0O0 =='octet':#line:144
            OOO0OO00O0OO0000O =md5 (OO00OO00O0OOOOO00 ).hexdigest ()#line:145
            for workinxgfor in range (0 ,4 ):#line:146
                list_in_X_G .append (int (OOO0OO00O0OO0000O [2 *workinxgfor :2 *workinxgfor +2 ],16 ))#line:147
    else :#line:148
        for workinxgfor in range (0 ,4 ):#line:149
            list_in_X_G .append (0 )#line:150
    if O0O0OOO0OOO0OO0O0 :#line:151
        OOOOO000OO0O0O0OO =md5 (bytearray (O0O0OOO0OOO0OO0O0 ,'utf-8')).hexdigest ()#line:152
        for workinxgfor in range (0 ,4 ):#line:153
            list_in_X_G .append (int (OOOOO000OO0O0O0OO [2 *workinxgfor :2 *workinxgfor +2 ],16 ))#line:154
    else :#line:155
        for workinxgfor in range (0 ,4 ):#line:156
            list_in_X_G .append (0 )#line:157
    for workinxgfor in range (0 ,4 ):#line:158
        list_in_X_G .append (0 )#line:159
    for workinxgfor in range (0 ,4 ):#line:160
        list_in_X_G .append (int (var1_Xg [2 *workinxgfor :2 *workinxgfor +2 ],16 ))#line:161
    return {'xgorgon':XGorgon0404 (list_in_X_G ).main (),'ts':str (int (var1_Xg ,16 ))}#line:162
def splitParams (inputinsp ):#line:164
    varinsp1 =inputinsp .split ('?')[1 ]#line:165
    return varinsp1 #line:166
def replaceParams (inputinrep1 ,inputinrep2 ):#line:169
    var1inrep =urlparse (inputinrep1 )#line:170
    var2inrep =parse_qs (var1inrep .query )#line:172
    for forworkinrep in inputinrep2 :#line:174
        if var2inrep .get (forworkinrep ):#line:175
            var2inrep [forworkinrep ][0 ]=str (inputinrep2 [forworkinrep ])#line:176
    _var3inrep ={}#line:178
    for forworkinrep in var2inrep :#line:179
        _var3inrep [forworkinrep ]=var2inrep [forworkinrep ][0 ]#line:180
    return '%s://%s%s?%s'%(var1inrep .scheme ,var1inrep .netloc ,var1inrep .path ,urlencode (_var3inrep ))#line:181
