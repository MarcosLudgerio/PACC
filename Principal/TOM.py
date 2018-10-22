import random
nome = "Marcos"
def boasVindas():
    mensagemBoasVindas = ['Olá, seja muito bem vindo, meu nome é TOM!', 'Olá meu nome é TOM, seja muito bem vindo!', 'Oi, meu nome é TOM. Seja bem vindo!']
    retorno = random.choice(mensagemBoasVindas)
    print(retorno)

def depoisDasBoasVindas():
    segundaMensagem = ['Eu vou lhe acompanhar nessa grande aventura!', 'Eu vou lhe acompanha no que for necessário!', 'Isso vai ser muito divertido!', 'Nós ainda temos muito o que conversar!', 'Eu sou o encarregado de lhe guiar nessa aventura especial!', 'UAU! Vamos brincar muito ainda!']
    retorno = random.choice(segundaMensagem)
    print(retorno)

def apresentacao():
    apresenta = ['Ops, me desculpa. Você ainda nem se apresentou', 'Você me já me disse quem você é? Estou tendo problemas com meu HD. Devo ter me esquecido!', 'Orxx, você não me disse quem é você! Perdão!', 'Nós já fomos apresentados?', 'Desculpa a falta de educação. Não perguntei o seu nome!', 'Aah, meus Circuitos! Esqueci de perguntar o seu nome!', 'Já nos conhecemos antes? Como é seu nome mesmo?']
    retorno = random.choice(apresenta)
    print(retorno)

def iniciarJogo(nome):
    inicio = [', vamos deixar de enrolação e partir par o que interessa!', ', estou ansioso pra começar, vamos logo!', ', mal vejo a hora de começar, vamos logo!', ', vamos parar de enrolação e ir ao que interessa!', ', que tal irmos ao que interessa?']
    retorno = random.choice(inicio)
    retorno = nome + retorno
    print(retorno)

def jogadorouadmin(nome):
    jogadorAdmin = [', o que você é?', ', qual a sua função?', ', você veio para jogar?', ', você é jogador ou administrador?', ', me diga qual o seu objetivo?']
    retorno = random.choice(jogadorAdmin)
    retorno = nome + retorno
    print(retorno)


def notificandoAdministrador(nome):
    notificando = [', com grandes poderes vêm grandes resposábilidades. Muito cuidado!', ', a partir daqui é importante você ter certeza do que está fazendo', ', nossa, que chic! Você realmente sabe o que está fazendo, né?!', ', uau! É importante que você saiba dos problemas que podem ser ocasionados com isso!', ', muito cuidado!']
    retorno = random.choice(notificando)
    retorno = nome + retorno
    print(retorno)


def selecionarNivel(nome):
    escolherNivel = [', vai encarar?', ', onde você quer brincar?', ', tem experiência em computação? É importante que sim!', ', o importante é se divertir, não acha?']
    retorno = random.choice(escolherNivel)
    retorno = nome + retorno
    print(retorno)

def nivelFacil():
    fraseFacil = ['Prometo caprichar nas questões!','Então você quer começar devagar. Muito interessante!', 'Não importa o nível o que vale é a diversão.', 'Ok, então vamos começar do básico!','Como quiser! Vamos começar devagar','Quem manda é o freguês! Vamos nessa!','Uau, você tem cara de ser bastante inteligente! Vai acertar todas!']
    retorno = random.choice(fraseFacil)
    print(retorno)

def nivelMedio():
    fraseMedio = ['Huum, então quer dizer que você gosta de desafios!', 'Uau! Que ousado! Irei caprichar nas questões!', 'Nossa! Muito Bem!', 'Sabia que iria escolher isso, está escrito na sua cara! Boa sorte!', 'Isso vai ser interessante, muito interessante!', 'Aah, que legal! Vamos nos diveritir!']
    retorno = random.choice(fraseMedio)
    print(retorno)

def nivelDificil():
    fraseDificil = ['Nossa, Que ousadia! Você tem cara disso mesmo.', 'Uau, estou na torcida por você!','Você é uma pessoa inteligente, pelo menos pela cara!', 'Nossa, não esperava isso! Boa sorte!', 'Uau, você me surpreedendo cada vez mais!', 'Sério, eu estou começando a ficar com medo de você!', 'As questões nem estão muito dificeis. Mentira, estão sim!']
    retorno = random.choice(fraseDificil)
    print(retorno)

def rendimentoBaixo(nome):
    baixo = [', como assim?! Não acredito! Achei se daria melhor!', ', nossa! Eu entendo, quem colocou essas questões tinha minhoca na cabeça! (espero que o meu desinvolvedor não veja isso)', ', aah! É uma pena! Mas não desanime, você pode estudar mais e tentar novamente, esperarei ansioso por você!', ', caramba! Deve ter acontecido algo. Apostei todas minhas fichas em você!', ', me desculpa! Deveria ter feito perguntas mais fáceis! ', ', calma! se é possível você conversar com uma maquina com sua voz mental, então é possível melhorar o rendimento!', ', não desista! Tente novamente, irá se sair melhor na próxima!', ', a culpa não foi sua! A culpa é de quem selecionou as questões. Ele é doido!', ', uau! esperaria mais de você. Se fizer lhe sentir melhor, eu posso hackear o meu desinvolvedor! (espero que ele não veja isso)']
    retorno = random.choice(baixo)
    retorno = nome + retorno
    print(retorno)

