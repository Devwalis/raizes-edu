📚 Introdução

Nas últimas décadas, vimos um aumento de alfabetizados no Brasil. Contudo, esse número maior refere-se apenas à população mais jovem. Ainda enfrentamos problemas com a população de 30 anos ou mais, para a qual não há nenhuma ação governamental focada em alfabetização. O projeto "Raízes da Educação" surgiu com o objetivo de diminuir a taxa de analfabetismo, principalmente na população mais vulnerável, que é a mais afetada por essa problemática.

🌱 Desenvolvimento

Diante dessa problemática, criamos o projeto para diminuir cada vez mais a taxa de analfabetismo no Brasil, visando inicialmente as comunidades da Região Metropolitana do Recife, com planos de expansão futura.

A Raízes da Educação tem como função criar uma ponte entre as pessoas que querem estudar, mas que, devido a diversas razões, não conseguem frequentar uma escola de forma convencional. Com vagas abertas para todas as idades, mas com ênfase em pessoas acima de 40 anos, o projeto visa conectar professores, espaços disponíveis para aulas e líderes comunitários ou familiares para realizar o cadastro dessas pessoas.

📋 Como funciona o cadastro?

No site será possível realizar o cadastro de quatro maneiras:

Professor

Líder comunitário (pode realizar múltiplos cadastros)

Cadastro simples (um único cadastro)

Instituição (que cede o espaço para aulas)

Após o preenchimento de uma turma, será enviado um e-mail com informações sobre o endereço e horário das aulas, que ocorrerão presencialmente, garantindo acesso inclusivo a todos.

💻 Documentação do Desenvolvimento do Site

🔧 Técnicas e Ferramentas Utilizadas

Back-End: Python com o framework Django

Banco de Dados: SQLite, pela simplicidade e facilidade de integração com o Django

Front-End: HTML, CSS e JavaScript, para garantir uma interface web acessível e interativa

API: Utilização de uma API de busca de CEP para facilitar o preenchimento dos endereços dos usuários

Design: Protótipo inicial feito no Figma, garantindo uma visão clara do layout antes da implementação técnica

📐 Estruturação do Projeto

Planejamento: Identificação do público-alvo e levantamento dos requisitos do sistema

Protótipo: Criação de um esboço no Figma para validar o design com a equipe

Desenvolvimento: Codificação do Back-End e Front-End, integração da API de CEP e banco de dados

Testes: Validação das funcionalidades com usuários simulados

Implantação: Disponibilização do site para uso real

🤔 Justificativa das Escolhas Metodológicas

Django: Escolhido por ser um framework robusto, com uma curva de aprendizado acessível e que permite desenvolvimento rápido

SQLite: Utilizado por ser leve e adequado para um sistema em estágio inicial

Figma: Utilizado para alinhar o design às expectativas dos usuários, reduzindo retrabalho

🏗️ Desenvolvimento Técnico

📊 Arquitetura

O sistema foi projetado em uma estrutura MVT (Model-View-Templates) para separar responsabilidades

O banco de dados armazena informações de usuários (alunos, professores, líderes comunitários e entidades)

O Front-End se comunica com o Back-End via requisições HTTP

🚀 Implementação

Cadastro: Desenvolvimento de formulários para alunos, professores, líderes comunitários e instituições

API de CEP: Implementação para preenchimento automático do endereço

Autenticação: Sistema de login para acesso seguro

🧩 Desafios Enfrentados

Integração da API de CEP: Resolvido através de uma biblioteca que facilitou as requisições

Manutenção do banco de dados: Ajustes na modelagem para suportar diferentes perfis de usuário

📈 Resultados

💡 Exemplos de Funcionamento

Sistema funcional para cadastro de alunos, professores, líderes comunitários e instituições

Preenchimento automático de CEP funcionando corretamente

Dados armazenados corretamente no banco de dados e acessíveis para consulta

🎯 Como Atende aos Objetivos?

Facilita a organização e realização de aulas presenciais para combater o analfabetismo

Oferece uma interface clara e objetiva para os usuários

🏁 Conclusão

📝 Síntese

Foi criado um sistema de cadastro funcional, integrado e alinhado ao objetivo de reduzir o índice de analfabetismo em Pernambuco.

📌 Considerações Finais

O projeto "Raízes da Educação" é um passo importante para a inclusão educacional, com potencial para expansão para outras regiões do Brasil.

🎨 Protótipo

🖥️ Home

Tela inicial que permite acesso aos principais conteúdos do site.

🧾 Tela de Cadastro e Login

Interface para cadastro de novos usuários e login de usuários existentes.

📋 Tela de Listas de Alunos e Professores

Exibe todos os alunos e professores cadastrados, facilitando a gestão das turmas.
