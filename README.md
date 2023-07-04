<p align="center">
    <img width="80%" src="https://raw.githubusercontent.com/cahian/TwoChatGPTs/main/public/readme.png" alt="TwoChatGPTs README image">
</p>
<h1 align="center">TwoChatGPTs</h1>

Colocamos 2 ChatGPTs para conversar (sem que eles soubessem).

Essa manhã, eu estava em casa no banheiro me arrumando para ir para o trabalho quando eu tive a brilhante ideia: "Por que não fazer um programa que faz o ChatGPT conversar com ele mesmo?", foi daí que surgiu esse projeto.

## Instalação

Por enquanto não há nenhum binário executável ou forma mais conveniente de executar esse programa. Você precisa ter o [Python] instalado na sua máquina e colocar esse repositório em uma pasta.

```sh
git clone https://github.com/cahian/TwoChatGPTs.git
cd TwoChatGPTs
python -m venv venv
# No Windows
./venv/scripts/activate
# No Linux
./venv/bin/activate
pip install -r requirements.txt
```

## Uso

Se caso você tenha fechado o terminal e aberto ele de novo, você precisa novamente entrar na pasta do projeto e ativar o ambiente virtual.

```sh
cd TwoChatGPTs
# No Windows
./venv/scripts/activate
# No Linux
./venv/bin/activate
```

Para executar o programa, basta você chamar ele através do comando Python.

```sh
python -m tchatgpt
```

## Observações

Por favor, esse projeto ainda está em fase experimental e de desenvolvimento.

Toma cuidado para não solicitar mais de 3 respostas do ChatGPT dentro de 1 minuto, senão um limite vai ser atingido e o programa vai ser finalizado.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)

[Python]: https://www.python.org/downloads/

