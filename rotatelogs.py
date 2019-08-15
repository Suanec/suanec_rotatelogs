# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2019/8/14.
# git: https://github.com/Suanec
# repo: https://github.com/Suanec/suanec_rotatelogs.git

# ===========================================================================
# I DO NOT KNOW THE DIFFERENCE FROM EVERY LICENSE OF OPEN SOURCE CODE YET
# NOW JUST COPY SPARK'S LICENSE TO HERE 
# I PLAN TO LEARN ABOUT POPULAR LICENSE TO KNOW THE DIFFERENCE BETWEEN THEM.
# ===========================================================================




#                                  Apache License
#                            Version 2.0, January 2004
#                         http://www.apache.org/licenses/

#    TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

#    1. Definitions.

#       "License" shall mean the terms and conditions for use, reproduction,
#       and distribution as defined by Sections 1 through 9 of this document.

#       "Licensor" shall mean the copyright owner or entity authorized by
#       the copyright owner that is granting the License.

#       "Legal Entity" shall mean the union of the acting entity and all
#       other entities that control, are controlled by, or are under common
#       control with that entity. For the purposes of this definition,
#       "control" means (i) the power, direct or indirect, to cause the
#       direction or management of such entity, whether by contract or
#       otherwise, or (ii) ownership of fifty percent (50%) or more of the
#       outstanding shares, or (iii) beneficial ownership of such entity.

#       "You" (or "Your") shall mean an individual or Legal Entity
#       exercising permissions granted by this License.

#       "Source" form shall mean the preferred form for making modifications,
#       including but not limited to software source code, documentation
#       source, and configuration files.

#       "Object" form shall mean any form resulting from mechanical
#       transformation or translation of a Source form, including but
#       not limited to compiled object code, generated documentation,
#       and conversions to other media types.

#       "Work" shall mean the work of authorship, whether in Source or
#       Object form, made available under the License, as indicated by a
#       copyright notice that is included in or attached to the work
#       (an example is provided in the Appendix below).

#       "Derivative Works" shall mean any work, whether in Source or Object
#       form, that is based on (or derived from) the Work and for which the
#       editorial revisions, annotations, elaborations, or other modifications
#       represent, as a whole, an original work of authorship. For the purposes
#       of this License, Derivative Works shall not include works that remain
#       separable from, or merely link (or bind by name) to the interfaces of,
#       the Work and Derivative Works thereof.

#       "Contribution" shall mean any work of authorship, including
#       the original version of the Work and any modifications or additions
#       to that Work or Derivative Works thereof, that is intentionally
#       submitted to Licensor for inclusion in the Work by the copyright owner
#       or by an individual or Legal Entity authorized to submit on behalf of
#       the copyright owner. For the purposes of this definition, "submitted"
#       means any form of electronic, verbal, or written communication sent
#       to the Licensor or its representatives, including but not limited to
#       communication on electronic mailing lists, source code control systems,
#       and issue tracking systems that are managed by, or on behalf of, the
#       Licensor for the purpose of discussing and improving the Work, but
#       excluding communication that is conspicuously marked or otherwise
#       designated in writing by the copyright owner as "Not a Contribution."

#       "Contributor" shall mean Licensor and any individual or Legal Entity
#       on behalf of whom a Contribution has been received by Licensor and
#       subsequently incorporated within the Work.

#    2. Grant of Copyright License. Subject to the terms and conditions of
#       this License, each Contributor hereby grants to You a perpetual,
#       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
#       copyright license to reproduce, prepare Derivative Works of,
#       publicly display, publicly perform, sublicense, and distribute the
#       Work and such Derivative Works in Source or Object form.

#    3. Grant of Patent License. Subject to the terms and conditions of
#       this License, each Contributor hereby grants to You a perpetual,
#       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
#       (except as stated in this section) patent license to make, have made,
#       use, offer to sell, sell, import, and otherwise transfer the Work,
#       where such license applies only to those patent claims licensable
#       by such Contributor that are necessarily infringed by their
#       Contribution(s) alone or by combination of their Contribution(s)
#       with the Work to which such Contribution(s) was submitted. If You
#       institute patent litigation against any entity (including a
#       cross-claim or counterclaim in a lawsuit) alleging that the Work
#       or a Contribution incorporated within the Work constitutes direct
#       or contributory patent infringement, then any patent licenses
#       granted to You under this License for that Work shall terminate
#       as of the date such litigation is filed.

