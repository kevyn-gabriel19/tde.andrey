nomes_dos_arquivos = ['texto1.txt', 'texto2.txt', 'texto3.txt']
for nome_arquivo in nomes_dos_arquivos:
    with open(nome_arquivo, 'r') as arquivo:
        numero_de_operacoes = int(arquivo.readline().strip())

        for _ in range(numero_de_operacoes):
            codigo_operacao = arquivo.readline().strip()

            conjunto1 = set(arquivo.readline().strip().split())
            conjunto2 = set(arquivo.readline().strip().split())

            if codigo_operacao == 'U':
                resultado = conjunto1.union(conjunto2)
                print(f"União: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")
            elif codigo_operacao == 'I':
                resultado = conjunto1.intersection(conjunto2)
                print(f"Interseção: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")
            elif codigo_operacao == 'D':
                resultado = conjunto1.difference(conjunto2)
                print(f"Diferença: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")
            elif codigo_operacao == 'C':
                resultado = {(x, y) for x in conjunto1 for y in conjunto2}
                print(f"Produto Cartesiano: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")
