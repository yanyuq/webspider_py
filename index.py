# coding=utf-8
import requests
from flask import Flask, request, jsonify
from flask import render_template

from com.yqb.webspider.elasticsearch_test import index_sina, index_zhihu, index_synthesize

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sina')
def sina():
    page_from = request.args.get('offset', int)
    page_size = request.args.get('limit', int)
    index_name = request.args.get('indexName', str)
    search_key = request.args.get('search', str)

    sina_data = index_sina(search_key, index_name, page_from, page_size)
    if sina_data['total'] > 10000:
        total = 10000
    else:
        total = sina_data['total']
    rows = sina_data['hits']
    return jsonify(total=total, rows=rows)


@app.route('/zhihu')
def zhihu():
    page_from = request.args.get('offset', int)
    page_size = request.args.get('limit', int)
    index_name = request.args.get('indexName', str)
    search_key = request.args.get('search', str)

    zhihu_data = index_zhihu(search_key, index_name, page_from, page_size)
    if zhihu_data['total'] > 10000:
        total = 10000
    else:
        total = zhihu_data['total']
    rows = zhihu_data['hits']
    return jsonify(total=total, rows=rows)


@app.route('/synthesize')
def synthesize():
    page_from = request.args.get('offset', int)
    page_size = request.args.get('limit', int)
    index_name = request.args.get('indexName', str)
    search_key = request.args.get('search', str)

    synthesize_data = index_synthesize(search_key, index_name, page_from, page_size)
    if synthesize_data['total'] > 10000:
        total = 10000
    else:
        total = synthesize_data['total']
    rows = synthesize_data['hits']
    return jsonify(total=total, rows=rows)


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/req')
def req():
    a = request.args.getlist('a', str)
    b = request.args.getlist('b', str)
    return jsonify(result=a + b)


@app.route('/req/<a>/<b>')
def req1(a, b):
    return jsonify(result=a + b)


@app.route('/count')
def count():
    zhihu_url = 'http://192.168.31.172:8080/zhihu/count'
    response = requests.get(zhihu_url)
    return jsonify(result=response.text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
