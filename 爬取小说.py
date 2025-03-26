import os
import re
import textwrap

import requests

url='https://www.qimao.com/shuku/195958-575436/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}
# 指定编码


resp=requests.get(url,headers=headers)
resp.encoding='utf-8'
def extract_phones(text):
    # 创建正则表达式对象
    pattern=re.compile(r'<div class="article" data-v-2358fcd5><p>(.*?)</p></div>')
    return pattern.findall(text)
# 生成一个函数吧文本里”</p><p>“替换掉成""
def replace_p(text):
    return text.replace('</p><p>','')
txt =url.join(extract_phones(resp.text))
txt1 =replace_p(txt)

# 创建函数 自动采集文章的标题
def extract_title(text):
    pattern = r'class="chapter-title"[^>]*>([\u4e00-\u9fa50-9\s]+)</h2>'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        result = match.group(1)  # 提取第一个汉字到 </h2> 之间的部分
        return result
    else:
        print("未找到匹配项")
        return
# 查看目录是否存在
if not os.path.exists(r'D:\\txt'):
    os.mkdir(r'D:\\txt')
name=extract_title(resp.text)

def format_text(text):
    return "\n".join(textwrap.wrap(text, 80))
txt2=format_text(txt1)
with open(rf'D:\\txt\{name}.txt','w',encoding='utf-8') as f:
    f.write(txt2)