# suanec_rotatelogs
# rotatelogs
```text
isometric3

      ___           ___                       ___                       ___                         ___           ___           ___
     /  /\         /  /\          ___        /  /\          ___        /  /\                       /  /\         /  /\         /  /\
    /  /::\       /  /::\        /  /\      /  /::\        /  /\      /  /:/_                     /  /::\       /  /:/_       /  /:/_
   /  /:/\:\     /  /:/\:\      /  /:/     /  /:/\:\      /  /:/     /  /:/ /\    ___     ___    /  /:/\:\     /  /:/ /\     /  /:/ /\
  /  /:/~/:/    /  /:/  \:\    /  /:/     /  /:/~/::\    /  /:/     /  /:/ /:/_  /__/\   /  /\  /  /:/  \:\   /  /:/_/::\   /  /:/ /::\
 /__/:/ /:/___ /__/:/ \__\:\  /  /::\    /__/:/ /:/\:\  /  /::\    /__/:/ /:/ /\ \  \:\ /  /:/ /__/:/ \__\:\ /__/:/__\/\:\ /__/:/ /:/\:\
 \  \:\/:::::/ \  \:\ /  /:/ /__/:/\:\   \  \:\/:/__\/ /__/:/\:\   \  \:\/:/ /:/  \  \:\  /:/  \  \:\ /  /:/ \  \:\ /~~/:/ \  \:\/:/~/:/
  \  \::/~~~~   \  \:\  /:/  \__\/  \:\   \  \::/      \__\/  \:\   \  \::/ /:/    \  \:\/:/    \  \:\  /:/   \  \:\  /:/   \  \::/ /:/
   \  \:\        \  \:\/:/        \  \:\   \  \:\           \  \:\   \  \:\/:/      \  \::/      \  \:\/:/     \  \:\/:/     \__\/ /:/
    \  \:\        \  \::/          \__\/    \  \:\           \__\/    \  \::/        \__\/        \  \::/       \  \::/        /__/:/
     \__\/         \__\/                     \__\/                     \__\/                       \__\/         \__\/         \__\/

```
```text
slant
    ____  ____  _________  ______________    ____  ___________
   / __ \/ __ \/_  __/   |/_  __/ ____/ /   / __ \/ ____/ ___/
  / /_/ / / / / / / / /| | / / / __/ / /   / / / / / __ \__ \
 / _, _/ /_/ / / / / ___ |/ / / /___/ /___/ /_/ / /_/ /___/ /
/_/ |_|\____/ /_/ /_/  |_/_/ /_____/_____/\____/\____//____/


```
```text
standard
  ____   ___ _____  _  _____ _____ _     ___   ____ ____
 |  _ \ / _ \_   _|/ \|_   _| ____| |   / _ \ / ___/ ___|
 | |_) | | | || | / _ \ | | |  _| | |  | | | | |  _\___ \
 |  _ <| |_| || |/ ___ \| | | |___| |__| |_| | |_| |___) |
 |_| \_\\___/ |_/_/   \_\_| |_____|_____\___/ \____|____/


```

##### instruction 
A simple rotatelog tool.
there is a lots of log rotator tools for limit log file size.
this is a simple implementations for Apache httpd rotatelogs.
with a differences is work in yarn namenode log mode.
that's means the oldest log was in the largest suffix file with $USER_LOG_FILE always fresh.

##### main points
- support Linux pipe operation.
- support file size limitation.
- support file number limitation.
- maintain all log file in ordered with the latest log in $USER_LOG_FILE and oldest log in the largest suffix file.
- a few faster than Apache rotatelogs. speed performance was not considered well.
- few memory cost.
- simple usage
- clean dependencies by implementations in naive Python 2.7
- light tools for log file maintaining.
- easy code for redevelopment and bug location.
- free use for anyone.


##### requirement 
python 2.7.x

##### reference 
https://httpd.apache.org/docs/2.4/programs/rotatelogs.html

##### usage
```
  chmod +x ${CUSTOM_PATH}/rotatelogs.py 
  $commandLine | ./rotatelogs.py -n 5 /data0/suanec/control_center/weibox/rotate_logs/weiflow-from-weiclient.log 100M
```

