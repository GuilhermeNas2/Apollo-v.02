<h1>Apollo v.03</h1>
<span>Esse script que carinhosamente apelidei de Apollo é um robô de automação desenvolvido para acelerar um processo repetitivo em um site de logística,
nele era necessário importar um arquivo, preencher alguns campos de um formulário e registrar um valor que é gerado no final pelo menos umas 30 vezes ao dia</span>

<h2>Funcionalidade</h2>
<h3>Excel</h3>
<p>Como principal funcionalidade para o processo, o script teve que ser desenvolvido para que o robô acesse um arquivo Excel e procure informações específicas, e inserindo 
dados recebidos no final do processo em outra planilha.</p>
<h3>XML</h3>
<p>Outra parte importante do processo é o XML, o Apollo consegue procurar dados necessários dentro desses arquivos para seguir o processo, basta especificar a tag dentro da função
usada responsável.</p>
<h3>Email</h3>
<p>Essa função vem a partir da necessidade do tratamento de erros, uma vez que era preciso enviar email para os clientes caso os XML's dos mesmos viessem com falta de informação,
então quando o erro ocorre, o Apollo consegue captar o problema e assim enviar o Email com o anexo do arquivo para que ocorra a correção.</p>


<h2>Requisitos</h2>
<p>Bom, para o funcionamento correto do robô é necessario criar 3 pastas na raiz do projeto, Excel, XML, Concluidos (O nome pode variar, basta mudar ele no caminho) um arquivo .env contendo algumas váriaveis em específico que você pode estar olhando abaixo.</p>
<span>
user= "Usuário para logar no site" 
password= "Senha do user"
url= "Site a ser acessado"
pathEx,pathXml,pathImg, pathConcluidos= "Caminho das pastas que devem ser criadas no diretório raiz"
email= "Email do quem ira enviar os emails"
passwordEmail= "Senha criado pelo Email para acesso de aplicativos terceiros"
emailsClientes= "Deve ser uma lista de emails [exem@gmail.com]
</span>