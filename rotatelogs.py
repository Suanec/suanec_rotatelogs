# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2019/8/14.
# git: https://github.com/Suanec
# repo: https://github.com/Suanec/suanec_rotatelogs.git
import argparse,sys
import os

# target cmd : ./rotatelogs -n 5 ./weiflow-from-weiclient.log 100M
# target_support : Usage: ../rotatelogs [-v] [-l] [-L linkname] [-p prog] [-f] [-t] [-e] [-c] [-n number] <logfile> {<rotation time in seconds>|<rotation size>(B|K|M|G)} [offset minutes from UTC]

OPEN_ERROR = 211
WRITE_ERROR = 212
FILERENAME_ERROR = 213
FILEREMOVE_ERROR = 214
ACCESS_ERROR = 215

class SizeMetric(object):
    def __init__(self, _rotate_size):
        self._rotate_size_str = _rotate_size
        self.ROTATION_SIZE_UNIT = {
            "B" : 1,
            "K" : 1024,
            "M" : 1024 ** 2,
            "G" : 1024 ** 3
        }
        self.ROTATION_SIZE_METRIC = self.ROTATION_SIZE_UNIT.keys()
        self.size_metric_convert()

    def size_metric_convert(self):
        self.rotation_metric = self._rotate_size_str[-1].upper()
        self.rotation_size = int(self._rotate_size_str) if(self.rotation_metric.isdigit()) else int(self._rotate_size_str[:-1])
        if(self.rotation_metric in self.ROTATION_SIZE_METRIC):
            self.rotation_size = int(self._rotate_size_str[:-1]) * self.ROTATION_SIZE_UNIT[self.rotation_metric]
        return self.rotation_size

    @property
    def rotate_size(self):
        return self.rotation_size

class RotateLogFileManager(SizeMetric):
    def __init__(self, _rotate_size, _log_file):
        super(RotateLogFileManager, self).__init__(_rotate_size= _rotate_size)
        self.log_file = _log_file
        try:
            self.file_abs_dir = os.path.realpath(os.path.dirname(self.log_file))
        except Exception,e:
            exit(ACCESS_ERROR)

    def file_name_generator(self, _suffix):
        if(not _suffix):
            return self.log_file
        else:
            return self.log_file + "." + str(_suffix)

class FileNumberLimit(RotateLogFileManager):
    def __init__(self, _num_file, _rotate_size, _log_file):
        super(FileNumberLimit, self).__init__(_rotate_size=_rotate_size, _log_file=_log_file)
        self.num_file = int(_num_file)
        self.max_fsuffix = self.num_file -1
        self.file_list = [self.file_name_generator(i) for i in xrange(1,self.num_file)]
        self.fsuffix_need_to_write = None

    def fsuffix_detected(self):
        fsuffix_not_exist = [_fsuffix for _fsuffix in xrange(1,self.num_file) if not os.path.exists(self.file_name_generator(_fsuffix))]
        if(len(fsuffix_not_exist) == self.max_fsuffix):
            self.fsuffix_need_to_write = None
            return self.fsuffix_need_to_write
        self.fsuffix_need_to_write = (self.max_fsuffix) if(len(fsuffix_not_exist) < 1) else min(fsuffix_not_exist)
        return self.fsuffix_need_to_write

    def file_rotate(self):
        self.fsuffix_detected()
        try:
            if(self.fsuffix_need_to_write == self.max_fsuffix):
                if(os.path.exists(self.file_name_generator(self.max_fsuffix))):
                    os.remove(self.file_name_generator(self.max_fsuffix))
        except Exception,e:
            sys.exit(FILEREMOVE_ERROR)
        try:
            if(self.fsuffix_need_to_write):
                for suffix in xrange(self.fsuffix_need_to_write, 1, -1):
                    os.rename(self.file_name_generator(suffix -1), self.file_name_generator(suffix))
            os.rename(self.log_file, self.file_name_generator(1))
        except Exception,e:
            sys.exit(FILERENAME_ERROR)

class RotateLogWriter(FileNumberLimit):
    def __init__(self, _num_file, _rotate_size, _log_file):
        super(RotateLogWriter, self).__init__(_num_file=_num_file, _rotate_size=_rotate_size, _log_file=_log_file)
        try:
            if(os.path.exists(self.log_file)):
                self.log_writer = open(self.log_file, "r")
                self.writted_size = len(self.log_writer.read())
                self.log_writer.close()
            else:
                self.writted_size = 0
            self.log_writer = open(self.log_file, "ab+")
        except Exception,e:
            sys.exit(OPEN_ERROR)

    def write(self, _msg = ''):
        msg_size = len(_msg)
        try:
            self.log_writer.write(_msg)
            self.writted_size += msg_size
            if(self.writted_size >= self.rotate_size):
                self.log_writer.flush()
                self.log_writer.close()
                self.file_rotate()
                self.log_writer = open(self.log_file, "ab+")
                self.writted_size = 0
        except Exception,e:
            print e.message
            sys.exit(WRITE_ERROR)




if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Run a test HTTPS server. '
                    'By default, the current directory is served.')
    parser.add_argument('-n', '--number-of-files', dest='file_number', type=int, default=2,
                        help='Use a circular list of filenames without timestamps. With -n 3, the series of log files opened would be "logfile", "logfile.1", "logfile.2", then overwriting "logfile". (default: %(default)s)')
    parser.add_argument("log_file", type=str, default='weiflow-from-weiclient.log',
                        help="The path plus basename of the logfile. If logfile includes any '%' characters, it is treated as a format string for strftime(3). Otherwise, the suffix .nnnnnnnnnn is automatically added and is the time in seconds (unless the -t option is used). Both formats compute the start time from the beginning of the current period. For example, if a rotation time of 86400 is specified, the hour, minute, and second fields created from the strftime(3) format will all be zero, referring to the beginning of the current 24-hour period (midnight).")
    parser.add_argument("rotation_size", type=str, default='500M',
                        help="The path plus basename of the logfile. If logfile includes any '%' characters, it is treated as a format string for strftime(3). Otherwise, the suffix .nnnnnnnnnn is automatically added and is the time in seconds (unless the -t option is used). Both formats compute the start time from the beginning of the current period. For example, if a rotation time of 86400 is specified, the hour, minute, and second fields created from the strftime(3) format will all be zero, referring to the beginning of the current 24-hour period (midnight).")
    args = parser.parse_args()
    print args
    rotation_size = SizeMetric(args.rotation_size).rotate_size
    print rotation_size
    rotator = RotateLogWriter(args.file_number, args.rotation_size, args.log_file)
    for line in sys.stdin:
        rotator.write(line)
    # for line in xrange(1,100000):
    #     rotator.write('%s %s %s %s %s %s %s %s %s %s %s ' % (line, line, line, line, line, line, line, line, line, line, line))