def rendimentoMedio(nome):
    medio = [', nossa! Você não foi ruim! Mas, poderia ter sido melhor!', ', nossa! Apostei minhas fichas que você iria se sair melhor!', ', estou muito feliz com o resultado! Olha as questões, poderia ter sido pior!', ', o cara que me fez não tem juízo. Ele colocou questões que nem ele sabe! (Não conta pra ele por favor!)', ', caramba! Poderia ter sido melhor! Culpe o meu desinvolvedor, ele é doido!', ', calma! se é possível você conversar com uma maquina com sua voz mental, então é possível melhorar o rendimento!', ', uau! esperaria mais de você. Se fizer lhe sentir melhor, eu posso hackear o meu desinvolvedor! (espero que ele não veja isso)']
    retorno = random.choice(medio)
    retorno = nome + retorno
    print(retorno)

def rendimentobom(nome):
    bom = [', nossa, pra alguém que conversa com uma máquina com a voz mental, você foi extraordinariamente bem!',', uau! Você se saiu muito bem! Parabéns!', ', que show! Estou pulando de algria!', ', nossa, muito bacana! Confesso que não daria nada por você. Me enganei, você é show!', ', Nossa, mano! Ta sem nerdisse, Ein?! Parabéns!', ', uau! Mandou o cara que selecionou as questões ir pastar!', ', muito obrigado! Me fez ganhar uma aposta. Dei todas minhas fichas em você.', ', uau! Apostei em você e apostei certo!']
    retorno = random.choice(bom)
    retorno = nome + retorno
    print(retorno)

def rendimentoExcelente():
    exclente = [', caramba! Estou com medo! Você é realmente terestre?',' nossa, pra alguém que conversa com uma máquina com a voz mental, você foi extraordinariamente bem!',' mal vejo a hora de avisar ao meu desinvolvedor que ele não é de nada. Ele não chega ao seus pés!',' NOSSA!!!!! Podem chamar o presidente, você merece uma medalha!',' eu sabia! Essa cara não nega! Gênio, parabéns!',' com esse nivel de questões, você ainda se saiu bem. Tiro meu chapéu pra você!',' você é de fato, um gênio! Sabia desde o inicio!',' quem diria, ein?! Nem o meu pensamento mais otimista lhe daria esse resultado!',' nossa, que incrível! Meu medidor de nerdisse disparou!', ', uau! Mano do céu. Podem ligar pra NASA, acabamos de encontrar um gênio!']
    retorno = random.choice(exclente)
    retorno = nome + retorno
    print(retorno)

def frasesDeAcertos():
    certas = ['Meus parabéns, acertou!', 'Resposta certa!','Muito bem!', 'Exato!', 'Acertou!', 'Exatamente!', 'Genial!']
    retorno = random.choice(certas)
    print(retorno)

def frasesDeErros():
    certas = ['Resposta Errada!', 'Aah, que pena!','Errou!', 'Foi quase!', 'Nossa, achei que fosse acertar essa!', 'Não acredito!', 'Você errou!']
    retorno = random.choice(certas)
    print(retorno)
    
def respostaInvalida():
    frases = ['Resposta inválida!', 'Por favor, responda de maneira válida!', 'Isso é inválido!', 'Não!', 'Você escolheu algo impossível']
    retorno = random.choice(frases)
    print(retorno)

def loginIncorreto():
    frases = ['Você tem certeza que sabe o que está fazendo?', 'Login incorreto!', 'Acesso negado!', 'Algo errado não esta certo!']
    retorno = random.choice(frases)
    print(retorno)

def erroDeLogin():
    frases = ['Fizemos o possivel, mas não deu! Retornando para o menu inicial!', 'Não foi possivel fazer o seu login, voltando para o menu inicial!', 'O seu login deu errado, o menu inical será exibido.', 'Infelizmente não foi possivel fazer o seu login, o menu inicial será exibido!']
    retorno = random.choice(frases)
    print(retorno)

def saindoDoSistema():
    frases = ['Foi ótimo conversar com você, até a próxima!', 'Que pena que acabou. Agora vou descansarum pouco.', 'Aah, já vai? Pena! Agora vou ali escanear o meu sistema!', 'Enfim, foi ótimo. Até mais, lembre que eu estou aqui!', 'Até a próxima execução.', 'Já vai? Que pena! Eu ia dar uma volta mas lembrei que sou apenas um sistema que sortea frases aleatoriamente! Que vida!']
    retorno = random.choice(frases)
    print(retorno)

def mudaAlternativa():
    frases = ['Já tem alternativa que nem essa!', 'Você está ficando louco ou quer me enlouquecer? Tá funcionando.', 'ALternativa duplicada! Mude!', 'Só pode existir apenas uma alternativa correta!', 'Duas alternativas corretas?! Aí você já quer demais!']
    retorno = random.choice(frases)
    print(retorno)

def senhaIncorreta():
    frases = ['Você tem certeza que sabe o que está fazendo?', 'Senha incorreta!', 'Acesso negado!', 'Algo errado não esta certo!']
    retorno = random.choice(frases)
    print(retorno)
