const criarTarefa = (titulo) => ({ titulo, concluida: false });

const concluirTarefa = (tarefa) => ({ ...tarefa, concluida: true });

const adicionarTarefa = (lista, tarefa) => [...lista, tarefa];

const listarTarefas = (lista) =>
 lista.map((t) => `${t.titulo} - ${t.concluida ? 'Concluída' : 'Pendente'}`);