#    4. Redistribution. You may reproduce and distribute copies of the
#       Work or Derivative Works thereof in any medium, with or without
#       modifications, and in Source or Object form, provided that You
#       meet the following conditions:

#       (a) You must give any other recipients of the Work or
#           Derivative Works a copy of this License; and

#       (b) You must cause any modified files to carry prominent notices
#           stating that You changed the files; and

#       (c) You must retain, in the Source form of any Derivative Works
#           that You distribute, all copyright, patent, trademark, and
#           attribution notices from the Source form of the Work,
#           excluding those notices that do not pertain to any part of
#           the Derivative Works; and

#       (d) If the Work includes a "NOTICE" text file as part of its
#           distribution, then any Derivative Works that You distribute must
#           include a readable copy of the attribution notices contained
#           within such NOTICE file, excluding those notices that do not
#           pertain to any part of the Derivative Works, in at least one
#           of the following places: within a NOTICE text file distributed
#           as part of the Derivative Works; within the Source form or
#           documentation, if provided along with the Derivative Works; or,
#           within a display generated by the Derivative Works, if and
#           wherever such third-party notices normally appear. The contents
#           of the NOTICE file are for informational purposes only and
#           do not modify the License. You may add Your own attribution
#           notices within Derivative Works that You distribute, alongside
#           or as an addendum to the NOTICE text from the Work, provided
#           that such additional attribution notices cannot be construed
#           as modifying the License.

#       You may add Your own copyright statement to Your modifications and
#       may provide additional or different license terms and conditions
#       for use, reproduction, or distribution of Your modifications, or
#       for any such Derivative Works as a whole, provided Your use,
#       reproduction, and distribution of the Work otherwise complies with
#       the conditions stated in this License.

#    5. Submission of Contributions. Unless You explicitly state otherwise,
#       any Contribution intentionally submitted for inclusion in the Work
#       by You to the Licensor shall be under the terms and conditions of
#       this License, without any additional terms or conditions.
#       Notwithstanding the above, nothing herein shall supersede or modify
#       the terms of any separate license agreement you may have executed
#       with Licensor regarding such Contributions.

#    6. Trademarks. This License does not grant permission to use the trade
#       names, trademarks, service marks, or product names of the Licensor,
#       except as required for reasonable and customary use in describing the
#       origin of the Work and reproducing the content of the NOTICE file.

#    7. Disclaimer of Warranty. Unless required by applicable law or
#       agreed to in writing, Licensor provides the Work (and each
#       Contributor provides its Contributions) on an "AS IS" BASIS,
#       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#       implied, including, without limitation, any warranties or conditions
#       of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
#       PARTICULAR PURPOSE. You are solely responsible for determining the
#       appropriateness of using or redistributing the Work and assume any
#       risks associated with Your exercise of permissions under this License.

#    8. Limitation of Liability. In no event and under no legal theory,
#       whether in tort (including negligence), contract, or otherwise,
#       unless required by applicable law (such as deliberate and grossly
#       negligent acts) or agreed to in writing, shall any Contributor be
#       liable to You for damages, including any direct, indirect, special,
#       incidental, or consequential damages of any character arising as a
#       result of this License or out of the use or inability to use the
#       Work (including but not limited to damages for loss of goodwill,
#       work stoppage, computer failure or malfunction, or any and all
#       other commercial damages or losses), even if such Contributor
#       has been advised of the possibility of such damages.

#    9. Accepting Warranty or Additional Liability. While redistributing
#       the Work or Derivative Works thereof, You may choose to offer,
#       and charge a fee for, acceptance of support, warranty, indemnity,
#       or other liability obligations and/or rights consistent with this
#       License. However, in accepting such obligations, You may act only
#       on Your own behalf and on Your sole responsibility, not on behalf
#       of any other Contributor, and only if You agree to indemnify,
#       defend, and hold each Contributor harmless for any liability
#       incurred by, or claims asserted against, such Contributor by reason
#       of your accepting any such warranty or additional liability.

