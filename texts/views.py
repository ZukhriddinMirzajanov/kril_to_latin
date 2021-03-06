from django.shortcuts import render

letters = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'yo',
    'ж': 'j',
    'з': 'z',
    'и': 'i',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'x',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'ъ': "'",
    'ь': '',
    'э': "e",
    'ю': "yu",
    'я': "ya",
    'ў': "o'",
    'қ': "q",
    'ғ': "g'",
    'ҳ': "h",
    ' ': ' ',
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'Ye',
    'Ё': 'Yo',
    'Ж': 'J',
    'З': 'Z',
    'И': 'I',
    'Й': 'Y',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'X',
    'Ц': 'Ts',
    'Ч': 'Ch',
    'Ш': 'Sh',
    'Ъ': "'",
    'Ь': '',
    'Э': "E",
    'Ю': "Yu",
    'Я': "Ya",
    'Ў': "O'",
    'Қ': "Q",
    'Ғ': "G'",
    'Ҳ': "H",
}

kril_letters = "йцукенгшщзхъфывапролджэюбьтимсчяЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ"

def index(request):
    return render(request, 'index.html')

def text(request):
    text  = request.GET.get('convert')
    converted = kril_lotin(text)
    context  = {
        'converted': converted
    }
    return render(request, 'text.html', context)

def kril_lotin(b):
    a = """"""
    v = 1
    for i in b:
        v = 0
        for j in letters:
            if i == j:
                a += letters[j]
            elif kril_letters.find(i)<0 and v==0:
                a += i
                v = 1
    return a