class Tarefa:
 def __init__(self, titulo, concluida=False):
        self.titulo = titulo
        self.concluida = concluida


 def concluir(self):
    self.concluida = True

class GerenciadorTarefas:
 def __init__(self):
    self.tarefas = []
 def adicionar(self, tarefa):
    self.tarefas.append(tarefa)

 def listar(self):
    return [(t.titulo, t.concluida) for t in self.tarefas]