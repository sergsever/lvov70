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
QUERY: 
METHOD_GET SIMPLE_URI CRLF CRLF
{
	printf("yacc:query is Ok.\n");
}
;
%%

