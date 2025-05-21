document.addEventListener('DOMContentLoaded', function() {
    const clienteSelect = document.getElementById('cliente');

    clienteSelect.addEventListener('change', function() {
        const clienteId = clienteSelect.value;
        if (clienteId) {
            fetch('/get-cliente-data/${clienteId}/')
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        console.error('Erro:', data.error);
                    } else {
                        document.getElementById('endereco').value = data.endereco || '';
                        document.getElementById('cnpj').value = data.cnpj || '';
                        document.getElementById('inicio_de_contrato').value = data.inicio_de_contrato || '';
                        document.getElementById('vigencia').value = data.vigencia || '';
                    }
                })
                .catch(error => console.error('Erro na solicitação:', error));
        } else {
            // Limpar campos se nenhum cliente estiver selecionado
            document.getElementById('endereco').value = '';
            document.getElementById('cnpj').value = '';
            document.getElementById('inicio_de_contrato').value = '';
            document.getElementById('vigencia').value = '';
        }
    });
});