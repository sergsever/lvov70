%{
#include <stdio.h>
#include "y.tab.h"
%}
%option noyywrap

WORD	[a-z|\.]*
%%
"GET"	printf("lex:GET:%s\n", yytext); return METHOD_GET;
"http://" printf("lex:http:%s\n", yytext); return http;
"\r\n"	printf("lex:CRLF:%s\n", yytext); return CRLF;
{WORD} printf("lex:URI:%s\n", yytext); return URI;

%%
