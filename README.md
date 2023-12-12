Short python function to quickly fix text that is parsed by resume-processers in job applications. Currently, it mostly applies to the text rendered by Fannie Mae applications. The goal is to expand its functionality and automate it over time. 

To use, you must paste the text into a string. For example, if the parser extract "*         I did this and that at company     Example Inc" then you'd type

`python3 fxaup.py """*         I did this and that at company     Example Inc"""`

Do use triples quotes since that allows to process multi-line strings. 

Currently, the function simply replaces the "*" with "-" and adds newline characters so that the output isn't single-line text but a bullet-like itemizations of the parsed lines. It also replaces multiple spaces with single spaces which seem to be some sort of an artefact from this parser. 