palavras_reservadas = ["break",
                       "case",
                       "const",
                       "continue",
                       "default",
                       "do",
                       "else",
                       "for",
                       "if",
                       "var",
                       "return",
                       "struct",
                       "switch",
                       "typedef",
                       "while",
                       "string",
                       "class",
                       "struct",
                       "include",
                       "print",
                       "true",
                       "false",
                       "nil",
                       "fun"]

operadores = ["+=",
              "-=",
              "++",
              "--",
              "<=",
              ">=",
              "->",
              "==",
              "!=",
              "or",
              "and",
              "*=",
              "/=",
              "<",
              ">",
              "+",
              "-",
              "=",
              "*",
              "/",
              "%",
              "!",
              "&"
              ]


ignoraveis = [" ",
              "'",
              "\n",
              "	"
              ]

expressoes_regulares = {
    'numerais': r'\b(\d+\.?\d*)\b',
    'caracteres_especiais': r"[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""'',
    'identificadores': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'delimitadores': r"[\(\)\[\]\{\};,:]",
    'constantes_textuais': r'"(.*?)"'
}
