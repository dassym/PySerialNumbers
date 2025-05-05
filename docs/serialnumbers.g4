/**
 * Grammar to define one or more serial numbers.
 */
 
grammar serialnumbers;

/**
 * List of serial numbers ranges
 */ 
list : range ( ';' range )* ;
	
/**
 * Range of serial numbers. 
 */ 
range : '-'? sn ( '-' sn | ':' DIGIT+ )? ;

/**
 * serial number. 
 */ 
sn : ALPHANUM* DIGIT+ ALPHA* ;

/**
 * Digit characters
 */ 
DIGIT : [0-9] ;

/**
 * Alphabetic characters
 */ 
ALPHA : [A-Za-z] | '+' | '/' | '*' | '.' | ',' | '$' | '#' | '@' | '~' | '_' ;

/**
 * Alphabetic and numeric characters  
 */ 
ALPHANUM : ALPHA | DIGIT ;