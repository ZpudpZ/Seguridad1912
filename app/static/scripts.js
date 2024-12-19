// Función para cargar los archivos disponibles al cargar la página
document.addEventListener('DOMContentLoaded', function () {
    loadFiles();
});

// Función para cargar los archivos disponibles
function loadFiles() {
    // Aquí deberías hacer una solicitud al backend para obtener los archivos disponibles.
    // Por ahora, simularemos algunos archivos.
    const files = [
        { name: "archivo1.txt", url: "/download/encrypted_archivo1.txt" },
        { name: "archivo2.txt", url: "/download/encrypted_archivo2.txt" }
    ];

    const fileList = document.getElementById("file-list");
    fileList.innerHTML = ''; // Limpiar la lista antes de cargar

    files.forEach(function (file) {
        const li = document.createElement("li");
        li.classList.add("list-group-item");
        li.innerHTML = `
            <span>${file.name}</span>
            <a href="${file.url}" class="btn btn-link">Descargar</a>
        `;
        fileList.appendChild(li);
    });
}
