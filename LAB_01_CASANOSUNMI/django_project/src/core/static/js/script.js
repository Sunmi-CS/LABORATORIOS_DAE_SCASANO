// Capturamos formulario
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("item-form");
    const list = document.getElementById("items-list");

    // Evento de envío
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const name = document.getElementById("name").value;
        const description = document.getElementById("description").value;

        const response = await fetch("/api/add/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()
            },
            body: JSON.stringify({ name, description })
        });

        const data = await response.json();

        if (data.id) {
            // Añadimos al listado sin recargar
            const li = document.createElement("li");
            li.textContent = `${data.name} - ${data.description}`;
            list.appendChild(li);
            form.reset();
        } else {
            alert("Error al agregar item");
        }
    });

    // Obtiene CSRF token desde cookie (necesario para Django)
    function getCSRFToken() {
        let name = "csrftoken=";
        let decodedCookie = decodeURIComponent(document.cookie);
        let ca = decodedCookie.split(";");
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i].trim();
            if (c.indexOf(name) === 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }
});
