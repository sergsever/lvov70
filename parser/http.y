%{
#include <stdio.h>

void
yyerror(char const *msg)
{
	fprintf(stderr, "%s\n", msg);
}
int main()
{
	yyparse();
}
%}
%token CRLF METHOD_GET HTTP HTTP_VER URI http
%%
QUERY: METHOD_GET http URI HTTP HTTP_VER CRLF http;
%%

