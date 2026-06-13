document.addEventListener('DOMContentLoaded', function () {

    // Resaltar enlace activo en la navegacion
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(function (link) {
        if (currentPath.startsWith(link.getAttribute('href'))) {
            link.style.color = '#ffffff';
            link.style.borderBottom = '2px solid #ffffff';
            link.style.paddingBottom = '2px';
        }
    });

    // Confirmacion al cerrar pedido
    const btnCerrar = document.querySelector('.btn-cerrar');
    if (btnCerrar) {
        btnCerrar.addEventListener('click', function (e) {
            const confirmado = confirm('Confirmar cierre de mesa y cobro al cliente?');
            if (!confirmado) {
                e.preventDefault();
            }
        });
    }

    // Confirmacion al eliminar producto
    const botonesEliminar = document.querySelectorAll('.btn-eliminar');
    botonesEliminar.forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            const confirmado = confirm('Desea eliminar este producto del inventario?');
            if (!confirmado) {
                e.preventDefault();
            }
        });
    });

});