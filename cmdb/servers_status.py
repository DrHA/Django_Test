import paramiko
import os

def server_status():
    free_m=excute_orders("192.168.35.111","free")
    return free_m


#执行命令 输入指令和ip，返回结果
def excute_orders(ip,cmd):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, "esunny", "123456")
    stdin ,stdout, stderr = ssh.exec_command(cmd)
    if(stderr.read() != None):
        return stdout.read()
    ssh.close()
    return 0

## 获取文件输入ip 源地址 目的地址
def get_file(ip,scr,des):
    if(os.path.exists("./192") == False):
        os.mkdir("./192/")
    t = paramiko.Transport(("192.168.35.111",22))
    t.connect(username="esunny", password="123456")
    sftp = paramiko.SFTPClient.from_transport(t)
    src = "/home/esunny/esunny.tap"
    des = "192/esunny"
    sftp.get(src,des)
    t.close()
    os._exit(0)
    return 0





