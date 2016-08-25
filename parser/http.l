%{
#include <stdio.h>
#include "y.tab.h"
%}
%%
METHOD_GET	yyval = yytext return METHOD;
%%
