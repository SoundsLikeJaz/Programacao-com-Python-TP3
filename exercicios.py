from funcoes import *;

# ---------------------------- Exercício 01 ----------------------------       
def ex01():
    nome = coletar_nome();
    sobrenome = coletar_sobrenome();
    print(nome + ' ' + sobrenome);
    
# ex01();

# ---------------------------- Exercício 02 ----------------------------

def ex02():
    nome_completo = coletar_nome_completo();
    for nome in nome_completo:
        print(nome, end=' ');
    
# ex02();

# ---------------------------- Exercício 03 ----------------------------

def ex03():
    nome_completo = coletar_nome_completo();
    for nome in nome_completo[1::]:
        print('', nome.upper(), end='');
    
    print(',', nome_completo[0]);
            
# ex03();

# ---------------------------- Exercício 04 ----------------------------

def ex04():
    data = coletar_data();
    for day in range(len(data)):
        data[day] = int(data[day]);
        
    for day in data:
        print(day, end=' ');
    
# ex04();

# ---------------------------- Exercício 05 ----------------------------

def ex05():
    data = coletar_data();
    
    if data:
        print('Data válida.');
        
# ex05();
    
# ---------------------------- Exercício 06 ----------------------------

def ex06():
    data = coletar_data();
    print(data[0], 'de', nomear_mes(data[1]), 'de', data[2]);
    
# ex06();

# ---------------------------- Exercício 07 ----------------------------

def ex07():
    termo = input('Digite um termo a ser verificado: ');
    
    print(f"{termo} {"" if e_palindromo(termo) else "não "}é um palíndromo.");
    
# ex07();

# ---------------------------- Exercício 08 ----------------------------

def ex08():
    palavra = input('Digite uma palavra: ');
    num = contar_vogais(palavra);
    
    if num == 0:
        print(f'A palavra "{palavra}" não possui vogais.');
    elif num == 1:
        print(f'A palavra "{palavra}" possui apenas 1 vogal.');
    else:
        print(f'A palavra "{palavra}" possui {contar_vogais(palavra)} vogais.');
        
# ex08();

# ---------------------------- Exercício 09 ----------------------------

def ex09():
    telefone = coletar_telefone();
    print(formatar_telefone(telefone));
    
# ex09();

# ---------------------------- Exercício 10 ----------------------------

def ex10():
    dia = coletar_dia_da_semana();
    print(dia);
    
# ex10();

# ---------------------------- Exercício 11 ----------------------------

def ex11():
    cpf = entrar_cpf();
    print(cpf);
    
# ex11();

# ---------------------------- Exercício 12 ----------------------------

def ex12():
    palavra = input('Digite uma palavra ou frase: ');
    
    for letra in palavra[::-1]:
        print(letra, end='');
        
# ex12();

# ---------------------------- Exercício 13 ----------------------------

def ex13():
    palavra = input('Digite uma palavra ou frase: ');
    print(palavra[::-1]);
    
# ex13();

# ---------------------------- Exercício 14 ----------------------------

def ex14():
    palavra = input('Digite uma palavra ou frase: ');
    print(palavra[0:5:]);
    print(palavra[len(palavra) - 5::]);
    
# ex14();

# ---------------------------- Exercício 15 ----------------------------

def ex15():
    termo = input('Digite algumas informações separadas por ; (ponto e vírgula): ');
    termo = termo.replace(';', ',');
    print(termo);
    
# ex15();

# ---------------------------- Exercício 16 ----------------------------

def ex16():
    num1 = int(input('Digite o primeiro número: '));
    num2 = int(input('Digite o segundo número: '));
    
    print(f'A média de {num1} e {num2} é {(num1 + num2) / 2}.');