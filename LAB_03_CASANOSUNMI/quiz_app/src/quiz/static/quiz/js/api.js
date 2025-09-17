// Carga de exámenes por API y creación rápida por POST (JSON)

async function fetchExams() {
  const grid = document.getElementById('exams-grid');
  grid.innerHTML = '<div class="text-center text-muted">Cargando...</div>';
  try {
    const res = await fetch('/api/exams/');
    const data = await res.json();

    grid.innerHTML = '';
    if (!data.length) {
      grid.innerHTML = '<div class="alert alert-info">No hay exámenes. ¡Crea el primero!</div>';
      return;
    }

    data.forEach(ex => {
      const card = document.createElement('div');
      card.className = 'exam-card';
      card.innerHTML = `
        <div class="exam-title">${ex.title}</div>
        <div class="exam-desc">${ex.description ? ex.description : ''}</div>
        <div class="exam-meta">
          <span class="badge-pill">${ex.question_count} preguntas</span>
          <a class="btn btn-sm btn-gradient" href="/exam/${ex.id}/">Ver</a>
        </div>
      `;
      grid.appendChild(card);
    });
  } catch (e) {
    grid.innerHTML = `<div class="alert alert-danger">Error al cargar: ${e}</div>`;
  }
}

async function createExamByAPI(evt){
  evt.preventDefault();
  const title = document.getElementById('api-title').value.trim();
  const description = document.getElementById('api-description').value.trim();

  if(!title){
    alert('El título es requerido');
    return;
  }
  try{
    const res = await fetch('/api/exams/', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ title, description })
    });
    if(!res.ok){
      const txt = await res.text();
      throw new Error(txt || 'Error en POST');
    }
    document.getElementById('api-title').value = '';
    document.getElementById('api-description').value = '';
    await fetchExams();
  }catch(e){
    alert('No se pudo crear el examen: ' + e.message);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('api-create-exam');
  if(form){
    form.addEventListener('submit', createExamByAPI);
  }

  const reload = document.getElementById('reload');
  if(reload){
    reload.addEventListener('click', fetchExams);
  }

  // Carga inicial
  fetchExams();
});




document.addEventListener("DOMContentLoaded", () => {
    const examListContainer = document.getElementById("exam-list");

    // 1. Cargar lista de exámenes
    fetch("/api/exams/")
        .then(res => res.json())
        .then(data => {
            data.forEach(exam => {
                const card = document.createElement("div");
                card.className = "card";
                card.innerHTML = `
                    <h3>${exam.title}</h3>
                    <p>${exam.description}</p>
                    <button onclick="loadExam(${exam.id})">Ver Detalles</button>
                `;
                examListContainer.appendChild(card);
            });
        });
});

// 2. Función para cargar detalles de un examen
function loadExam(examId) {
    fetch(`/api/exams/${examId}/`)
        .then(res => res.json())
        .then(exam => {
            const examListContainer = document.getElementById("exam-list");
            examListContainer.innerHTML = `
                <h2>${exam.title}</h2>
                <p>${exam.description}</p>
                <h3>Preguntas:</h3>
                <ul>
                    ${exam.questions.map(q => `
                        <li>
                            <strong>${q.text}</strong>
                            <ul>
                                ${q.choices.map(c => `<li>${c.text}</li>`).join("")}
                            </ul>
                        </li>
                    `).join("")}
                </ul>
                <button onclick="window.location.reload()">Volver</button>
            `;
        });
}
