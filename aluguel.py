#Classe Equipamento
    #Representa um item individual disponível para aluguel. Deve ser capaz de registrar seu próprio estado (alugado/disponível).

class Equipamento:
    
    #Atributos
        #id_equipamento (int): Identificador único.
        #nome (string): Nome do equipamento.
        #|preco_diaria (float): Custo do aluguel por dia.

    def __init__(self, id_equipamento, nome, preco_diaria):
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.preco_diaria = preco_diaria
        self.status = "Disponível"

   #Métodos
        #alugar(): Altera o status para "Alugado".
   
    def alugar(self):
        if self.status == "Disponível":
            self.status = "Alugado"
            return True
        return False
    
        #devolver(): Altera o status para "Disponível".
    def devolver(self):
        self.status = "Disponível"


class Locadora:

    #Classe Locadora
        #Gerencia o inventário de equipamentos e o faturamento por cliente. Irá interagir diretamente com os objetos Equipamento.

    def __init__(self):
        self.inventario = [] 
        self.faturamento_por_cliente = {}

    def cadastrar_equipamento(self, equipamento):
        self.inventario.append(equipamento)

    def buscar_equipamento(self, id_equipamento):
        for equip in self.inventario:
            if equip.id_equipamento == id_equipamento:
                return equip
        return None

    def realizar_locacao(self, nome_cliente, id_equipamento, dias):
        equipamento = self.buscar_equipamento(id_equipamento)

        if equipamento is None:
            print("Equipamento não encontrado.")
            return

        if not equipamento.alugar():
            print("Equipamento indisponível.")
            return

        custo = equipamento.preco_diaria * dias

        # Atualiza faturamento
        self.faturamento_por_cliente[nome_cliente] = \
            self.faturamento_por_cliente.get(nome_cliente, 0) + custo

        print(f"Locação realizada: {equipamento.nome} | Total: R${custo:.2f}")

    def equipamentos_disponiveis(self):
        return [equip.nome for equip in self.inventario if equip.status == "Disponível"]
    

#teste de código 

locadora = Locadora()

locadora.cadastrar_equipamento(Equipamento(1, "Furadeira", 30))
locadora.cadastrar_equipamento(Equipamento(2, "Serra", 50))

print(locadora.equipamentos_disponiveis())

locadora.realizar_locacao("Gabriel", 1, 2)

print(locadora.equipamentos_disponiveis())
print(locadora.faturamento_por_cliente)