// core/static/js/scripts.js

// core/static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('demanda-form');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Impede a submissão padrão
            const formData = new FormData(form);
            fetch(form.action || window.location.href, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest', // Indica uma requisição AJAX
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken') // Inclui o token CSRF
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Redireciona para a URL especificada
                    window.location.href = data.redirect_url;
                } else {
                    // Exibe erros no formulário
                    displayFormErrors(data.errors);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }

    function displayFormErrors(errors) {
        // Remove erros anteriores
        const errorElements = document.querySelectorAll('.text-danger');
        errorElements.forEach(el => el.remove());

        // Adiciona novos erros
        for (const [field, msgs] of Object.entries(errors)) {
            const input = document.getElementById(`id_${field}`);
            if (input) {
                const errorDiv = document.createElement('div');
                errorDiv.classList.add('text-danger');
                errorDiv.innerHTML = msgs.join('<br>');
                input.parentNode.appendChild(errorDiv);
            }
        }
    }
});



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
