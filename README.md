# yomao
---
yomao is a line bot that retrieve and post a popular image from [pixiv](http://www.pixiv.net/) by a keyword that user provide.

yomoa is powered by [Line bot trial API](https://business.line.me/services/products/4/introduction).

### How to add it for fun!
---
![qr](https://qr-official.line.me/sid/L/vay5690f.png)

### Building Dependency
---
* [Python](https://www.python.org/) >= 3
* [requests](http://docs.python-requests.org/en/master/)
* [pixivpy](https://github.com/upbit/pixivpy)
* [flask](http://flask.pocoo.org/)

You can simply install the libraries using pip:
```
$ pip install -r requirements.txt
```

### Special Requirement
---
* If you have a special network environment, just modify the `requests_kwargs` in `linebot_yomao.conf_sample`. It will be passed to the package `requests` for your special network environment.

### Feature
---
* Reply a popular image that queried from pixiv randomly.
* The format is as followed.
```
/yomao keyword_A kwyword_B ...
```
* After key in, it will take about 7~10 secs for retrieving image.
 

![Demo_cat](http://i.imgur.com/0GZKD3e.png "Demo_pikachu")

### Author
---
Sean Chen <genius091612@gmail.com>

### License
---
GPLv3 or later