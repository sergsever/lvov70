%{
#include <stdio.h>
#include "y.tab.h"
%}
%option noyywrap

WORD	[a-z|\.]*
HTTP	"http://"
%%
"GET"	printf("lex:GET:%s\n", yytext); return METHOD_GET;
"{HTTP}"."{WORD}+" printf("lex:URI:%s\n", yytext); return URI;
"\r\n"	printf("lex:CRLF:%s\n", yytext); return CRLF;
%%
