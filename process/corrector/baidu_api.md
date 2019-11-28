| 应用名称 | AppID | API Key | Secret Key |
| -------- | ----- | ------- | ---------- |
| corrector | 17829438 | 8afgFdfrlNVSaRMFqSqNUKt0 | 8XWhg3BsPe4CiquRF5m6ijOfENpIkH1h |

[SDK文档](https://ai.baidu.com/docs#/NLP-Python-SDK/top)
```bash
pip install baidu-aip
```

```python
from aip import AipNlp
app_id      =   '17829438'
api_key     =   '8afgFdfrlNVSaRMFqSqNUKt0'
secret_key  =   '8XWhg3BsPe4CiquRF5m6ijOfENpIkH1h'

client = AipNlp(app_id, api_key, secret_key)

responses = []
text_list = ['形像代言人',
            '此事不会影像中国关系大局',
            '化夏子孙团结一心',
            '就难免必理不平衡。',
            '西藏叛乱的失败，使尼赫鲁“大印度联邦”的构想华为泡影。',
            '看看人家，不给钱就酸了，因为你缺的那个敬业福。',
            '甚至龙族的秘密歪斜也没有关系。',
            '我们会优先推动五大创新研发计画。',
            '说自己市提前两天排对的。',
            '等啊等，忠于等到了。',
            '还有进口香皂、家居服、花艺样样聚全。',
            '“蒙汉药!”加尼马尔恍然大悟，他费了九牛二虎之力，终于把他的助手弄醒。',
            '好象是我们错了。',
            '人群中发出一阵惊吁声。',
            '清河安宁庄西二条路人形步道翻修！',
            '看来生活中也是蛮回撒娇的呢。',
            '还可能与这个小村落与比斯特购物村想去不远也不无关系。']

print(len(text_list))

for text in text_list:
    print(client.ecnet(text))
```

