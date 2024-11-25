def coletar_nome():
    """
    Coleta um nome e verifica se é válido.

    Args:
        None
    Returns:
        str: Nome
    """
    
    while True:
        nome = input('Digite o nome: ');
        if (validar_nome(nome)):
            return nome;
        
        print('Nome inválido. Digite apenas letras.');
        
def coletar_sobrenome():
    """
    Coleta um sobrenome e verifica se é válido.
    
    Args:
        None
    Returns:
        str: Sobrenome
    """
    
    while True:
        sobrenome = input('Digite o sobrenome: ');
        if (validar_nome(sobrenome)):
            return sobrenome;
        
        print('Sobrenome inválido. Digite apenas letras.');
        
def coletar_nome_completo():
    """
    Coleta um nome completo e verifica se é válido.
    
    Args:
        None
    Returns:
        list: Nome completo
    """
    
    while True:
        nome_completo = input('Digite o nome completo: ');
        if (validar_nome_completo(nome_completo)):
            return nome_completo.split(" ");
        
        print('Nome inválido. Digite apenas letras.');
        
def validar_nome(nome):
    """
    Verifica se o nome é válido.
    
    Args:
        str: Nome
    Returns:
        bool: True se o nome é composto apenas por letras e composto por mais de 1 caractere, False caso contrário
    """
    
    if (nome.isalpha() and len(nome) > 1):
        return True;
    
    return False;

def validar_nome_completo(nome_completo):
    """
    Verifica se o nome completo é válido.
    
    Args:
        str: Nome completo
    Returns:
        bool: True se os nomes são compostos apenas por letras e composto por mais de 1 caractere, False caso contrário
    """
    
    nome_completo = nome_completo.split(" ");
    for nome in nome_completo:
        if (not validar_nome(nome)):
            return False;
        
    return True;

def coletar_data():
    """
    Coleta uma data e verifica se é válida.
    
    Args:
        None
    Returns:
        list: Data
    """
    
    while True:
        data = input('Digite a data: ');
        if (validar_data(data) and verificar_data(data)):
            return data.split('/');
                
        
        print('Data inválida. Digite no formato dd/mm/aaaa.');
        
def validar_data(data):
    """
    Verifica se a data é válida ao formato dd/mm/aaaa.
    
    Args:
        str: Data
    Returns:
        bool: True se a data é composta por 10 caracteres, sendo 2 números, uma barra, 2 números, uma barra, 4 números, False caso contrário
    """
    
    data = data.split('/');
    if (len(data) != 3):
        return False;
    
    if (not data[0].isdigit() or not data[1].isdigit() or not data[2].isdigit()):
        return False;
    
    if (len(data[0]) != 2 or len(data[1]) != 2 or len(data[2]) != 4):
        return False;
                            
    return True;

def verificar_data(data):
    """
    Verifica se a data é válida no calendário.
    
    Args:
        str: Data
    Returns:
        bool: True se a data é válida, False caso contrário
    """
    
    data = data.split('/');
    dia = int(data[0]);
    mes = int(data[1]);
    ano = int(data[2]);
    
    if (mes < 1 or mes > 12):
        return False;
    elif (dia < 1):
        return False;      
    elif (mes == 2):
            
        if (dia > 29):
            return False;
        elif (dia == 29 and not e_bissexto(ano)):
            return False;
            
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if (dia > 30):
            return False;
    else:
        if (dia > 31):
            return False;
            
    return True;

def e_bissexto(ano):
    """
    Verifica se o ano é bissexto.
    
    Args:
        int: Ano
    Returns:
        bool: True se o ano é bissexto, False caso contrário
    """
    
    if (ano % 4 == 0 and ano % 100 != 0):
        return True;
    elif (ano % 400 == 0):
        return True;
    
    return False;

def nomear_mes(mes):
    """
    Nomeia o mês.
    
    Args:
        int: Mês
    Returns:
        str: Nome do mês
    """
    
    mes = int(mes);
    match mes:
        case 1:
            return 'janeiro';
        case 2:
            return 'fevereiro';
        case 3:
            return 'março';
        case 4:
            return 'abril';
        case 5:
            return 'maio';
        case 6:
            return 'junho';
        case 7:
            return 'julho';
        case 8:
            return 'agosto';
        case 9:
            return 'setembro';
        case 10:
            return 'outubro';
        case 11: 
            return 'novembro';
        case 12:
            return 'dezembro';
        case _:
            raise ValueError('Mês inválido.');
        
