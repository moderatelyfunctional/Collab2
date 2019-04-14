function colpy_down(text)
{
    keywords = ["and", "assert", "async", "as", "await", "break", "class", "continue", "def", "del", "elif",
    "else", "except", "exec", "finally", "for", "from", "global", "if", "import",
    "in", "is", "lambda", "not", "or", "pass", "print", "raise", "return", "try",
    "while", "with", "yield"];

    state = 0;

    formatText = [];
    formatStart = [];
    formatEnd = [];

    line = "<p class=\"bufferText\">";
    //0, default | 1, quote | 2, comment
    for (var a = 0; a < text.length; a++)
    {
        char = text.charAt(a);

        if(state == 0)
        {
            if(char == '/' && text.charAt(a+1) == '/')
            {
                line = line.concat("</p><p class=\"bufferComment\">");
                formatStart.push(a);
                state = 1;
                continue;
            }
            if(char == "\"")
            {
                line = line.concat("</p><p class=\"bufferQuote\">");
                formatStart.push(a);
                state = 2;
                continue;
            }
        }
        if(state == 1)
        {
            if(char == '\\' && text.charAt(a+1) == 'n')
            {
                line = line.concat("</p>");
                formatText.push(line);
                formatEnd.push(a);
                line = "<p class=\"bufferText\">";
                state = 0;
                continue;
            }
        }
        if(state == 2)
        {
            if(char == '\\')
                continue;
            if(char == '\#')
            {
                line = line.concat("</p><p class=\"bufferText\">");
                formatEnd.push(a);
                state = 0;
                continue;
            }
        }
    }
}

function colpy_up(text)
{

}

function colpy_save(text)
{

}
