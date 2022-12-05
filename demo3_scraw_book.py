# -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup
 
 
'''
# web: https://www.bookresource.net/pdf-1/list-1.html
# pdf-1 ：first type
# list-1  ：first page
# pdf-n/list-n ： #data samples
# 
'''
 
 
url_base='https://www.bookresource.net/'
def getHTMLText(url):
    ## standard frame
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}      
        r = requests.get( url ,  headers = headers )
        r.raise_for_status  # if status!= 200，raise HTTPError  ( or r.status_code HTTP请求的返回状态，200 indicate success，404 wrong )
        r.encoding = r.apparent_encoding # r.apparent_encoding
        return r.text
    except:
        print('Error！')
        return 'Load Page Error!'
    
 
def Parse_To_Data(html):
    b = BeautifulSoup(  html , 'lxml'  )
    
    i=0
    covers_list=[]                                          # 创建存储封面地址的list
    for data in b.select( 'img' ):                      # 查找标签img的元素
        #print (data['src'])                                # 下一步插入list    
        covers_list.insert( i , data['src'] )            # 错误写法 covers_list[i] = data['src']，报错List的索引超出范围
        i=i+1                                                   # next
 
    i=0
    zy_list=[]
    title_list=[]
    auo_list=[]
    press_list=[]
    for data in b.find_all('div',attrs={"class": "list_info"}):         # div节点
        # title
        a = data.a.text.strip( )
        title_list.insert(i,a)
        # author
        temp_press = data.find_all('p')
        b = temp_press[0].text.strip( ).lstrip('author：').strip( )
        auo_list.insert(i,b)
        # editor
        temp_press = data.find_all('p')
        c = temp_press[1].text.strip( ).lstrip('editor：').strip( )
        press_list.insert(i,c)
        # intro
        temp_abs = data.find_all('p')
        d = temp_abs[3].text.strip( ).lstrip('Intro：').strip( )
        zy_list.insert(i,d)
 
        print(title_list[i])
        print(auo_list[i])
        print(press_list[i])
        print(zy_list[i])
        
        i=i+1
        print('\n')
 
    return covers_list,title_list,auo_list,press_list,zy_list

def new_txt():
    file = open('book.txt',mode='w')
    #file.write("id\tbookname\tauthor\n")

def write_to_txt(sort,page,bookname_list,author_list):
    file = open('book.txt',mode='a+')
    for i in  range(0,len(bookname_list)) :
        content = (str(i) + '\t' + bookname_list[i] + '\t' + author_list[i] +'\t' + "NotBorrowed"+"\n")#.encode("utf-8", 'ignore').decode("utf-8", "ignore")
        file.write(content)
    file.close()
 
#
if True:
    new_txt()
    author_list = []
    bookname_list = []
    for sort in range(1, 12, 1):                 
        for page in range(1, 3, 1):
            url = url_base + 'pdf-' + str(sort) + '/list-'  + str(page) + '.html'
            print (  '\nScrawing'+'%dth'% (sort)+'，%dth page：' % (page)+url+'\n')
            html=getHTMLText(  url  )
            (a,b,c,d,e)= Parse_To_Data( html )
            for item in b:
                bookname_list.append(item)
            for item in c:
                author_list.append(item)
    write_to_txt(sort,page,bookname_list,author_list)
