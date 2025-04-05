
# INFINITE CALC

> Uma biblioteca matemática abrangente feita exclusivamente em python abordando do básico ao avançado!

## DESCRIÇÃO

Infinite Calc é uma biblioteca matemática totalmente baseada em python que aborda operações e expressões das mais simples as mais complexas, além disso esta biblioteca incluirá calculos de outras áreas como física, química, geografia e letras.

## FERRAMENTAS DISPONÍVEIS

- **Operações Básicas**:
  - Soma, Subtração, Multiplicação, Divisão.

- **Operações Avançadas**:
  - Potenciação: Calcula a potencia de um número por N potência
  - Radiciação N-ésima: Calcula raízes N-ésimas
  - Fatorial: Calcula o fatorial de N número
  - Logaritmação: Calcula logaritmos de qualquer base além de logaritmos naturais

- **Resolvedor de Equações**:
  - Equação do primeiro grau(afim): Calcula a raiz de uma equação afim
  - Equação do segundo grau(bhaskara): Calcula as 2 raízes de uma equação quadrática, suportando c = 0
  - Discriminante(delta): Calcula o discriminante da equação quadrática

- **Constantes matemáticas com precisão**:
  - π: Valor de pi com precisão de 40 casas decimais
  - e: Constante de Euler com precisão de 40 casas decimais

## INSTALAÇÃO

**Clone o Repositório**:  

git clone <https://github.com/GhostPro1736/InfiniteCalc.git>

## EXEMPLO DE USO

### CÁLCULO DE LOGARITMOS DE QUALQUER BASE E LOGARITMOS NATURAIS

from InfiniteCalc import Operations  

**Logaritmo em qualquer base**  
print(Operations.log(1000,10)) ≈ 3.0  

**Logaritmo natural**  
print(Operations.natural_log(2)) ≈ 0.6931

### CÁLCULO DE BHASKARA E DETERMINANTE DELTA

from InfiniteCalc import EqSolver  

**Equação quadrática**  
print(EqSolver.bhaskara(1,-3,2)) = (2.0, 1.0)  

**Discriminante delta**  
print(EqSolver.delta(1,-3,2)) = 1  

## CONTRIBUIÇÕES

Contribuições sempre serão bem vindas! caso deseje contribuir para este projeto siga os passos a seguir:  

1. Faça um fork do repositório.
2. Crie uma branch para sua feature ou correção (`git checkout -b minha-feature`).
3. Faça commit das suas alterações (`git commit -m 'Adicionei minha feature'`).
4. Envie um push para a branch (`git push origin minha-feature`).
5. Abra um Pull Request.
6. Preencha o Pull Request: Preencha as informações necessárias para o pull request, como uma descrição detalhada das alterações feitas. Certifique-se de fornecer informações claras e concisas para que o proprietário do repositório original possa entender suas contribuições.
7. Envie o Pull Request: Clique em "Create pull request" para enviar o pull request para o repositório original. Eu irei verificar as mudanças assim que possível para trazer novas features ou as devidas alterações

Para mais informações sobre mim ou o projeto:

- GitHub: [JoaoVitor197843](https://github.com/JoaoVitor197843)

- Discord: [.ghost_pro](https://discord.com/)

- Email: [João_Vitor](<mailto:jv2093809@gmail.com?subject=InfiniteCalc&body=Olá! eu gostaria de propor uma ideia para o InfiniteCalc>)

## LICENÇA

Este projeto open source está utilizando a [licença MIT](LICENSE.md). Acesse o arquivo para mais detalhes.

### PERMISSÕES GARANTIDAS PELA LICENÇA MIT

- Uso comercial
- Modificação
- Distribuição
- Uso privado

fique a vontade para utilizar esta biblioteca da forma que desejar. Obrigado por dedicar seu tempo ao Infinite Calc — desejo um ótimo dia a todos os desenvolvedores que lerem isto!
