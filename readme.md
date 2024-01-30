- [English](readme.md)
- [中文](readme_zh.md)

1. Install python 3.x version. Generally, just use the latest version.
2. Install the flask framework. It is recommended to use pip to install it.
3. Start execution
     + windows => run.bat
     + macos && linux => run.sh
> The startup script uses the default 80 as the http service port. If port 80 is not allowed to be used due to operating system restrictions, you can run the startup script with administrator privileges, or you can use other ports as the http service by changing the script mentioned above.
4. For development and debugging environment only, please use solutions like Gunicorn and uWSGI when deploying.
5. PerfDog configures the upload address. Deploy and run demo and perfdog on the same machine. Using the default startup script as an example, the upload address configured in PerfDog is: http://127.0.0.1:80/report
     + http: Generally no need to change
     + 127.0.0.1: This is the local address used when demo and perfdog are deployed on the same computer. If the demo deployment and perfdog are not running on the same computer, this needs to be replaced with the real IP address (or domain name) of the computer where the demo is deployed.
     + 80: The port used by the demo as the upload service. If the startup script is changed and the demo is started using other ports, the upload address needs to be changed to the corresponding port after the change.
     + /report: Generally no need to change