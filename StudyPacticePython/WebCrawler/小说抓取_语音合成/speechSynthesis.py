#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 21:19
# @Author  : yb.w
# @File    : speechSynthesis.py  语音合成 百度API

from aip import AipSpeech
class Speech(object):



    # # 读取文件
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()


    '''
    参数	类型	描述	是否必须
    tex	String	合成的文本，使用UTF-8编码，请注意文本长度必须小于1024字节	是
    cuid String	用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内	否
    spd	String	语速，取值0-9，默认为5中语速	否
    pit	String	音调，取值0-9，默认为5中语调	否
    vol	String	音量，取值0-15，默认为5中音量	否
    per	String	发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女	否
    '''

    def get_result(self,file_content):
        # 此内容为百度API信息
        APP_ID = '15310754'
        API_KEY = 'DVpb2PZqsE4EDDwM0lUqEtAa'
        SECRET_KEY = 'nmdaxeQ3gGff7tY0wUIq9Kp060c5Ty2m '

        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        result  = client.synthesis(file_content, 'zh', 1, {
            'spd': 3,
            'vol': 5,
            'per': 4,
        })
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('auido.mp3', 'wb') as f:
                f.write(result)



if __name__ == '__main__':
    speech = Speech()
    # get_file_content('test.txt')
    content = speech.get_file_content('test.txt')
    speech.get_result(content)