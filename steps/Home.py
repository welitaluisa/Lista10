from behave import *


@given('que acesso o site blazedemo')
def que_acesso_o_site_blazedemo(context):
    print('Passo 1 - Abriu o site')


@when('clico em home')
def clico_em_home(context):
    print('Passo 2 - Clicou em home ')


@when('clico em register')
def clico_em_register(context):
    print('Passo 3 - Clicou em Register')


@when('digito o name')
def digito_o_name(context):
    print('Passo 4 - digitou o name')


@when('digito a company')
def digito_a_company(context):
    print('Passo 5 - digitou a company')


@when('digito o email')
def digito_o_eMail(email):
    print('Passo 6 - digitou o email')


@when('digito o password')
def digito_o_password(context):
    print('Passo 7 - digitou o password')


@when('confirmo o password')
def confirmo_o_password(context):
    print('Passo 8 - confirma o password')


@when('clico no botao register')
def clico_no_botao_register(context):
    print('Passo 9 - clicou no botão Register')


@then('Valido que o Cadastro foi realizado com sucesso')
def Valida_que_o_Cadastro_foi_realizado_com_sucesso(context):
    print('Passo 10 - validou os dados e registra o usuario')
