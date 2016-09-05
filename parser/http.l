%{
#include <stdio.h>
#include "y.tab.h"
%}
%option noyywrap

WORD	[a-z|\.]*
%%
"GET"	printf("lex:GET:%s\n", yytext); return METHOD_GET;
"/"	printf("lex:SIMPLE_URI:%s\n", yytext); return SIMPLE_URI;
"http:"  printf("lex:http:%s\n", yytext); return http;
"\r\n"	 printf("lex:CRLF:%s\n", yytext); return CRLF;
"{WORD}" printf("lex:addr:%s\n", yytext); return (addr);

%%
