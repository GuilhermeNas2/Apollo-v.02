<h1>Apollo v.03</h1>
<span>
    Esse script, que carinhosamente apelidei de Apollo, é um robô de automação desenvolvido para acelerar um processo repetitivo em um site de logística. Nele, é necessário importar um arquivo, preencher alguns campos de um formulário e registrar um valor que é gerado no final pelo menos umas 30 vezes ao dia. Obviamente, o script principal do robô só funciona no site que eu configurei; ele é um software privado. Porém, as funcionalidades principais que desenvolvi e quero compartilhar com vocês estão separadas em classes, então podem ser testadas tranquilamente, basta adaptar as informações necessárias.
</span>

<h2>Funcionalidades</h2>
<h3>Excel</h3>
<p>Como principal funcionalidade para o processo, o script foi desenvolvido para que o robô acesse um arquivo Excel, procure informações específicas e insira dados recebidos no final do processo em outra planilha.</p>
<h3>XML</h3>
<p>Outra parte importante do processo é o XML. O Apollo consegue procurar dados necessários dentro desses arquivos para seguir o processo, basta especificar a tag dentro da função usada.</p>
<h3>Email</h3>
<p>Essa função vem a partir da necessidade do tratamento de erros. Uma vez que era preciso enviar emails para os clientes caso os XMLs dos mesmos viessem com falta de informação, o Apollo consegue captar o problema e enviar o email com o anexo do arquivo para que ocorra a correção.</p>


<h2>Requisitos</h2>
<p>Para o funcionamento correto do robô, é necessário clonar o repositório nesse link aqui "https://github.com/GuilhermeNas2/Apollo-v.02.git",após isso devem ser criadas 3 pastas na raiz do projeto: Excel, XML, Concluídos (o nome pode variar, basta mudar ele no caminho). Também é necessário um arquivo .env contendo algumas variáveis específicas que você pode conferir abaixo.</p>
<span>
user= "Usuário para logar no site" <br>
password= "Senha do usuário" <br>
url= "Site a ser acessado" <br>
pathEx, pathXml, pathImg, pathConcluidos= "Caminho das pastas que devem ser criadas no diretório raiz" <br>
email= "Email de quem irá enviar os emails" <br>
passwordEmail= "Senha criada pelo email para acesso de aplicativos de terceiros" <br>
emailsClientes= "Deve ser uma lista de emails [exem@gmail.com]" <br>
</span>
<p>Na questão de bibliotecas, todas devem estar listadas no arquivo requirements.txt, então basta criar um venv no seu repositório e baixar todas facilmente.</p>
<h2>Configurações</h2>
<p>Bom, como já dito anteriormente esse código está configurado para atender as regras de negócios de um cliente, então vou comentar o que as funções fazem e o que pode ser 
alterado para funcionar com você</p>
<img src="./Imagens/ExcelS.PNG">