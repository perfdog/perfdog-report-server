# coding: utf-8

import os
import uuid


class Report(object):
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def set_data_by_pb(self, value):
        pass

    def set_data_by_json(self, value):
        pass

    def set_icon(self, value):
        pass

    def add_screenshots(self, screenshots):
        pass

    def done(self):
        pass


class ReportManager(object):
    def __init__(self):
        self.base_dir = os.path.split(os.path.realpath(__file__))[0] + os.sep + 'data'
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)

    def create_report(self):
        report_id = str(uuid.uuid4())
        report_dir = self.get_report_dir(report_id)
        os.mkdir(report_dir)
        return report_id, Report(report_dir)

    def get_report(self, report_id):
        report_dir = self.get_report_dir(report_id)
        return Report(report_dir)

    def get_report_dir(self, report_id):
        return '%s%s%s' % (self.base_dir, os.sep, report_id)


reportManager = ReportManager()


def create_by_json(value):
    (report_id, report) = reportManager.create_report()
    report.set_data_by_json(value)
    return report_id


def create_by_pb(value):
    (report_id, report) = reportManager.create_report()
    report.set_data_by_pb(value)
    return report_id


def set_icon(report_id, value):
    report = reportManager.get_report(report_id)
    report.set_icon(value)


def add_screenshots(report_id, screenshots):
    report = reportManager.get_report(report_id)
    report.add_screenshots(screenshots)


def done(report_id):
    report = reportManager.get_report(report_id)
    report.done()
