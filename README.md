# Projeto Alura Space

O Alura Space é um projeto desenvolvido com Django, que simula um CRUD para o envio de publicações a respeito de corpos celestes.

| :placard: Vitrine.Dev | Guilherme Henrique  |
| --------------------- | ------------------- |
| :sparkles: Nome       | **Alura-Space**     |
| :label: Tecnologias   | Python, Django, CSS |

### Detalhes do projeto

> - **Fazer login.**
> - **Cadastrar um novo usuário.**
> - **Cadastrar novas imagems para a página inicial.**
> - **Filtrar por categoria.**
> - **Pesquisar por nome.**
> - **Administração através do Django Admin**

- `/login`: Essa rota é responsável por fazer o login na aplicação e redirecionar para a página inicial ou para a página de login, caso o acesso falhe.

  [login]

  ```python
  def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )

            if usuario:
                auth.login(request, usuario)
                messages.success(request, f"Usuário {nome} logado com sucesso!")
                return redirect('index')
            else:
                messages.error(request, f"Usuário {nome} não encontrado.")
                return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})
  ```

####

- `/cadastro`: Essa rota tem a finalidade de cadastrar o novo usuário e recebe através do formulário os campos de `nome`,`email`,`senha` e `confirmação de senha` para o cadastro. Faz a validação da senha e redireciona para a página de login para o acesso.

[cadastrar]

  ```python
  def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)

    if form.is_valid():
        if form['senha1'].value() != form['senha2'].value():
            messages.error(request, "Senhas não conferem.")
            return redirect('cadastro')

        nome = form['nome_cadastro'].value()
        email = form['email'].value()
        senha = form['senha1'].value()

        # busca o usuário no banco de dados
        if User.objects.filter(username=nome).exists():
            messages.error(request, f"Usuário {nome} já cadastrado.")
            return redirect('cadastro')

        usuario = User.objects.create_user(
            username=nome, email=email, password=senha)
        usuario.save()
        messages.success(request, f"Usuário {nome} cadastrado com sucesso.")
        return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})
  ```

  Os valores da especialidade são valores enumerados conforme a regra de negócio do projeto, aqui no caso são quatro
  possibilidades sendo elas: `ORTOPEDIA`,`CARDIOLOGIA`,`GINECOLOGIA` e `DERMATOLOGIA`.
  O endereço deve ser passado como um objeto, contendo os campos de `logradouro`,`bairro`,`cep`,`cidade`,`uf`,`numero`
  e `complemento`.

####

- `POST /pacientes`: Essa rota tem a finalidade de cadastrar o paciente e recebe através do corpo da requisição um JSON
  com
  os dados: `nome`,`email`,`telefone`,`cpf`, e `endereço`.

  ```json
  {
    "nome": "Priscila",
    "email": "priscila@yahoo.com",
    "telefone": "195654986",
    "cpf": "11111111111",
    "endereco": {
      "logradouro": "Rua dos bobos",
      "bairro": "bairro dos bobos",
      "cep": "12345678",
      "cidade": "Cidade dos bobos",
      "uf": "MG",
      "numero": "0",
      "complemento": ""
    }
  }
  ```

  O endereço deve ser passado como um objeto, contendo os campos de `logradouro`,`bairro`,`cep`,`cidade`,`uf`,`numero`
  e `complemento`.

####

- `GET /pacientes` & `GET /medicos`: Essas rotas tem a finalidade de listar os pacientes e médicos cadastrados,
  respectivamente.

  ```json
  {
    "content": [
      {
        "id": 3,
        "nome": "Pedro José",
        "email": "pedrinho@yahoo.com",
        "cpf": "99999999999",
        "telefone": "1932649265",
        "endereco": {
          "logradouro": "Rua dos bobos",
          "bairro": "bairro dos bobos",
          "cep": "12345678",
          "cidade": "Cidade dos bobos",
          "uf": "MG",
          "numero": "0",
          "complemento": ""
        }
      },
      {
        "id": 1,
        "nome": "Priscila Aniele",
        "email": "priscila@yahoo.com",
        "cpf": "11111111111",
        "telefone": "22222222222",
        "endereco": {
          "logradouro": "Rua dos bobos",
          "bairro": "bairro dos bobos",
          "cep": "12345678",
          "cidade": "Cidade dos bobos",
          "uf": "MG",
          "numero": "0",
          "complemento": ""
        }
      }
    ]
  }
  ```

  A resposta é um array com a chave `content` e com os valores dos médicos ou pacientes cadastrados no banco de dados.
  <br/>
  Ao final do array content, temos outras configurações para paginação, aqui, o código foi omitido.

####

- `GET /pacientes/{id}` & `GET /medicos/{id}`: Essas rotas tem a finalidade de detalhar o cadastro dos pacientes ou
  médicos respectivamente, passando o `{id}` do paciente ou médico na URL.

  ```json
  {
    "id": 1,
    "nome": "Priscila Aniele",
    "email": "priscila@yahoo.com",
    "cpf": "11111111111",
    "telefone": "22222222222",
    "endereco": {
      "logradouro": "Rua dos bobos",
      "bairro": "bairro dos bobos",
      "cep": "12345678",
      "cidade": "Cidade dos bobos",
      "uf": "MG",
      "numero": "0",
      "complemento": ""
    }
  }
  ```

  A resposta é um JSON com os dados do paciente ou médico cadastrado com o `{id}` informado.

