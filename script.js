document.getElementById("claseForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const alumno = document.getElementById("alumno").value;
    const nivel = document.getElementById("nivel").value;
    const especialidad = document.getElementById("especialidad").value;
    const mensaje = document.getElementById("mensaje").value;

    const output = document.getElementById("output");
    const contenedor = document.createElement("div");
    contenedor.classList.add("solicitud-item");

    contenedor.innerHTML = `
        <h3>Solicitud de ${alumno}</h3>
        <p><strong>Nivel:</strong> ${nivel}</p>
        <p><strong>Especialidad:</strong> ${especialidad}</p>
        <p><strong>Tema a reforzar:</strong> ${mensaje}</p>
        <hr>
    `;

    output.appendChild(contenedor);

    // Reiniciar formulario
    document.getElementById("claseForm").reset();
});
