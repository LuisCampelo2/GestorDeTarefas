// Espera o DOM estar completamente carregado
document.addEventListener('DOMContentLoaded', () => {
    const tarefaInput = document.querySelector('#input-tarefa'); // Campo de entrada
    const btnEnviar = document.querySelector('#btn-enviar'); // Botão de adicionar
    const listaTarefas = document.querySelector('#lista-tarefas'); // Lista de tarefas

    // Função para adicionar tarefa
    const adicionarTarefa = () => {
        const tarefa = tarefaInput.value.trim(); // Remove espaços em branco

        if (!tarefa) {
            alert('Por favor, insira uma tarefa válida!');
            return;
        }

        // Adiciona a tarefa na lista (somente no front-end)
        const li = document.createElement('li');
        li.textContent = tarefa;

        // Adiciona botão de remover para cada tarefa
        const btnRemover = document.createElement('button');
        btnRemover.textContent = 'Remover';
        btnRemover.classList.add('btn-remover'); // Classe para estilizar
        btnRemover.addEventListener('click', () => {
            li.remove(); // Remove a tarefa da lista
        });

        li.appendChild(btnRemover); // Adiciona o botão ao item da lista
        listaTarefas.appendChild(li); // Adiciona a tarefa à lista

        tarefaInput.value = ''; // Limpa o campo de entrada
    };

    // Evento de clique no botão de enviar
    btnEnviar.addEventListener('click', adicionarTarefa);

    // Permite adicionar tarefa pressionando "Enter"
    tarefaInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            adicionarTarefa();
        }
    });
});