####

- `PUT /pacientes` & `PUT /medicos`: Essas rotas tem a finalidade de alterar o cadastro do paciente ou
  médico respectivamente, passando o `id` no corpo da requisição JSON com as outras chaves que desejamos alterar.
  Obtendo a resposta da requisição de detalhamento acima, vamos passar a seguinte alteração para `PUT /pacientes`:

  ```json
  {
    "id": "1",
    "nome": "Maria Joaquina",
    "telefone": "19982210064"
  }
  ```

  A resposta será um JSON com os dados do paciente ou médico alterados com o `id` informado. No caso, a resposta seria
  a seguinte:

  ```json
  {
    "id": 1,
    "nome": "Maria Joaquina",
    "email": "priscila@yahoo.com",
    "cpf": "11111111111",
    "telefone": "19982210064",
    "endereco": {
      "logradouro": "Rua dos bobos",
      "bairro": "bairro dos bobos",
      "cep": "12345678",
      "cidade": "Cidade dos bobos",
      "uf": "MG",
      "numero": "0",
      "complemento": ""
    }
  }
  ```

  Note que o id do paciente continua o mesmo, alteramos o `nome` e `telefone`, dessa forma a resposta foi o JSON da
  alteração executada com sucesso!

  ####

  Caso não seja passado o id do paciente ou médico, a resposta será um JSON com o `campo` e `mensagem` de erro.

  ```json
  [
    {
      "campo": "id",
      "mensagem": "não deve ser nulo"
    }
  ]
  ```

####

- `DELETE /pacientes/{id}` & `DELETE /medicos/{id}`: Essas rota tem a finalidade de excluir o cadastro dos pacientes ou
  médicos respectivamente, passando o `{id}` do paciente ou médico na URL.

  ####

  A resposta das requisições são duas possíveis, para **sucesso** a resposta é um código
  [**HTTP 204**](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/204), informando que a
  requisição foi bem sucedida, porém não retornou nada. <br/>
  E, em caso de **erro**, a resposta é um código
  [**HTTP 404**](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/404), informando que o paciente ou médico com
  o `{id}` não foi encontrado.

####

- `POST /consultas`: Essa rota tem a finalidade de cadastrar uma consulta para um paciente. Deve ser passado no corpo da
  requisição um JSON com os campos do `idMedico`, `idPaciente`, e a `data`. Exemplo:

  ```json
  {
    "idMedico": 7,
    "idPaciente": 1,
    "data": "07/05/2023 22:50"
  }
  ```

  A data deve obrigatóriamente ser uma data futura, caso o contrario a resposta será um JSON com o `campo` e `mensagem`
  de erro.

  ```json
  [
    {
      "campo": "data",
      "mensagem": "deve ser uma data futura"
    }
  ]
  ```

  Em caso de sucesso, a resposta será um JSON com os dados da consulta cadastrada:

  ```json
  {
    "id": 5,
    "idMedico": 7,
    "idPaciente": 1,
    "data": "2023-08-07T17:00:00"
  }
  ```

  Nessa resposta temos o `id`, `o id do médico`, `o id do paciente` e a `data` da consulta cadastrada no banco de
  dados. <br/>
  Temos aqui uma validação da regra de negócio de horário da clínica, o qual deve ser um dia da semana e estar entre as
  7 e 18h.

  ```java
  @Component
  public class ValidadorHorarioFuncionamentoClinica implements ValidadorAgendamentoConsulta {

      public void validar(DadosAgendamentoConsulta dados) {
          var dataConsulta = dados.data();
          var domingo = dataConsulta.getDayOfWeek().equals(DayOfWeek.SUNDAY);
          var antesAbertura = dataConsulta.getHour() < 7;
          var depoisAbertura = dataConsulta.getHour() > 18;

          if (domingo || antesAbertura || depoisAbertura) {
              throw new ValidacaoException("Consulta fora do horário de atendimento da clínica.");
          }
      }

  }
  ```

  ####

- `DELETE /consultas`: Essa rota tem a finalidade de excluir uma consulta cadastrada. Deve ser passado no corpo da
  requisição um JSON com os campos do `idConsulta` e `motivo` do cancelamento, o qual também é um enum e deve
  ser `PACIENTE_DESISTIU`, `MEDICO_CANCELOU` ou `OUTROS`.

  ```json
  {
    "idConsulta": 5,
    "motivo": "OUTROS"
  }
  ```

  A resposta da requisição acima será um código
  [**HTTP 204**](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/204), informando que a
  requisição foi bem sucedida, porém não retornou nada. <br/>

<!-- Inserir imagem com a #vitrinedev ao final do link -->

### Imagens

![index](https://github.com/guih1886/alura-space/blob/main/static/assets/imagens/prints/index.png#vitrinedev)
![login](https://github.com/guih1886/alura-space/blob/main/static/assets/imagens/prints/login.png)
![cadastrar](https://github.com/guih1886/alura-space/blob/main/static/assets/imagens/prints/cadastrar.png)
![cadastrar-usuario](https://github.com/guih1886/alura-space/blob/main/static/assets/imagens/prints/cadastrar-usuario.png)
