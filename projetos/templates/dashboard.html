{% extends 'base.html' %}

{% block title %}Dashboard{% endblock %}

{% block content %}
<div class="container">

    <!-- Card com total de inserções -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="card text-center">
                <div class="card-body">
                    <h4>Total de Inserções</h4>
                    <p class="display-4">{{ total_insercoes }}</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Gráficos de Pizza e Rosca -->
    <div class="row mb-4">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header text-center">
                    Inserções por Local
                </div>
                <div class="card-body">
                    <canvas id="chartLocais"></canvas>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <div class="card-header text-center">
                    Inserções por Operação
                </div>
                <div class="card-body">
                    <canvas id="chartOperacoes"></canvas>
                </div>
            </div>
        </div>
    </div>

    <!-- Gráficos de Barras e Linhas -->
    <div class="row">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header text-center">
                    Inserções por Usuário
                </div>
                <div class="card-body">
                    <canvas id="chartUsuarios"></canvas>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <div class="card-header text-center">
                    Inserções por Data
                </div>
                <div class="card-body">
                    <canvas id="chartDatas"></canvas>
                </div>
            </div>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    // Dados para os gráficos
    const usuariosLabels = {{ usuarios_labels|safe }};
    const usuariosData = {{ usuarios_data|safe }};
    const locaisLabels = {{ locais_labels|safe }};
    const locaisData = {{ locais_data|safe }};
    const operacoesLabels = {{ operacoes_labels|safe }};
    const operacoesData = {{ operacoes_data|safe }};
    const datasLabels = {{ datas_labels|safe }};
    const datasData = {{ datas_data|safe }};

    // Gráfico de Inserções por Usuário
    new Chart(document.getElementById('chartUsuarios'), {
        type: 'bar',
        data: {
            labels: usuariosLabels,
            datasets: [{
                label: 'Inserções por Usuário',
                data: usuariosData,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

    // Gráfico de Inserções por Local
    new Chart(document.getElementById('chartLocais'), {
        type: 'pie',
        data: {
            labels: locaisLabels,
            datasets: [{
                label: 'Inserções por Local',
                data: locaisData,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

    // Gráfico de Inserções por Operação
    new Chart(document.getElementById('chartOperacoes'), {
        type: 'doughnut',
        data: {
            labels: operacoesLabels,
            datasets: [{
                label: 'Inserções por Operação',
                data: operacoesData,
                backgroundColor: [
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)'
                ],
                borderColor: [
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

    // Gráfico de Inserções por Data
    new Chart(document.getElementById('chartDatas'), {
        type: 'line',
        data: {
            labels: datasLabels,
            datasets: [{
                label: 'Inserções por Data',
                data: datasData,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
</script>
{% endblock %}
