class Tarefa:
    def __init__(self, titulo, descricao="", concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"Tarefa: {self.titulo} | {self.descricao} | Status: {status}"

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, titulo, descricao=""):
        nova_tarefa = Tarefa(titulo, descricao)
        self.tarefas.append(nova_tarefa)

    def concluir_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                tarefa.concluir()
                return True
        return False

    def listar(self):
        for tarefa in self.tarefas:
            print(tarefa)

if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()
    gerenciador.adicionar("Estudar Python", "Praticar orientação a objetos")
    gerenciador.adicionar("Ler artigo", "Artigo sobre paradigmas de programação")
    gerenciador.concluir_tarefa("Estudar Python")
    gerenciador.listar()