def e_palindromo(termo):
    """
    Verifica se o termo é um palíndromo.
    
    Args:
        str: Termo
    Returns:
        bool: True se o termo é um palíndromo, False caso contrário
    """
    
    index = 0;
    while index < len(termo) / 2:
        if (termo[index] != termo[len(termo) - index - 1]):
            return False;
        
        index += 1;
        
    return True;

def contar_vogais(palavra):
    """
    Conta as vogais de uma palavra.
    
    Args:
        str: Palavra
    Returns:
        int: Número de vogais
    """
    
    vogais = 'aeiou';
    count = 0;
    for letra in palavra:
        if letra in vogais:
            count += 1;
            
    return count;

def coletar_telefone():
    """
    Coleta um telefone e verifica se é válido.
    
    Args:
        None
    Returns:
        str: Telefone - Formato (xx) xxxxx-xxxx
    """
    while True:
        telefone = input('Digite o telefone: ');
        if (validar_telefone(telefone)):
            return telefone;
        
        print('Telefone inválido. Digite 11 numeros.');
        
def validar_telefone(telefone):
    """
    Verifica se o telefone é válido.
    
    Args:
        str: Telefone
    Returns:
        bool: True se o telefone é composto por 11 números, False caso contrário
    """
    
    if (telefone.isdigit() and len(telefone) == 11):
        return True;
    
    return False;

def formatar_telefone(telefone):
    """
    Formata o telefone no padrão (xx) xxxxx-xxxx.
    
    Args:
        str: Telefone
    Returns:
        str: Telefone formatado - (xx) xxxxx-xxxx
    """
    
    return f'({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}';

def coletar_dia_da_semana():
    """
    Coleta o dia da semana e verifica se é válido, nomeando-o.
    
    Args:
        None
    Returns:
        str: Dia da semana
    """
    
    while True:
        dia = int(input('Digite o dia da semana: '));
        if (validar_dia_da_semana(dia)):
            return nomear_dia_da_semana(dia);
        
        print('Dia da semana inválido. Digite o número do dia da semana.');
        
def validar_dia_da_semana(dia):
    """
    Verifica se o dia da semana é válido.
    
    Args:
        int: Dia da semana
    Returns:
        bool: True se o dia da semana é um número entre 1 e 7, False caso contrário
    """
    
    if (dia >= 1 and dia <= 7):
        return True;
    
    return False;

def nomear_dia_da_semana(dia):
    """
    Nomeia o dia da semana.
    
    Args:
        int: Número do dia da semana
    Returns:
        str: Nome do dia da semana
    """
    
    match dia:
        case 1:
            return 'Domingo';
        case 2:
            return 'Segunda';
        case 3:
            return 'Terça';
        case 4:
            return 'Quarta';
        case 5:
            return 'Quinta';
        case 6:
            return 'Sexta';
        case 7:
            return 'Sábado';
        case _:
            raise ValueError('Dia da semana inválido.');
        
def entrar_cpf():
    """
    Coleta um CPF e verifica se é válido, formatando-o.
    
    Args:
        None
    Returns:
        str: CPF - Formato xxx.xxx.xxx-xx
    """
    
    while True:
        cpf = input('Digite o CPF: ');
        if (validar_cpf(cpf)):
            return formatar_cpf(cpf);
        
        print('CPF inválido. Digite 11 números.');
        
def validar_cpf(cpf):
    """
    Verifica se o CPF é válido.
    
    Args:
        str: CPF
    Returns:
        bool: True se o CPF é composto por 11 números, False caso contrário
    """
    
    if (cpf.isdigit() and len(cpf) == 11):
        return True;
    
    return False;

def formatar_cpf(cpf):
    """
    Formata o CPF no padrão xxx.xxx.xxx-xx.
    
    Args:
        str: CPF
    Returns:
        str: CPF formatado - xxx.xxx.xxx-xx
    """
    
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}';