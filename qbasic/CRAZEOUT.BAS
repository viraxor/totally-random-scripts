RANDOMIZE TIMER

FOR I% = 1 TO 10000
  FOR J% = 1 TO 80
    FCOLOR% = INT(RND * 15)
    BCOLOR% = FCOLOR%
    WHILE BCOLOR% = FCOLOR%
      BCOLOR% = INT(RND * 15)
    WEND
    COLOR FCOLOR%, BCOLOR%
    CHAR$ = CHR$(INT(RND * 94) + 33)
    PRINT CHAR$;
  NEXT J%
NEXT I%