##### test command
```
set -efx

IDX=20
START_DATE=`date +"%s"`
rm -f ./weiflow-from-weiclient.log*
for i in `seq 1 $IDX`
do
  echo $i
  # hive -e "select * from online_data_record_per_hour_new_tag where dt=20190801 and hour=18" 2> ./weiflow-from-weiclient.log | head -n 30000 >> /data0/suanec/control_center/weibox/rotate_logs/weiflow-from-weiclient.log
  # hive -e "select * from online_data_record_per_hour_new_tag where dt=20190801 and hour=18" 2> ./weiflow-from-weiclient.log 1> /data0/suanec/control_center/weibox/rotate_logs/weiflow-from-weiclient.log
  # hive -e "select * from online_data_record_per_hour_new_tag where dt=20190801 and hour=18" 2> ./weiflow-from-weiclient.log | tail -n 30000 >> /data0/suanec/control_center/weibox/rotate_logs/weiflow-from-weiclient.log
  # hive -e "select * from online_data_record_per_hour_new_tag where dt=20190801 and hour=18" 2> ./weiflow-from-weiclient.log | /data0/suanec/control_center/weibox/rotate_logs/../rotatelogs -n 3 /data0/suanec/control_center/weibox/rotate_logs/weiflow-from-weiclient.log 500M
  # hive -e "select * from online_data_record_per_hour_new_tag where dt=20190801 and hour=18" 2> ./weiflow-from-weiclient.log | python ./rotatelogs.py -n 5 /data0/suanec/control_center/weibox/rotate_logs/weiflow-from-weiclient.log 100M
  # hive -e "select * from online_data_record_per_hour_new_tag where dt=20190801 and hour=18" 2> ./weiflow-from-weiclient.log | python ./rotatelogs.py -n 3 /data0/suanec/control_center/weibox/rotate_logs/weiflow-from-weiclient.log 500M
  # hive -e "select * from online_data_record_per_hour_new_tag where dt=20190801 and hour=18" 2> ./weiflow-from-weiclient.log | ./rotatelogs.py -n 3 /data0/suanec/control_center/weibox/rotate_logs/weiflow-from-weiclient.log 500M
done
END_DATE=`date +"%s"`
RUN_TIME=$(echo "(${END_DATE}-${START_DATE})/${IDX}" | bc -l )
echo "RUN_TIME : "
echo ${RUN_TIME}

```
##### result size
```
/business/content/datasource/online_data_record_per_hour_new_tag/dt=20190801/hour=18/ori_new_tag.txt
6.1G
```
##### simple result
|command|time-cost|
|-|-|
|head -3w|13s|
|all|136s|
|tail -3w|66s|
|apache rotateLogs -n 3 500M| 102s|
|suanec rotateLogs -n 5 100M| 60s |
|suanec rotateLogs -n 3 500M| 56s |

##### result size
```
[root@header-1 rotate_logs]# ll
总用量 1272308
-rw-r--r--  1 root root     10970 8月  15 13:45 rotatelogs.py
-rw-r--r--  1 root root       240 8月  15 16:25 test_rotatelog.sh
-rw-r--r--  1 root root      3061 8月  15 16:12 user_custom_script.sh
-rw-r--r--  1 root root 254170229 8月  15 16:13 weiflow-from-weiclient.log
-rw-r--r--  1 root root 524304017 8月  15 16:13 weiflow-from-weiclient.log.1
-rw-r--r--  1 root root 524290323 8月  15 16:13 weiflow-from-weiclient.log.2
```
```
[root@header-1 rotate_logs]# ll -h
总用量 1.3G
-rw-r--r--  1 root root  11K 8月  15 13:45 rotatelogs.py
-rw-r--r--  1 root root  240 8月  15 16:25 test_rotatelog.sh
-rw-r--r--  1 root root 3.0K 8月  15 16:12 user_custom_script.sh
-rw-r--r--  1 root root 243M 8月  15 16:13 weiflow-from-weiclient.log
-rw-r--r--  1 root root 501M 8月  15 16:13 weiflow-from-weiclient.log.1
-rw-r--r--  1 root root 501M 8月  15 16:13 weiflow-from-weiclient.log.2
```

##### future
- rotatelogs - Piped logging program to rotate Apache logs
- all mentioned in https://httpd.apache.org/docs/2.4/programs/rotatelogs.html will be added.

