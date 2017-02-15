# PythonCode
My Python scripts

The Inetsim_parser.py file will format the legacy service.log data from:
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] connect
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] recv: POST /mstat/report HTTP/1.1
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] recv: Host: ping.com
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] recv: Content-Type: json
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] recv: Content-Length: 464
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] recv: Accept: */*
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] recv: Content-Encoding: rc4,gzip
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] recv: Accept-Language: en-us
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] recv: User-Agent: ConnectMobile/31 CFNetwork/808.3 Darwin/16.3.0
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] recv: Accept-Encoding: gzip, deflate
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] recv: Connection: keep-alive
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] recv: <(POSTDATA)>
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] info: POST data stored to: /var/lib/inetsim/http/postdata/0aa781ba68ed36af51cdc2b7f9b70d784ea76caf
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] info: Request URL: http://ping.com/mstat/report
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] info: No matching file extension configured. Sending default fake file.
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] send: HTTP/1.1 200 OK
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] send: Content-Length: 258
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] send: Server: Microsoft-IIS/5.0
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] send: Content-Type: text/html
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] send: Connection: Close
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] send: Date: Wed, 15 Feb 2017 16:39:31 GMT
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] info: Sending file: /var/lib/inetsim/http/fakefiles/sample.html
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] stat: 1 method=POST url=http://ping.com/mstat/report sent=/var/lib/inetsim/http/fakefiles/sample.html postdata=/var/lib/inetsim/http/postdata/0aa781ba68ed36af51cdc2b7f9b70d784ea76caf
[2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] disconnect

So that it will now look like this:
Feb 15 11:40:05 dnssink inetsim [2017-02-15 11:39:31] [1165] [http_80_tcp 2468] [10.10.10.10:55400] connect recv: POST /mstat/report HTTP/1.1 recv: Host: ping.com recv: Content-Type: json recv: Content-Length: 464 recv: Accept: */* recv: Content-Encoding: rc4,gzip recv: Accept-Language: en-us recv: User-Agent: ConnectMobile/31 CFNetwork/808.3 Darwin/16.3.0 recv: Accept-Encoding: gzip, deflate recv: Connection: keep-alive recv: <(POSTDATA)> info: POST data stored to: /var/lib/inetsim/http/postdata/0aa781ba68ed36af51cdc2b7f9b70d784ea76caf info: Request URL: http://ping.com/mstat/report info: No matching file extension configured. Sending default fake file. send: HTTP/1.1 200 OK send: Content-Length: 258 send: Server: Microsoft-IIS/5.0 send: Content-Type: text/html send: Connection: Close send: Date: Wed, 15 Feb 2017 16:39:31 GMT info: Sending file: /var/lib/inetsim/http/fakefiles/sample.html stat: 1 method=POST url=http://ping.com/mstat/report sent=/var/lib/inetsim/http/fakefiles/sample.html postdata=/var/lib/inetsim/http/postdata/0aa781ba68ed36af51cdc2b7f9b70d784ea76caf disconnect
