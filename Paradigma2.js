function criarTarefa(titulo, descricao = "") {
    return { titulo, descricao, concluida: false };
  }
  
  function concluirTarefa(tarefa) {
    return { ...tarefa, concluida: true };
  }
  
  function adicionarTarefa(lista, tarefa) {
    return [...lista, tarefa];
  }
  
  function listarTarefas(lista) {
    return lista.map(
      (t) =>
        `Tarefa: ${t.titulo} | ${t.descricao} | Status: ${
          t.concluida ? "Concluída" : "Pendente"
        }`
    );
  }
  
  // Exemplo de uso
  let tarefas = [];
  tarefas = adicionarTarefa(tarefas, criarTarefa("Estudar JS", "Aprender funções puras"));
  tarefas = adicionarTarefa(tarefas, criarTarefa("Ler livro", "Livro sobre lógica funcional"));
  tarefas[0] = concluirTarefa(tarefas[0]);
  
  listarTarefas(tarefas).forEach((t) => console.log(t));
  