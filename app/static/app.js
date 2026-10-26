const formulario = document.querySelector('#form-materia');
const lista = document.querySelector('#lista-materias');
const mensaje = document.querySelector('#mensaje');

async function cargarMaterias() {
  const respuesta = await fetch('/api/materias');
  const materias = await respuesta.json();
  lista.replaceChildren();
  materias.forEach((materia) => {
    const item = document.createElement('li');
    const color = document.createElement('span');
    color.className = 'color';
    color.style.background = materia.color;
    color.setAttribute('aria-hidden', 'true');
    const nombre = document.createElement('span');
    nombre.textContent = materia.nombre;
    const boton = document.createElement('button');
    boton.type = 'button';
    boton.dataset.id = materia.id;
    boton.textContent = 'Eliminar';
    item.append(color, nombre, boton);
    lista.append(item);
  });
}

formulario.addEventListener('submit', async (evento) => {
  evento.preventDefault();
  const datos = Object.fromEntries(new FormData(formulario));
  const respuesta = await fetch('/api/materias', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(datos) });
  if (!respuesta.ok) { mensaje.textContent = (await respuesta.json()).detail; return; }
  formulario.reset(); mensaje.textContent = 'Materia registrada.'; await cargarMaterias();
});

lista.addEventListener('click', async (evento) => {
  if (!evento.target.matches('button')) return;
  const id = evento.target.dataset.id;
  const aviso = await fetch(`/api/materias/${id}`, { method: 'DELETE' }).then((respuesta) => respuesta.json());
  const texto = `Se eliminarán ${aviso.tareas_afectadas} tarea(s). ¿Deseas continuar?`;
  if (!window.confirm(texto)) return;
  await fetch(`/api/materias/${id}?confirmar=true`, { method: 'DELETE' });
  await cargarMaterias();
});

cargarMaterias();
