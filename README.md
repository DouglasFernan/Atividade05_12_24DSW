# Expansão do Sistema de Gerenciamento de Produtos

**Branch ativa**: `develop`  
**Superuser**:  
- **Usuário**: `douglas`  
- **Senha**: `douglas`  

---

Com base no exercício anterior, o sistema de gerenciamento de produtos deve ser expandido seguindo os passos abaixo:

## Etapas

1. **Criação de novos modelos**
   - Crie os modelos `Categoria` e `Fornecedor`.
   - Defina os atributos para cada modelo pensando nos dados necessários.

2. **Relacionamentos entre modelos**
   - O relacionamento entre **Produto** e **Categoria** deve ser **muitos para muitos**:
     - Um produto pode estar relacionado a mais de uma categoria.
     - Uma categoria pode conter vários produtos.
   - O relacionamento entre **Produto** e **Fornecedor** deve ser **muitos para um**:
     - Um produto deve ser fornecido por um único fornecedor.
     - Um fornecedor pode fornecer vários produtos.

3. **Administração**
   - Registre os novos modelos no admin do Django.

4. **População dos dados**
   - Utilizando o admin do Django, registre os seguintes dados:
     - **5 produtos** (se já tiver registrado anteriormente, não é necessário registrar novamente).
     - **3 categorias**.
     - **2 fornecedores**.

5. **Páginas do sistema**
   - Crie uma página para listar cada um dos modelos: **Produto**, **Categoria** e **Fornecedor**.
   - Crie uma página de **detalhes de produtos**.
