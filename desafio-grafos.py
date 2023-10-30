valores_grafos = {}

while(True):
    print('Menu')
    print('adiciona vertice <key>')
    print('adiciona aresta <src> <dest> [weight]')
    print('mostra')
    print('sair')
    resposta=input('O que vc gostaria de fazer? \n')
    
    if resposta == 'sair':
        break
    elif resposta.startswith('adiciona vertice'):
        vertice = int(resposta.split(' ')[2])
        valores_grafos[vertice]={}
        print('\n')
    elif resposta.startswith('adiciona aresta'):
        arestaSource = int(resposta.split(' ')[2])
        arestaDestination = int(resposta.split(' ')[3])
        arestaWeight = int(resposta.split(' ')[4])
        for i in valores_grafos:
            if i == arestaSource:
                valores_grafos[i].update({'dst':arestaDestination})
                valores_grafos[i].update({'weight':arestaWeight}) 
        print('\n')
    elif resposta == 'mostra':
        print('Vertice: ', end='')
        for i in valores_grafos:
            print(i,end=' ')
        print('\n')
        for j in valores_grafos:
            print('(src=',j,end='')
            for k in valores_grafos[j]:
                print(f' ,{k}={valores_grafos[j][k]}',end='')
            print(')')
