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
%token CRLF METHOD_GET HTTP HTTP_VER URI
%%
QUERY: METHOD_GET URI HTTP HTTP_VER CRLF;
%%

