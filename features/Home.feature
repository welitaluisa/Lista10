Feature: Criar um cadastro No Site Blazer
  Scenario: Cadastrar um usuario
    Given que acesso o site blazedemo
    When clico em home
    And  clico em register
    And  digito o name
    And  digito a company
    And  digito o email
    And  digito o password
    And  Confirmo o password
    And  clico no botao register
    Then valido que o cadastro foi realizado com sucesso


