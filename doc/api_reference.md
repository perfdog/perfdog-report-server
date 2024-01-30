## 语言
- [English](api_reference.md)
- [中文](api_reference_zh.md)

# Interface Description
## Base path
+ The basic path of the upload interface. All upload test data interfaces evolve based on this path. When you do not use the upload service demo, you need to deeply customize the upload service. For example, in a web service that integrates your existing environment, this path may conflict with the existing path, or the existing web service has its own path planning, so you can upload it. The request is mapped to other paths and the custom path can be configured in the client.
For example, the base path is /report:
     + post /report is to upload performance indicator data
     + put /report/icon to set the test reference icon
     + post /report/screenshots is used to upload application screenshots generated during the test process. It can be called multiple times if there are a lot of screenshots.
     + put /report/done for upload completion
+ This path is also used to configure the upload service address in PerfDog. The format is a common url format: http(s)://abc.com:port/report
     + http(s) -> is the protocol used for uploading. The upload service developed based on this protocol can be http/https
     + abc.com -> is the deployment address of the upload service, which can be a domain name or IP address. For example, when PerfDog and upload are deployed on the same machine, it can be 127.0.0.1
     + port -> is the service port. Use port 80 for http and port 443 for https. You can omit the port part. In other cases, you need to fill in the port.
     + /report -> is the base path of the upload interface

> According to this example, use http protocol service, deploy and run on the same machine as PerfDog, use port 80, the basic path is /report, and the upload service address configured in PerfDog is: http://127.0.0.1/report

## Start uploading test data
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

> Generate performance data during the upload test, such as fps, lag, etc.
>



## Set test application icon
+ path: /icon
+ method: put
+ header:
     * Content-Type: 'multipart/form-data'
+req
     * reportId
     * icon: file
+ resp
```json
{
     errCode: 0,
     errStr: ""
}
```

## Upload application screenshots generated during testing
+ path: /screenshots
+ method: post
+ header:
     * Content-Type: 'multipart/form-data'
+req
     * reportId
     * file1: file
     * file2: file
     * file3: file
     * file4: file
     * file5: file
     *...
+ resp
```json
{
     errCode: 0,
     errStr: ""
}
```


> You can upload multiple images at one time or use zip to compress multiple images for upload.


## Complete upload of test data
+ path: /done
+ method: put
+ header:
     * Content-Type: 'multipart/form-data'
+req
     * reportId
+ resp
```json
{
     errCode: 0,
     errStr: ""
}
```