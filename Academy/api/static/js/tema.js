document.addEventListener('DOMContentLoaded', function () {
    const botaoToggleTema = document.getElementById('toggle-theme');
    const body = document.body;

    botaoToggleTema.addEventListener('click', function () {
        body.classList.toggle('dark-mode');
    });
});