#    END OF TERMS AND CONDITIONS

#    APPENDIX: How to apply the Apache License to your work.

#       To apply the Apache License to your work, attach the following
#       boilerplate notice, with the fields enclosed by brackets "[]"
#       replaced with your own identifying information. (Don't include
#       the brackets!)  The text should be enclosed in the appropriate
#       comment syntax for the file format. We also recommend that a
#       file or class name and description of purpose be included on the
#       same "printed page" as the copyright notice for easier
#       identification within third-party archives.

#    Copyright [yyyy] [name of copyright owner]

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


# =======================================================================
# Apache Spark Subcomponents:

# The Apache Spark project contains subcomponents with separate copyright
# notices and license terms. Your use of the source code for the these
# subcomponents is subject to the terms and conditions of the following
# licenses.


# ========================================================================
# For heapq (pyspark/heapq3.py):
# ========================================================================

# See license/LICENSE-heapq.txt

# ========================================================================
# For SnapTree:
# ========================================================================

# See license/LICENSE-SnapTree.txt

# ========================================================================
# For jbcrypt:
# ========================================================================

# See license/LICENSE-jbcrypt.txt

# ========================================================================
# BSD-style licenses
# ========================================================================

# The following components are provided under a BSD-style license. See project link for details.
# The text of each license is also included at licenses/LICENSE-[project].txt.

#      (BSD 3 Clause) netlib core (com.github.fommil.netlib:core:1.1.2 - https://github.com/fommil/netlib-java/core)
#      (BSD 3 Clause) JPMML-Model (org.jpmml:pmml-model:1.2.7 - https://github.com/jpmml/jpmml-model)
#      (BSD License) AntLR Parser Generator (antlr:antlr:2.7.7 - http://www.antlr.org/)
#      (BSD License) ANTLR 4.5.2-1 (org.antlr:antlr4:4.5.2-1 - http://wwww.antlr.org/)
#      (BSD licence) ANTLR ST4 4.0.4 (org.antlr:ST4:4.0.4 - http://www.stringtemplate.org)
#      (BSD licence) ANTLR StringTemplate (org.antlr:stringtemplate:3.2.1 - http://www.stringtemplate.org)
#      (BSD License) Javolution (javolution:javolution:5.5.1 - http://javolution.org)
#      (BSD) JLine (jline:jline:0.9.94 - http://jline.sourceforge.net)
#      (BSD) ParaNamer Core (com.thoughtworks.paranamer:paranamer:2.3 - http://paranamer.codehaus.org/paranamer)
#      (BSD) ParaNamer Core (com.thoughtworks.paranamer:paranamer:2.6 - http://paranamer.codehaus.org/paranamer)
#      (BSD 3 Clause) Scala (http://www.scala-lang.org/download/#License)
#         (Interpreter classes (all .scala files in repl/src/main/scala
#         except for Main.Scala, SparkHelper.scala and ExecutorClassLoader.scala),
#         and for SerializableMapWrapper in JavaUtils.scala)
#      (BSD-like) Scala Actors library (org.scala-lang:scala-actors:2.11.8 - http://www.scala-lang.org/)
#      (BSD-like) Scala Compiler (org.scala-lang:scala-compiler:2.11.8 - http://www.scala-lang.org/)
#      (BSD-like) Scala Compiler (org.scala-lang:scala-reflect:2.11.8 - http://www.scala-lang.org/)
#      (BSD-like) Scala Library (org.scala-lang:scala-library:2.11.8 - http://www.scala-lang.org/)
#      (BSD-like) Scalap (org.scala-lang:scalap:2.11.8 - http://www.scala-lang.org/)
#      (BSD-style) scalacheck (org.scalacheck:scalacheck_2.11:1.10.0 - http://www.scalacheck.org)
#      (BSD-style) spire (org.spire-math:spire_2.11:0.7.1 - http://spire-math.org)
#      (BSD-style) spire-macros (org.spire-math:spire-macros_2.11:0.7.1 - http://spire-math.org)
#      (New BSD License) Kryo (com.esotericsoftware:kryo:3.0.3 - https://github.com/EsotericSoftware/kryo)
#      (New BSD License) MinLog (com.esotericsoftware:minlog:1.3.0 - https://github.com/EsotericSoftware/minlog)
#      (New BSD license) Protocol Buffer Java API (com.google.protobuf:protobuf-java:2.5.0 - http://code.google.com/p/protobuf)
#      (New BSD license) Protocol Buffer Java API (org.spark-project.protobuf:protobuf-java:2.4.1-shaded - http://code.google.com/p/protobuf)
#      (The BSD License) Fortran to Java ARPACK (net.sourceforge.f2j:arpack_combined_all:0.1 - http://f2j.sourceforge.net)
#      (The BSD License) xmlenc Library (xmlenc:xmlenc:0.52 - http://xmlenc.sourceforge.net)
#      (The New BSD License) Py4J (net.sf.py4j:py4j:0.10.6 - http://py4j.sourceforge.net/)
#      (Two-clause BSD-style license) JUnit-Interface (com.novocode:junit-interface:0.10 - http://github.com/szeiger/junit-interface/)
#      (BSD licence) sbt and sbt-launch-lib.bash
#      (BSD 3 Clause) d3.min.js (https://github.com/mbostock/d3/blob/master/LICENSE)
#      (BSD 3 Clause) DPark (https://github.com/douban/dpark/blob/master/LICENSE)
#      (BSD 3 Clause) CloudPickle (https://github.com/cloudpipe/cloudpickle/blob/master/LICENSE)

