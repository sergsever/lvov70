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
%token CRLF METHOD_GET HTTP HTTP_VER SIMPLE_URI http addr
%%
URI
: http '//' addr;
| SIMPLE_URI;
QUERY: METHOD_GET URI HTTP_VER CRLF;

%%

