const booksGrid = document.getElementById('booksGrid');
const reloadBtn = document.getElementById('reloadBtn');
const bookSelect = document.getElementById('bookSelect');
const reviewForm = document.getElementById('reviewForm');

async function loadBooks(){
  booksGrid.innerHTML = '<div class="card">Cargando...</div>';
  try{
    const res = await fetch('/api/books/');
    const data = await res.json();
    booksGrid.innerHTML = '';
    bookSelect.innerHTML = '<option value="">Selecciona libro</option>';
    data.forEach(b => {
      // card
      const card = document.createElement('article');
      card.className = 'card';
      card.innerHTML = `
        <h3>${escapeHtml(b.title)}</h3>
        <div class="meta">Autor: ${escapeHtml(b.author.name)} · ISBN: ${escapeHtml(b.isbn || '-')}</div>
        <p class="meta">${b.publication_date || ''}</p>
        <div style="margin-top:10px">
          <a href="/books/${b.id}/" class="btn">Ver detalle (HTML)</a>
          <button class="btn" onclick="loadDetail(${b.id})" style="margin-left:8px">Ver detalle (API)</button>
        </div>
      `;
      booksGrid.appendChild(card);

      // select
      const opt = document.createElement('option');
      opt.value = b.id;
      opt.textContent = b.title;
      bookSelect.appendChild(opt);
    });
  }catch(err){
    booksGrid.innerHTML = '<div class="card">Error al cargar.</div>';
    console.error(err);
  }
}

async function loadDetail(id){
  booksGrid.innerHTML = '<div class="card">Cargando detalle...</div>';
  try{
    const res = await fetch(`/api/books/${id}/`);
    if(!res.ok) throw new Error('No encontrado');
    const b = await res.json();
    booksGrid.innerHTML = '';
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
      <h3>${escapeHtml(b.title)}</h3>
      <p class="meta">Autor: ${escapeHtml(b.author.name)}</p>
      <p>${escapeHtml(b.summary || '')}</p>
      <h4>Categories</h4>
      <ul>${b.categories.map(c => `<li>${escapeHtml(c.name)}</li>`).join('')}</ul>
      <h4>Publications</h4>
      <ul>${(b.publications||[]).map(p => `<li>${escapeHtml(p.publisher.name)} — ${escapeHtml(p.country)} (${escapeHtml(p.date_published)})</li>`).join('')}</ul>
      <div style="margin-top:12px"><button class="btn" onclick="loadBooks()">Volver</button></div>
    `;
    booksGrid.appendChild(card);
  }catch(e){
    booksGrid.innerHTML = '<div class="card">Error al obtener detalle.</div>';
    console.error(e);
  }
}

reloadBtn && reloadBtn.addEventListener('click', loadBooks);

reviewForm && reviewForm.addEventListener('submit', async (ev) => {
  ev.preventDefault();
  const bookId = bookSelect.value;
  const rating = document.getElementById('rating').value;
  const comment = document.getElementById('comment').value;
  const userId = document.getElementById('userId').value;

  if(!bookId || !rating || !userId){ alert('Selecciona libro, rating y user_id'); return; }

  try{
    const res = await fetch(`/api/books/${bookId}/reviews/`, {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ user_id: parseInt(userId), rating: parseInt(rating), comment })
    });
    if(res.status === 201){
      alert('Review creada!');
      reviewForm.reset();
    } else {
      const txt = await res.text();
      alert('Error: ' + txt);
    }
  }catch(err){
    console.error(err);
    alert('Error al enviar review');
  }
});

// pequeños helpers
function escapeHtml(s){
  if(!s) return '';
  return String(s).replace(/[&<>"']/g, (m) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m]));
}

// carga inicial
document.addEventListener('DOMContentLoaded', loadBooks);
