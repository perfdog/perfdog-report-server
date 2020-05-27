#! /usr/bin/python
# coding: utf-8

from flask import Flask, request, jsonify

import report

app = Flask(__name__)


@app.route('/report', methods=['POST'])
def create_report():
    report_id = None
    keys = list(request.form.keys())
    if 'pb' in keys:
        report_id = report.create_by_pb(request.form['pb'])
    elif 'json' in keys:
        report_id = report.create_by_json(request.form['json'])

    if report_id is None:
        res = {'errCode': -1, 'errStr': 'invalid arguments'}
    else:
        res = {'errCode': 0, 'errStr': 'success', 'reportId': '1dc791c3-ce2b-49e1-badf-a5c785a9a3db'}

    return jsonify(res)


@app.route('/report/icon', methods=['PUT'])
def set_icon():
    report_id = request.form['reportId']
    value = request.form['icon']
    report.set_icon(report_id, value)
    return jsonify({'errCode': 0, 'errStr': 'success'})


@app.route('/report/screenshots', methods=['POST'])
def add_screenshots():
    report_id = request.form['reportId']
    screenshots = []
    for key in request.form.keys():
        if key == 'reportId':
            continue
        screenshot = (key, request.form[key])
        screenshot.append(screenshot)

    report.add_screenshots(report_id, screenshots)
    return jsonify({'errCode': 0, 'errStr': 'success'})


@app.route('/report/done', methods=['PUT'])
def done():
    report_id = request.form['reportId']
    report.done(report_id)
    return jsonify({'errCode': 0, 'errStr': 'success'})
