## 语言
- [English](readme.md)
- [中文](readme_zh.md)

1. 安装python 3.x版本，一般使用最新版就好
2. 安装flask框架，推荐使用pip安装
3. 启动执行
    + windows => run.bat
    + macos && linux => run.sh
> 启动脚本使用了缺省的80作为http服务端口，如果因为操作系统限制不让使用80端口，可使用管理员权限运行启动脚本，也可以通过更改上面提到的脚本，使用其它端口作为http服务端口。
4. 仅供开发调试环境使用，部署时请使用类似Gunicorn和uWSGI的方案
5. PerfDog配置上传地址，以demo和perfdog同机部署运行，使用缺省的启动脚本为例，在PerfDog中配置的上传地址为：http://127.0.0.1:80/report
    + http： 一般无需更改
    + 127.0.0.1： 为demo和perfdog同机部署时使用的本地地址，如果此demo部署和perfdog非同一计算机运行，此处需要更换为部署demo计算机真实的IP地址（或者域名）。
    + 80： 为demo作为上传服务使用的端口，如果更改了启动脚本，使用其它端口启动了demo, 上传地址需要更换为更改过后相应的端口
    + /report： 一般无需更改