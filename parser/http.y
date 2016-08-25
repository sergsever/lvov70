%{
#include <stdio.h>
%}
%%
CRLF: "\r\n"
METHOD_GET: "GET?";
METHOD_HEAD: "HEAD?";
http: "http://?";
https: "https://?";
HTTP_VER: "HTTP/1.0"
	| "HTTP/1.1";
uri_string: "/?"
	| "/?[a-z|.]+";
URI: http | https uri_string;
METHOD: METHOD_GET
	| METHOD_HEAD;
QUERY: METHOD URI HTTP_VER CRLF;
%%
