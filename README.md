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

  ![login](https://github.com/guih1886/alura-space/blob/main/static/assets/imagens/prints/login.png)

####

- `/cadastro`: Essa rota tem a finalidade de cadastrar o novo usuário e recebe através do formulário os campos de `nome`,`email`,`senha` e `confirmação de senha` para o cadastro. Faz a validação da senha e redireciona para a página de login para o acesso.

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

![cadastrar](https://github.com/guih1886/alura-space/blob/main/static/assets/imagens/prints/cadastrar.png)

<!-- Inserir imagem com a #vitrinedev ao final do link -->

### Imagens

![index](https://github.com/guih1886/alura-space/blob/main/static/assets/imagens/prints/index.png#vitrinedev)
![cadastrar-usuario](https://github.com/guih1886/alura-space/blob/main/static/assets/imagens/prints/cadastrar-usuario.png)
