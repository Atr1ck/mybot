from bs4 import BeautifulSoup
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import re

character_map = {
    "星乃 一歌":["ln","ick",1],
    "天马 咲希":["ln","saki",2],
    "望月 穂波":["ln","hnm",3],
    "日野森 志歩":["ln","shino",4],
    "花里 实乃里":["mmj","mnr",5],
    "桐谷 遥":["mmj","hrk",6],
    "桃井 爱莉":["mmj","airi",7],
    "日野森 雫":["mmj","szk",8],
    "小豆泽 心羽":["vbs","khn",9],
    "白石 杏":["vbs","an",10],
    "东云 彰人":["vbs","akt",11],
    "青柳 冬弥":["vbs","toya",12],
    "天马 司":["ws","tks",13],
    "凤 笑梦":["ws","emu",14],
    "草薙 宁宁":["ws","nene",15],
    "神代 类":["ws","rui",16],
    "宵崎 奏":["25h","knd",17],
    "朝比奈 真冬":["25h","mfy",18],
    "东云 绘名":["25h","ena",19],
    "晓山 瑞希":["25h","mzk",20],
    "初音 未来":["vs","miku",21],
    "镜音 铃":["vs","rin",22],
    "镜音 连":["vs","ren",23],
    "巡音 流歌":["vs","ruka",24],
    "MEIKO":["vs","meiko",25],
    "KAITO":["vs","kaito",26]
}

print(character_map["望月 穗波"])
print(character_map[""])