# ========================================================================
# MIT licenses
# ========================================================================

# The following components are provided under the MIT License. See project link for details.
# The text of each license is also included at licenses/LICENSE-[project].txt.

#      (MIT License) JCL 1.1.1 implemented over SLF4J (org.slf4j:jcl-over-slf4j:1.7.5 - http://www.slf4j.org)
#      (MIT License) JUL to SLF4J bridge (org.slf4j:jul-to-slf4j:1.7.5 - http://www.slf4j.org)
#      (MIT License) SLF4J API Module (org.slf4j:slf4j-api:1.7.5 - http://www.slf4j.org)
#      (MIT License) SLF4J LOG4J-12 Binding (org.slf4j:slf4j-log4j12:1.7.5 - http://www.slf4j.org)
#      (MIT License) pyrolite (org.spark-project:pyrolite:2.0.1 - http://pythonhosted.org/Pyro4/)
#      (MIT License) scopt (com.github.scopt:scopt_2.11:3.2.0 - https://github.com/scopt/scopt)
#      (The MIT License) Mockito (org.mockito:mockito-core:1.9.5 - http://www.mockito.org)
#      (MIT License) jquery (https://jquery.org/license/)
#      (MIT License) AnchorJS (https://github.com/bryanbraun/anchorjs)
#      (MIT License) graphlib-dot (https://github.com/cpettitt/graphlib-dot)
#      (MIT License) dagre-d3 (https://github.com/cpettitt/dagre-d3)
#      (MIT License) sorttable (https://github.com/stuartlangridge/sorttable)
#      (MIT License) boto (https://github.com/boto/boto/blob/develop/LICENSE)
#      (MIT License) datatables (http://datatables.net/license)
#      (MIT License) mustache (https://github.com/mustache/mustache/blob/master/LICENSE)
#      (MIT License) cookies (http://code.google.com/p/cookies/wiki/License)
#      (MIT License) blockUI (http://jquery.malsup.com/block/)
#      (MIT License) RowsGroup (http://datatables.net/license/mit)
#      (MIT License) jsonFormatter (http://www.jqueryscript.net/other/jQuery-Plugin-For-Pretty-JSON-Formatting-jsonFormatter.html)
#      (MIT License) modernizr (https://github.com/Modernizr/Modernizr/blob/master/LICENSE)
#      (MIT License) machinist (https://github.com/typelevel/machinist)

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
