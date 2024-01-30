## 语言
- [English](api_reference.md)
- [中文](api_reference_zh.md)

# 接口说明
## 基础路径
+ 上传接口的基础路径，所有上传测试数据接口都是依赖此路径演化来的。当不使用上传服务demo，需要深度定制上传服务，比如整合自己现有环境的web服务中，此路径可能会和现有的路径有冲突，或者现存的web服务有自己的路径规划，就可以上传请求映射到其它的路径，同时在客户端中配置自定义的路径即可。
如基础路径为 /report:
    + post /report 为上传性能指标数据
    + put /report/icon 为设置测试引用图标
    + post /report/screenshots 为上传测试过程生成的应用截图，可调用多次，如果截图数量很多
    + put /report/done 为上传完成
+ 此路径也在PerfDog中配置上传服务地址使用到，格式为通用url格式: http(s)://abc.com:port/report
    + http(s) -> 为上传使用的协议，依据此协议开发出的上传服务可以为http/https
    + abc.com -> 为上传服务的部署地址，可以为域名或者ip地址，如PerfDog和上传同机部署时可以为127.0.0.1
    + port -> 为服务端口，http时使用80端口，https时使用443端口，可以省略端口部分，其它情况需要填写端口。
    + /report -> 为上传接口基础路径

> 依此例，使用http协议服务，和PerfDog同机部署运行，端口使用80，基础路径为/report, 在PerfDog中配置的上传服务地址为: http://127.0.0.1/report

## 开始上传测试数据
+ path: 
+ method: post
+ header:
    * Content-Type: 'multipart/form-data'
+ req
    * file_format: json/pb
    * data: file 
+ resp
```json
{
    errCode: 0,
    errStr: "",
    reportId: ""
}
```

> 上传测试过程中生成性能数据，如fps、卡顿等等
>



## 设置测试应用图标
+ path: /icon
+ method: put
+ header:
    * Content-Type: 'multipart/form-data'
+ req
    * reportId
    * icon: file
+ resp
```json
{
    errCode: 0,
    errStr: ""    
}
```

## 上传测试过程中生成的应用截图
+ path: /screenshots
+ method: post
+ header:
    * Content-Type: 'multipart/form-data'
+ req
    * reportId
    * file1: file
    * file2: file
    * file3: file
    * file4: file
    * file5: file
    * ...
+ resp
```json
{
    errCode: 0,
    errStr: ""    
}
```


> 一次可以上传多张 或者使用zip压缩多张图片上传


## 完成上传测试数据
+ path: /done
+ method: put
+ header:
    * Content-Type: 'multipart/form-data'
+ req
    * reportId
+ resp
```json
{
    errCode: 0,
    errStr: ""    
}
```