<!--
.. title: http
.. slug: http
.. date: 2020-01-27 18:58:14 UTC-08:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

# HTTP/HTTPS - hypertext transfer protocol

- communication protocol between web servers and clients
- each command executed independently (i.e. stateless)
- when you enter a URL in your browser, this actually sends an HTTP command to the Web server directing it to fetch and transmit the requested Web page.
- client sends request, server sends response
- HTTP requests made up of: endpoint, method, headers, data (body)
- endpoint (route) is the url you request for
- http methods (verbs)
    - get - retrieves data from server
        - less secure, typically not used with a form
    - post - submits data to server
    - put - updates data already on server
    - delete - deletes data from server
- http header fields (https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)
    - general - general applicability for both request and response messages.
    - response
        - Set-Cookie - An HTTP cookie
            - 	Set-Cookie: UserID=JohnDoe; Max-Age=3600; Version=1
        - Server - A name for the server
            - example:
                - Server: Apache/2.4.1 (Unix)
        - Content-Type - the media type of the content
            - example:
                - Content-Type: text/html; charset=utf-8
        - Content-Length - The length of the response body in octets (8-bit bytes)
            - example:
                - Content-Length: 348
        - Date - The date and time that the message was sent
            - example:
                - Date: Tue, 15 Nov 1994 08:12:31 GMT
    - request (http://gethttp.info/most-common-http-headers.php)
        - Host - specifies domain of the server it is communicating with
            - examples:
                - Host: gethttp.info
                - Host: apple.com:8080
        - Cookie - An HTTP cookie previously sent by the server with Set-Cookie
        - Accept - how the client tells the server what kind of content it can accept in the HTTP response
            - examples:
                - Accept: text/html, text/plain; q=0.6, */*; q=0.1
                - Accept: application/graphql, application/json; q=0.8, application/xml; q=0.7
        - Accept-Encoding - defines what type of content encoding the client can accept in the response body
            - examples:
                - Accept-Encoding: gzip, deflate
                - Accept-Encoding: br, gzip;q=0.9, deflate;q=0.8, *;q=0.1
        - Accept-Language - tells the server the cient's preferred natural language
            - examples:
                - Accept-Language: en-GB, en-US, en;q=0.9
                - Accept-Language: de-AT, de-DE;q=0.9, en;q=0.5
        - Authorization - specifies the authorization scheme and any associated data or token
            - 
            - examples:
                - Authorization: Basic ZmFsa2VuOmpvc2h1YTU=
                - Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzY290Y2guaW8iLCJleHAiOjEzMDA4MTkzODAsIm5hbWUiOiJDaHJpcyBTZXZpbGxlamEiLCJhZG1pbiI6dHJ1ZX0.03f329983b86f7d9a9f5fef85305880101d5e302afafa20154d094b229f75773
        - Referer - tells server where requested URL came from (e.g. from a link, typed into browser address bar...)
            - examples
                - Referer: https://www.google.co.uk/
                - Referer: https://www.quora.com/profile/Lee-Dowthwaite
        - User-Agent - identifies the requesting system
            - examples:
                - User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
- The data (sometimes called “body” or “message”) contains information you want to be sent to the server. This option is only used with POST, PUT, PATCH or DELETE requests.
