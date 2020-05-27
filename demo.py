#! /usr/bin/python
# coding: utf-8

from flask import Flask, request, jsonify

import report

app = Flask(__name__)


@app.route('/report', methods=['POST'])
def create_report():
    file_format = request.form['file_format']
    if file_format == 'pb':
        report_id = report.create_by_pb(request.files['data'])
    elif file_format == 'json':
        report_id = report.create_by_json(request.files['data'])

    if report_id is None:
        res = {'errCode': -1, 'errStr': 'invalid arguments'}
    else:
        res = {'errCode': 0, 'errStr': 'success', 'reportId': report_id}

    return jsonify(res)


@app.route('/report/icon', methods=['PUT'])
def set_icon():
    report_id = request.form['reportId']
    report.set_icon(report_id, request.files['icon'])
    return jsonify({'errCode': 0, 'errStr': 'success'})


@app.route('/report/screenshots', methods=['POST'])
def add_screenshots():
    report_id = request.form['reportId']
    files = []
    for name in request.files:
        files.append(request.files[name])

    report.add_screenshots(report_id, files)
    return jsonify({'errCode': 0, 'errStr': 'success'})


@app.route('/report/done', methods=['PUT'])
def done():
    report_id = request.form['reportId']
    report.done(report_id)
    return jsonify({'errCode': 0, 'errStr': 'success'})
